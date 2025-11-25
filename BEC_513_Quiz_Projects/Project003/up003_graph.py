import pandas as pd, matplotlib.pyplot as plt, sys

df = pd.read_csv(sys.stdin, sep="\t", header=None, names=["x", "y", "i"])
fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 3]})

for i, lim in enumerate([(-500, 500), (-200, 200)]):
    sc = ax[i].scatter(df.x, df.y, c=df.i, cmap="BuPu", s=1, alpha=0.7)
    ax[i].set_ylim(0, 200); ax[i].set_xlim(*lim)
    fig.colorbar(sc, ax=ax[i], label="Fragment centre count" if i else None)
fig.text(0.5, 0.02, "Distance from motif center (bp)", ha="center")
fig.text(0.02, 0.5, "cfDNA fragment length (bp)", va="center", rotation="vertical")
plt.savefig("output.png", dpi=600, bbox_inches="tight")
