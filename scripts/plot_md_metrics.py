import sys
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def parse_xvg(filepath: Path) -> tuple[np.ndarray, np.ndarray]:
    x_vals, y_vals = [], []
    with filepath.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith(("#", "@")):
                continue
            parts = line.split()
            if len(parts) >= 2:
                x_vals.append(float(parts[0]))
                y_vals.append(float(parts[1]))
    return np.array(x_vals), np.array(y_vals)


def plot_rmsd(xvg_path: Path, out_png: Path) -> None:
    time_ns, rmsd_nm = parse_xvg(xvg_path)
    plt.figure(figsize=(8, 4.5), dpi=300)
    plt.plot(time_ns, rmsd_nm, linewidth=1.5)
    plt.xlabel("Time (ns)")
    plt.ylabel("Backbone RMSD (nm)")
    plt.title("pVHL Complex Backbone RMSD")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()


def plot_rmsf(xvg_path: Path, out_png: Path) -> None:
    residue, rmsf_nm = parse_xvg(xvg_path)
    plt.figure(figsize=(9, 4.5), dpi=300)
    plt.plot(residue, rmsf_nm, linewidth=1.5)
    plt.xlabel("Residue Index")
    plt.ylabel("C-alpha RMSF (nm)")
    plt.title("Per-Residue Flexibility (C-alpha RMSF)")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()


if __name__ == "__main__":
    base_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    rmsd_file = base_dir / "rmsd_backbone.xvg"
    rmsf_file = base_dir / "rmsf_ca.xvg"

    if rmsd_file.exists():
        plot_rmsd(rmsd_file, base_dir / "rmsd_backbone.png")
    if rmsf_file.exists():
        plot_rmsf(rmsf_file, base_dir / "rmsf_ca.png")
