standard_prompt = '''
Hi, your job is to interpret a function f(x) that is implemented in the {DIR2FUNC} script. f(x) takes string inputs.
All you can do is call f(x) on an input string by running PYTHON({DIR2FUNC} string). 
Try to describe the function implemented by f(x) by running experiments on it. 
You can call the function on multiple inputs at a time by running PYTHON({DIR2FUNC} string1 string2 string3 ...). 
We encourage testing a large range of inputs before writing a description.
The goal is to find a good simple description of f(x) that explains most of the function behavior. f(x) may combine multiple different operations.
Your description of the function should be in the following form.
[DESCRIPTION]: Describe what the function is doing in language.
'''

cot_prompt = '''
Hi, your job is to interpret a function f(x) that is implemented in the {DIR2FUNC} script. f(x) takes string inputs.
All you can do is call f(x) on an input string by running PYTHON({DIR2FUNC} string). 
Try to describe the function implemented by f(x) by running experiments on it. 
You can call the function on multiple inputs at a time by running PYTHON({DIR2FUNC} string1 string2 string3 ...).
We encourage an iterative approach where you test a large range of inputs before writing a description.
The goal is to find a good simple description of f(x) that explains most of the function behavior. f(x) may combine multiple different operations.

Make a plan of your iterative approach then write the description. Your output should be in the following format:

Plan: Your plan here.

[DESCRIPTION]: Describe what the function is doing in language.
'''

vote_prompt = '''Given an instruction and several choices, decide which choice is most promising. Analyze each choice in detail, then conclude in the last line "The best choice is {s}", where s the integer id of the choice.
'''

# compare_prompt = '''Briefly analyze the coherency of the following two passages. Conclude in the last line "The more coherent passage is 1", "The more coherent passage is 2", or "The two passages are similarly coherent".
# '''

score_prompt = '''Analyze the following passage, then at the last line conclude "Thus the coherency score is {s}", where s is an integer from 1 to 10.
'''
