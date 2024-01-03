# Reading Data
filename = 'files/input.txt'

with open(filename) as fn:
   ln = fn.readline()

# Keep count of lines
   lncnt = 1
   while ln:
       print("Line {}: {}".format(lncnt, ln.strip()))
       ln = fn.readline()
       lncnt += 1


print("\n")
# Counting Word Frequency
from collections import Counter

with open(r'files/input.txt') as f:
               p = Counter(f.read().split())
               print(p)