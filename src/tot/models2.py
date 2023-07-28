import argparse
import openai
import backoff
import regex
import re
import pandas as pd
import subprocess
from getpass import getpass
import pandas as pd
import os
from tqdm import tqdm
from IPython import embed
import time
from random import random, uniform
import random as rd
import torch.nn as nn
import json
import warnings
# warnings.filterwarnings("ignore")
import numpy as np
from tot.call_interpreter import ask_model

# from tot.infer import function_name

rd.seed(0000)

regx = [r"([A-Z]+\(((?:[^()\"']|(?:\"[^\"]*\")|(?:'[^']*')|\((?1)*\))*)\))",
        r'''(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|\b[^,]+)''']

args = {"model": "gpt-4", "func_category": "strings", "dataset_path": "./results/",
        "function_path": "src/tot/",
        "temp_function_path": "./temp/", "n_func": 1, }


class SessionState:
    def __init__(self):
        self.running = False
        self.followup = False
        self.prompt = ''
        self.command = ''
        self.acceptreject = False
        self.history = []
        self.totalCost = 0
        self.displayChat = False
        self.displayCost = False


newSession = True
manualApproval = False


def followup(state):
    state.followup, state.running = True, True


def formatTable(table):
    lines = ''
    for x, i in enumerate(table['GPT Commands']):
        lines += '{} - {}\n'.format(table['GPT Commands'][x], table['GPT Explanations'][x])
    return (lines)


commandTable = pd.DataFrame({
    'GPT Commands': ['PYTHON(function.py)'],
    'GPT Explanations': [
        'Run a python script with the given file name. Use quotes for the filename argument. Do not use quotes in the function command itself.'],
    'Raw Translation': ['python {}']
})


# return the prompt according to the task
def return_sysPrompt(model):
    if model == 'gpt-4':
        sysPrompt = 'You now have access to some commands to help complete the user\'s request. ' \
                    'You are able to access the user\'s machine with these commands. In every message you send, ' \
                    'include "COMMAND: " with your command at the end. Here is a list of commands with ' \
                    'explanations of how they are used:\n{}\n When you use a command, the user will respond ' \
                    'with "Response: " followed by the output of the commmand. Use this output to help the ' \
                    'user complete their request.'
    else:
        sysPrompt = 'You now have access to some commands to help complete the user\'s request. ' \
                    'You are able to access the user\'s machine with these commands, and to get the corresponding output from the user. ' \
                    'In every message you send, ' \
                    'include "COMMAND: " with your command at the end. ' \
                    'When you use a command, the user will respond ' \
                    'with "Response: " followed by the output of the commmand.' \
                    'Do not run anything yourself. Only state the command and wait for the user to provide its output. ' \
                    'Use this output to help the ' \
                    'user complete their request. ' \
                    'Here is a list of commands with ' \
                    'explanations of how they are used:\n{}\n ' \
                    '(Let the user provide the respones for your commands, do not estimate them yourself without feedback from the user).' \
            # 'Do not run anything yourself. Only state the command. ' \
    return sysPrompt


