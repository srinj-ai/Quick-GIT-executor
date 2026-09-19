import os
import subprocess
import pandas as pd


folders_data = []


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