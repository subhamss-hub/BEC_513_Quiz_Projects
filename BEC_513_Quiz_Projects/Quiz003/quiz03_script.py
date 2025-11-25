import sys
with open(sys.argv[1]) as f:
    sec = {line.split("\t", 1)[0]: line.rstrip().split("\t", 1)[1] for line in f}
for line in sys.stdin:
    row = line.rstrip().split("\t", 1)
    if row[0] in sec:
        sys.stdout.write(f"{line.rstrip()}\t{sec[row[0]]}\n")
