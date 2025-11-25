import matplotlib.pyplot as plt
import sys
import pandas as pd

# Read input BED from stdin
bed_df = pd.read_csv(sys.stdin, sep="\t", header=None, low_memory=False)
bed_df["length"] = bed_df[2] - bed_df[1]
length_distribution = bed_df["length"].value_counts(normalize=True).sort_index()

# Plot query distribution
plt.plot(length_distribution.index, length_distribution.values,
         color="purple", label=f"query (n={len(bed_df)})", linewidth=0.5)

# Load reference file
with open(sys.argv[1]) as ref_file:
    reference_df = pd.read_csv(ref_file, sep="\t", header=None, names=["length", "frequency"])

# Plot reference distribution
plt.plot(reference_df["length"], reference_df["frequency"],
         color="green", label="reference", linewidth=0.5)

# Sampling counts calculation
reference_df["sample_count"] = ((reference_df["frequency"] * len(bed_df)) / 3).round()

sampled_data = []
for _, ref_row in reference_df.iterrows():
    subset = bed_df[bed_df["length"] == ref_row["length"]]
    n_samples = min(int(ref_row["sample_count"]), len(subset))
    if n_samples > 0:
        sampled = subset.sample(n=n_samples, random_state=1)
        sampled_data.append(sampled)

combined_df = pd.concat(sampled_data)
combined_df.to_csv(sys.stdout, sep="\t", header=False, index=False)

rescaled_distribution = combined_df["length"].value_counts(normalize=True)
plt.scatter(rescaled_distribution.index, rescaled_distribution.values,
            color="skyblue", label=f"rep (n={len(combined_df)})", marker="*", s=15)
plt.legend()
plt.savefig("output.png")
