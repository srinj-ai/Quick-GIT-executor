import os
import subprocess
import pandas as pd


folders_data = []


def load_environment(env_file=None):
    """Load environment variables from a .env file if present."""
    if env_file is None:
        env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")

    if not os.path.isfile(env_file):
        return False

    with open(env_file, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = [part.strip() for part in line.split("=", 1)]
            value = value.strip()

            if value and value[0] in ('"', "'") and value[-1] == value[0]:
                value = value[1:-1]
            elif value.startswith("r") and len(value) >= 3 and value[1] in ('"', "'") and value[-1] == value[1]:
                value = value[2:-1]

            os.environ.setdefault(key, value)

    return True


# ---------- RUN GIT COMMAND ----------

def run_git(target_directory, command):

    print(f"\n> git {' '.join(command)}\n")

    result = subprocess.run(
        ["git", "--no-pager"] + command,
        cwd=target_directory,
        text=True
    )

    return result.returncode


# ---------- PROJECTS ----------

def get_folder(target_directory):
    if not target_directory:
        raise ValueError(
            "DIRECTORY is not set. Add DIRECTORY = r'C:\\path\\to\\projects' to .env or set it in the shell."
        )

    folders_data.clear()

    for item in os.listdir(target_directory):
        full_path = os.path.join(target_directory, item)

        if os.path.isdir(full_path):
            folders_data.append({
                "Folder_Name": item,
                "path": f"/{item}"
            })

    df = pd.DataFrame(folders_data)
    df.to_csv("folders_with_path.csv", index=False)


# ---------- GIT COMMANDS ----------

def git_status(target_directory):
    run_git(target_directory, ["-c", "color.ui=always", "status"])


def git_pull(target_directory):
    run_git(target_directory, ["-c", "color.ui=always", "pull"])


def git_push(target_directory):
    run_git(target_directory, ["-c", "color.ui=always", "push"])


def git_log(target_directory):
    run_git(
        target_directory,
        [
            "-c", "color.ui=always",
            "log",
            "--oneline",
            "--graph",
            "--decorate"
        ]
    )


def git_branch(target_directory):
    run_git(
        target_directory,
        ["-c", "color.ui=always", "branch"]
    )


def git_fetch(target_directory):
    run_git(target_directory, ["fetch"])


def git_add(target_directory):
    run_git(target_directory, ["add", "-A"])


def git_commit(target_directory, msg):
    run_git(
        target_directory,
        ["commit", "-m", msg]
    )


def git_quick_push(target_directory, msg):

    print("\nAdding files...")
    run_git(
        target_directory,
        ["add", "-A"]
    )

    print("\nCommitting...")
    run_git(
        target_directory,
        ["commit", "-m", msg]
    )

    print("\nPushing...")
    run_git(
        target_directory,
        ["push"]
    )


def git_switch(target_directory, branch_name):

    run_git(
        target_directory,
        ["switch", branch_name]
    )


def git_merge(target_directory, branch_name):

    run_git(
        target_directory,
        ["merge", branch_name]
    )