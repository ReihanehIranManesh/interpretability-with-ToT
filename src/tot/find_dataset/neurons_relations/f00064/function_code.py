import openai
import sys

openai.api_key = "EMPTY"  # Not support yet
openai.api_base = {API_BASE}
model = "vicuna-13b-v1.1"

con1 = 'a river'
con2 = 'the continent where that river is located'
ex = 'the input is in Europe'

def function(input, sys_prompt):
    messages=[
        {"role": "system", "content": sys_prompt},   #system prompt
        {"role": "user", "content": 
         f"I am going to give you an input." + 
         f"If the input is {con1}, reply with only {con2}. " + 
         f"If the input is not {con1}, return 'undefined'. If {ex}, return 'undefined'.\n"+
         f"Reply with a single word. Do not include any additional information other than the output word.\n"+
         f"Input:{input}"
         }
    ]

    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0
    )

    return completion.choices[0].message.content

if __name__ == '__main__':
    outputs = ''
    prompt = "You are a helpful assistant. You apply real-world knowledge to map input words to output words according to a rule provided by the user. Try to be as precise as possible. Do not include additional explanation."
    for arg in sys.argv[1:]:
        x = arg
        outputs += f'({arg}, {function(arg, prompt)}) '
    print(f'Function input - output pairs: {outputs}')