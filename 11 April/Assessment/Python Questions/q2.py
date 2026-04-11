import ast
import sys

def uniqueChar(data):
    words = data.split()
    unique_counts = {word: len(set(word)) for word in words}
    return unique_counts

raw = sys.stdin.read().strip()

res = ast.literal_eval(raw)

print(uniqueChar(res))

#i/p : ["Python is programming language"]
#o/p: {'Python': 6, 'is': 2, 'programming': 10, 'language': 6} #unique characters in each word and their count