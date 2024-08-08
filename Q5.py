import sys

input_content = sys.stdin.read().split('\n')
string = ''
for i in range(len(input_content)):
    string += input_content[i][::-1] + '\n'
print(string)
