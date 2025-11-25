import pandas as pd
import sys

# Read input data from stdin as DataFrame
data = pd.read_csv(sys.stdin, sep="\t", header=None, low_memory=False)

# Read selection (categories) file into a list
with open(sys.argv[1], "r") as sel_file:
    categories_list = [line.rstrip() for line in sel_file]

# Assign categories for sorting
data[0] = pd.Categorical(data[0], categories=categories_list)

# Sort by columns 0, 1, and 2
sorted_data = data.sort_values([0, 1, 2])

# Output to TSV, no header, no index
sorted_data.to_csv(sys.stdout, sep="\t", header=False, index=False)
