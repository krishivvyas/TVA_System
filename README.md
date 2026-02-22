# 🕰️ TVA (Timeline Variance Authority) CLI

> *"For all time. Always."*

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) ![Git](https://img.shields.io/badge/Git-Wrapper-F05032.svg) ![Typer](https://img.shields.io/badge/CLI-Typer-009688.svg)

## 📁 OVERVIEW: FILE TVA-770

The **TVA CLI** is a highly aggressive, lore-accurate Git wrapper designed to protect the **Sacred Timeline** (`main` branch). 

Inspired by Marvel's *Loki*, this tool enforces **Trunk-Based Development** and Continuous Integration by punishing developers who keep feature branches alive for too long. If you step off the Sacred Timeline and fail to merge your "Variant" branch within the allotted time limit (default: 30 minutes), the TVA will deploy a reset charge and banish your branch to **The Void**.

## ✨ THE PROTOCOLS (Features)

* **Variant Tracking:** Automatically logs the exact temporal coordinate (timestamp) when you create a new branch.
* **The Pruning Protocol:** Scans the repository for branches that have exceeded their permitted lifespan. Expired branches are forcibly checked out, detached from the Sacred Timeline, and renamed to the `void/` namespace.
* **The TemPad:** A specialized command to view branches that have been consumed by Alioth in The Void.
* **Immersive UI:** Built with `rich` to replicate the brutalist, retro-futuristic orange terminal aesthetic of the TVA computers.
* **Classified Anomalies:** Hidden Easter eggs and triggers based on specific branch names.

---

## 🛠️ INSTALLATION & SETUP

### 1. The Temporal Aura (Environment)
It is highly recommended to isolate the TVA systems using Conda or venv.
```bash
conda create --name tva python=3.10 -y
conda activate tva

```

### 2. Install Dependencies

```bash
pip install typer rich gitpython

```

### 3. Configure the TemPad (Alias)

To use the TVA globally across your repositories, you must map the command.

**For Mac / Linux (add to `~/.bashrc` or `~/.zshrc`):**

```bash
alias tva="python3 /path/to/your/TVA_System/tva.py"

```

**For Windows PowerShell (add to your `$PROFILE`):**

```powershell
function tva { python "C:\path\to\your\TVA_System\tva.py" $args }

```

---

## 📜 STANDARD OPERATING PROCEDURE (Usage)

Ensure you are inside a valid Git repository before executing TVA commands.

### 1. Stepping off the Sacred Timeline

Create a new feature branch. This starts the countdown.

```bash
tva variant feature-login

```

*(Warning: The Time-Keepers are now monitoring this branch.)*

### 2. Enforcing the Timeline

Run the pruning sweep. If your branch is older than 30 minutes, it will be banished. (Can be automated via cron jobs).

```bash
tva prune

```

### 3. Accessing The Void

If your branch was pruned, it is not permanently deleted. It has been renamed to `void/branch-name_timestamp`. View the void with:

```bash
tva tempad

```

---

## 🚨 CLASSIFIED: KNOWN ANOMALIES (Easter Eggs)

The system contains undocumented triggers. Enter at your own risk.

* `tva variant mobius`
* `tva variant sylvie`
* `tva variant kang`
* `tva alligator`
* `tva miss-minutes`

---

## ⚠️ DISCLAIMER

*This tool is a novelty wrapper for Git, but its file operations are real. The default configuration renames branches rather than performing hard deletions (`git branch -D`), but the TVA assumes no liability for lost work, temporal paradoxes, or encounters with Alioth. Always push your code.*

```

Would you like to move on to building the automated cron job/background task to make the pruning run on its own?

```