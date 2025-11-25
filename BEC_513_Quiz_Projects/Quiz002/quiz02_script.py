import pandas as pd, matplotlib.pyplot as plt, sys
df = pd.read_csv(sys.stdin, sep="\t", header=None, names=["x", "y", "g"])
for gene, group in df.groupby("g"):
    plt.plot(group.x, group.y, label=gene)
plt.legend()
plt.savefig("output.png")
