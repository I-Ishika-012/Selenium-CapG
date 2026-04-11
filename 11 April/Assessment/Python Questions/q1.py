import ast
import sys

def anagram(data):
    str1, str2 = data
    return sorted(str1) == sorted(str2)

raw = sys.stdin.read().strip()

res = ast.literal_eval(raw)

print(anagram(res))

#i/p : ["listen", "silent"]
#o/p: True