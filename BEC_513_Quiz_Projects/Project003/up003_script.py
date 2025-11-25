import sys
from collections import defaultdict

# Prepare nested dict to count occurrences
counts = defaultdict(lambda: defaultdict(int))

# Read and process each line from stdin
for entry in sys.stdin:
    fields = entry.rstrip().split("\t")
    center_undigested = (int(fields[2]) + int(fields[3])) / 2
    center_digested = (int(fields[8]) + int(fields[9])) / 2
    delta = center_digested - center_undigested
    frag_length = int(fields[11])
    counts[delta][frag_length] += 1

# Output result in TSV to stdout
for delta in counts:
    for frag_length in counts[delta]:
        sys.stdout.write(f"{delta}\t{frag_length}\t{counts[delta][frag_length]}\n")
