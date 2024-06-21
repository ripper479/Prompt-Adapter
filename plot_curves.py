import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


save_dir = "main_curves"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

path = "Results.xlsx"
file = pd.read_excel(path, sheet_name="imcls_fewshot")

datasets = [
    "OxfordPets", "FGVCAircraft", "DTD",
    "EuroSAT", "Caltech101", "UCF101"
]

shots = [1, 2, 4, 8, 16]

COLORS = {
    "zero_shot_clip": "C5",
    "clip_adapter": "C4",
    "meta_adapter": "C0",
    "tip_adapter_f": "C2",
    "tip_adapter": "C1",
    "prompt_adapter": "C3"
}
MS = 3
ALPHA = 1
plt.rcParams.update({"font.size": 12})

average = {
    "zero_shot_clip": 0.,
    "clip_adapter": np.array([0., 0., 0., 0., 0.]),
    "meta_adapter": np.array([0., 0., 0., 0., 0.]),
    "tip_adapter_f": np.array([0., 0., 0., 0., 0.]),
    "tip_adapter": np.array([0., 0., 0., 0., 0.]),
    "prompt_adapter": np.array([0., 0., 0., 0., 0.])
}

for dataset in datasets:
    print(f"Processing {dataset} ...")

    zero_shot_clip = file[dataset][0]

    clip_adapter = file[dataset][2:7]
    clip_adapter = [float(num) for num in clip_adapter]

    meta_adapter = file[dataset][7:12]
    meta_adapter = [float(num) for num in meta_adapter]

    tip_adapter_f = file[dataset][12:17]
    tip_adapter_f = [float(num) for num in tip_adapter_f]

    tip_adapter = file[dataset][17:22]
    tip_adapter = [float(num) for num in tip_adapter]

    prompt_adapter = file[dataset][22:27]
    prompt_adapter = [float(num) for num in prompt_adapter]

    average["zero_shot_clip"] += zero_shot_clip
    average["clip_adapter"] += np.array(clip_adapter)
    average["meta_adapter"] += np.array(meta_adapter)
    average["tip_adapter_f"] += np.array(tip_adapter_f)
    average["tip_adapter"] += np.array(tip_adapter)
    average["prompt_adapter"] += np.array(prompt_adapter)

    # Plot
    values = [zero_shot_clip]
    values += prompt_adapter
    values += tip_adapter
    values += tip_adapter_f
    values += meta_adapter
    values += clip_adapter
    val_min, val_max = min(values), max(values)
    diff = val_max - val_min
    val_bot = val_min - diff*0.05
    val_top = val_max + diff*0.05

    fig, ax = plt.subplots()
    ax.set_facecolor("#EBEBEB")

    ax.set_xticks([0] + shots)
    ax.set_xticklabels([0] + shots)
    ax.set_xlabel("Number of labeled training examples per class")
    ax.set_ylabel("Score (%)")
    ax.grid(axis="x", color="white", linewidth=1)
    ax.axhline(zero_shot_clip, color="white", linewidth=1)
    ax.set_title(dataset)
    ax.set_ylim(val_bot, val_top)

    ax.plot(
        0, zero_shot_clip,
        marker="*",
        markersize=MS*1.5,
        color=COLORS["zero_shot_clip"],
        alpha=ALPHA
    )
    ax.plot(
        shots, clip_adapter,
        marker="o",
        markersize=MS,
        color=COLORS["clip_adapter"],
        label="CLIP-Adapter",
        alpha=ALPHA
    )
    ax.plot(
        shots, meta_adapter,
        marker="o",
        markersize=MS,
        color=COLORS["meta_adapter"],
        label="Meta-Adapter",
        alpha=ALPHA
    )
    ax.plot(
        shots, tip_adapter_f,
        marker="o",
        markersize=MS,
        color=COLORS["tip_adapter_f"],
        label="Tip-Adapter-F",
        alpha=ALPHA
    )
    ax.plot(
        shots, tip_adapter,
        marker="o",
        markersize=MS,
        color=COLORS["tip_adapter"],
        label="Tip-Adapter",
        alpha=ALPHA
    )
    ax.plot(
        shots, prompt_adapter,
        marker="o",
        markersize=MS,
        color=COLORS["prompt_adapter"],
        label="Prompt-Adapter",
        linestyle="dotted",
        alpha=ALPHA
    )

    ax.text(-0.5, zero_shot_clip-diff*1e-8, "Zero-shot-CLIP", color=COLORS["zero_shot_clip"],fontsize='small')
    ax.legend(loc="lower right")

    fig.savefig(f"{save_dir}/{dataset}.png", bbox_inches="tight")


# Plot
average = {k: v/len(datasets) for k, v in average.items()}
zero_shot_clip = average["zero_shot_clip"]
clip_adapter = list(average["clip_adapter"])
meta_adapter = list(average["meta_adapter"])
tip_adapter_f = list(average["tip_adapter_f"])
tip_adapter = list(average["tip_adapter"])
prompt_adapter = list(average["prompt_adapter"])

values = [zero_shot_clip]
values += clip_adapter
values += meta_adapter
values += tip_adapter_f
values += tip_adapter
values += prompt_adapter
val_min, val_max = min(values), max(values)
diff = val_max - val_min
val_bot = val_min - diff*0.05
val_top = val_max + diff*0.05

fig, ax = plt.subplots()
ax.set_facecolor("#EBEBEB")

ax.set_xticks([0] + shots)
ax.set_xticklabels([0] + shots)
ax.set_xlabel("Number of labeled training examples per class")
ax.set_ylabel("Score (%)")
ax.grid(axis="x", color="white", linewidth=1)
ax.axhline(zero_shot_clip, color="white", linewidth=1)
ax.set_title("Average over 6 datasets", fontweight="bold")
ax.set_ylim(val_bot, val_top)

ax.plot(
    0, zero_shot_clip,
    marker="*",
    markersize=MS*1.5,
    color=COLORS["zero_shot_clip"],
    alpha=ALPHA
)
ax.plot(
    shots, clip_adapter,
    marker="o",
    markersize=MS,
    color=COLORS["clip_adapter"],
    label="CLIP-Adapter",
    alpha=ALPHA
)
ax.plot(
    shots, meta_adapter,
    marker="o",
    markersize=MS,
    color=COLORS["meta_adapter"],
    label="Meta-Adapter",
    alpha=ALPHA
)
ax.plot(
    shots, tip_adapter_f,
    marker="o",
    markersize=MS,
    color=COLORS["tip_adapter_f"],
    label="Tip-Adapter-F",
    alpha=ALPHA
)
ax.plot(
    shots, tip_adapter,
    marker="o",
    markersize=MS,
    color=COLORS["tip_adapter"],
    label="Tip-Adapter",
    alpha=ALPHA
)
ax.plot(
    shots, prompt_adapter,
    marker="o",
    markersize=MS,
    color=COLORS["prompt_adapter"],
    label="Prompt-Adapter",
    linestyle="dotted",
    alpha=ALPHA
)

ax.text(-0.5, zero_shot_clip-diff*1e-8, "Zero-shot-CLIP", color=COLORS["zero_shot_clip"],fontsize='small')
ax.legend(loc="lower right")

fig.savefig(f"{save_dir}/average.png", bbox_inches="tight")