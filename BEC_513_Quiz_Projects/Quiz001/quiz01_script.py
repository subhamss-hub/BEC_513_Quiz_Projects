import sys
col = int(sys.argv[2]) - 1
with open(sys.argv[1]) as f:
    sel = {line.strip() for line in f}
for line in sys.stdin:
    vals = line.strip().split("\t")
    if vals[col] in sel:
        sys.stdout.write(line)
