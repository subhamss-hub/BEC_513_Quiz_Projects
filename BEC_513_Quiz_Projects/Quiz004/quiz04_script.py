import sys, pandas as pd
n = int(sys.argv[1])
df = pd.read_csv(sys.stdin, header=None, names=["num"])
df["q1"] = pd.qcut(df["num"], n, labels=[f"q{i+1}" for i in range(n)])
df["q2"] = df["q1"]
df["bin"] = pd.qcut(df["num"], n)
df.to_csv(sys.stdout, sep="\t", index=False, header=False)