def runCmd(flag, state):
    if flag:
        try:
            p = subprocess.Popen(state.command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output, errors = p.communicate()
            state.prompt = 'Response: ' + output.decode("utf-8")
            # print(output.decode("utf-8"))
            if errors:
                state.prompt += 'Error occurred, please try again (some of the input values might be undefined)'
                # state.prompt += 'Errors: ' + errors.decode("utf-8")
        except subprocess.CalledProcessError as e:
            state.prompt = 'Response: ' + e.output.decode("utf-8")
    else:
        state.prompt = "Response: User rejected this command"
    followup(state)


def define_prompt(prompt_template, dir2func):
    prompt = prompt_template.format(DIR2FUNC=os.path.join(dir2func))
    return prompt


def save_description(response, filepath):
    description = response.rsplit('[DESCRIPTION]: ')[-1]
    description = description.rsplit('[DOMAIN]: ')[0]
    with open(filepath, 'w') as f:
        f.write(description)
    f.close()


def save_fullhistory(history, filepath):
    with open(filepath + '.txt', 'a') as f:
        for i in history:
            if i['role'] == 'user':
                f.write('\nuser:\n' + i['content'])
            elif i['role'] == 'assistant':
                f.write('\nassistant:\n' + i['content'])
    with open(filepath + '.json', 'w') as file:
        json.dump(history, file)
    f.close()


def interp_func(prompt, model, debug=False):
    state = SessionState()
    sysPrompt = return_sysPrompt(model)
    round_count = 0
    while True:
        state.running = True
        if state.running:
            state.running = False
            if not state.followup:
                state.prompt = prompt
            if (newSession or state.history == []) and (not state.followup):
                state.history = [{'role': 'system', 'content': sysPrompt.format(formatTable(commandTable))}]
            else:
                state.history[0] = {'role': 'system', 'content': sysPrompt.format(formatTable(commandTable))}
            state.followup = False
            response, state = ask_model(state.prompt, model, state)
            if len(regex.findall(regx[0], response)) >= 1:
                cmd = regex.findall(regx[0], response)[0][0]
                pIndex = cmd.index('(')
                stem = cmd[:pIndex]
                rawArgs = cmd[pIndex + 1:][:-1]
                cmdId = -1

                for x, i in enumerate(commandTable['GPT Commands']):
                    if stem in i:
                        cmdId = x
                        break

                rawArgs.replace('\n', '\\n')
                rawArgs.replace('\\\n', '\\n')
                if cmdId == -1:
                    state.prompt = 'Response: Unrecognized command'
                    followup(state)
                elif "'''" in rawArgs:
                    state.prompt = 'Response: Error parsing multi-line string (\'\'\') Use a single line with escaped newlines instead (")'
                    followup(state)
                elif '"""' in rawArgs:
                    state.prompt = 'Response: Error parsing multi-line string (\"\"\") Use a single line with escaped newlines instead (")'
                    followup(state)
                else:
                    state.command = commandTable['Raw Translation'][cmdId]
                    args = []
                    if rawArgs != '':
                        args = re.findall(regx[1], rawArgs)  # [rawArgs]
                        state.command = state.command.format(*args)

                    singleQuotes = False
                    for i in args:
                        if i.startswith("'"):
                            singleQuotes = True
                            state.prompt = "Response: Error parsing argument in single quotes. Use double quotes around the argument instead"
                            followup(state)
                            break

                    if not singleQuotes:
                        if manualApproval:
                            state.acceptreject = False
                        else:
                            runCmd(1, state)

        # round_count+=1

        if state.acceptreject:
            print(
                'GPT is trying to run the following command: ' + state.command + '\nPlease accept or reject this request.')
            decision = input('Accept or Reject [Accept, Reject]:')
            if decision.lower() == 'accept':
                state.acceptreject = False
                runCmd(1, state)
            elif decision.lower() == 'reject':
                state.acceptreject = False
                runCmd(0, state)

        if debug:
            print(response)
            print(state.prompt)

        if "[DESCRIPTION]" in response:
            # print('')
            return (response, state.history)

        if round_count > 100:
            raise Warning("Interpretation process exceeded 100 rounds")
            return ('', '')


def copy_func(source, target, vicuna_server=None, llama_hf_path=None):
    os.system(f'scp {source} {target}/function.py')

    return


def remove_func(target):
    os.system(f'rm {target}')


def remove_temp_folder(target):
    os.system(f'rm -r {target}')


completion_tokens = prompt_tokens = 0

api_key = os.getenv("OPENAI_API_KEY", "")
if api_key != "":
    openai.api_key = api_key
else:
    print("Warning: OPENAI_API_KEY is not set")

api_base = os.getenv("OPENAI_API_BASE", "")
if api_base != "":
    print("Warning: OPENAI_API_BASE is set to {}".format(api_base))
    openai.api_base = api_base


@backoff.on_exception(backoff.expo, openai.error.OpenAIError)
def completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


def gpt(prompt, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
    messages = [{"role": "user", "content": prompt}]
    return chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)


def gptsolve(prompt, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None, function_name=None) -> list:
    messages = [{"role": "user", "content": prompt}]
    return findchatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop,
                       function_name=function_name)


def chatgpt(messages, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None) -> list:
    global completion_tokens, prompt_tokens
    outputs = []
    while n > 0:
        cnt = min(n, 20)
        n -= cnt
        res = completions_with_backoff(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens,
                                       n=cnt, stop=stop)
        outputs.extend([choice["message"]["content"] for choice in res["choices"]])
        # log completion tokens
        completion_tokens += res["usage"]["completion_tokens"]
        prompt_tokens += res["usage"]["prompt_tokens"]
    return outputs


def findchatgpt(messages, model="gpt-4", temperature=0.7, max_tokens=1000, n=1, stop=None, function_name=None) -> list:
    outputs = []
    t_start = time.time()
    count = 0
    try:
        remove_temp_folder(args["temp_function_path"])
    except:
        pass
    os.makedirs(args["temp_function_path"], exist_ok=True)

    function = "find_dataset/" + function_name + "/function_code.py"

    path2save = os.path.join(args["dataset_path"], args["model"], function_name)

    os.makedirs(path2save, exist_ok=True)

    copy_func(source=function,
              target=args["temp_function_path"])

    while n > 0:
        while True:
            try:
                response, history = interp_func(messages[0]["content"], args["model"])
                break
            except Exception as e:
                print(e)

        save_fullhistory(history, path2save + '/history' + str(n))
        save_description(response, path2save + '/description' + str(n) + ".txt")
        outputs.append(response)

        n -= 1

    t_end = time.time()
    print(f'total time for {count} functions: {t_end - t_start}')

    remove_temp_folder(args["temp_function_path"])

    return outputs
