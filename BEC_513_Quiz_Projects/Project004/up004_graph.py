import sys, math
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

nor, tum = [], []
for line in sys.stdin:
    words = line.strip().split("\t")
    val = math.log(float(words[1]) + 1, 2)
    (nor if words[2] == "Solid Tissue Normal" else tum).append(val)

_, p = ttest_ind(tum, nor)
plt.boxplot([nor, tum], notch=True, labels=[
    f"Normal (n={len(nor)})", f"Tumor (n={len(tum)})"])
plt.ylabel("log2(TPM + 1)")
plt.title(f"Lung Adenocarcinoma (p={p:.1e})")
plt.tight_layout()
plt.savefig("output.png")
