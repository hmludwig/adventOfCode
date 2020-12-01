import sys

f = open(sys.argv[1])
data = f.read().split()
data = [int(i) for i in data]
