import argparse
from tot.methods.bfs import solve
from tot.tasks.strings import StringsTask
import openai

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

args = argparse.Namespace(backend='gpt-4', temperature=0.7, task='strings', naive_run=False, prompt_sample="cot",
                          method_generate='sample', method_evaluate='vote', method_select='greedy', n_generate_sample=2,
                          n_evaluate_sample=2, n_select_sample=1)
func_category = "strings"
base = "00000"

for i in range(15, 16, 1):
    name = base + str(i)
    name = name[len(str(i)):]
    function_name = func_category + "/f" + name

    task = StringsTask()
    ys, infos = solve(args, task, 0, function_name)
    print(ys[0])
