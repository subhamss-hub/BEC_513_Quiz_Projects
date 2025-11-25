import sys, os, pandas as pd

root = sys.argv[1]
ids, tpms = [], []
for d in os.listdir(root):
    for f in os.listdir(os.path.join(root, d)):
        if f.endswith("tsv"):
            with open(os.path.join(root, d, f)) as handle:
                for line in handle:
                    row = line.strip().split("\t")
                    if "NKX2-1" in row:
                        ids.append(d)
                        tpms.append(row[6])
                        break
tpm_df = pd.DataFrame({"id": ids, "tpm": tpms})

cond_ids, conds = [], []
for line in sys.stdin:
    row = line.strip().split("\t")
    if "Solid Tissue Normal" in line:
        cond_ids.append(row[0])
        conds.append("Solid Tissue Normal")
    if "Primary Tumor" in line:
        cond_ids.append(row[0])
        conds.append("Primary Tumor")
cond_df = pd.DataFrame({"id": cond_ids, "cond": conds})

pd.merge(tpm_df, cond_df, on="id").to_csv("output.tsv", sep="\t", index=False, header=False)