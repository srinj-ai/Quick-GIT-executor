import os
import pandas as pd
import gitquick as git

from prompt_toolkit import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.key_binding import KeyBindings


target_directory = os.getenv("DIRECTORY")


def menu(options, title):
    selected = 0

    def get_text():
        lines = [
            (f"bold cyan", f"===== {title} =====\n\n")
        ]

        for i, option in enumerate(options):
            if i == selected:
                lines.append(
                    ("bold green", f"  > {option[0]}\n")
                )
            else:
                lines.append(
                    ("", f"    {option[0]}\n")
                )

        return lines

    control = FormattedTextControl(get_text)
    window = Window(content=control)

    kb = KeyBindings()

    @kb.add("up")
    def _(event):
        nonlocal selected
        selected = (selected - 1) % len(options)

    @kb.add("down")
    def _(event):
        nonlocal selected
        selected = (selected + 1) % len(options)

    @kb.add("enter")
    def _(event):
        event.app.exit(result=options[selected][1])

    @kb.add("q")
    def _(event):
        event.app.exit(result="exit")

    app = Application(
        layout=Layout(window),
        key_bindings=kb,
        full_screen=True,
        mouse_support=False
    )

    return app.run()


# Generate project list
git.get_folder(target_directory)

df = pd.read_csv("folders_with_path.csv")

project_options = []

for _, row in df.iterrows():
    folder_name = row["Folder_Name"]

    project_path = os.path.join(
        target_directory,
        folder_name
    )

    project_options.append(
        (folder_name, project_path)
    )


# =========================
# MAIN LOOP
# =========================

while True:

    selected_project = menu(
        project_options + [
            ("Exit", "exit")
        ],
        "SELECT PROJECT"
    )

    if selected_project == "exit":
        break

    project_directory = selected_project


    # =========================
    # GIT MENU
    # =========================

    while True:

        command_options = [
            ("Git Status", "status"),
            ("Git Pull", "pull"),
            ("Git Push", "push"),
            ("Git Log", "log"),
            ("Git Branch", "branch"),
            ("Git Fetch", "fetch"),
            ("Git Add", "add"),
            ("Git Commit", "commit"),
            ("Quick Push", "quick_push"),
            ("Git Switch", "switch"),
            ("Git Merge", "merge"),
            ("Back to Projects", "back"),
            ("Exit", "exit")
        ]

        command = menu(
            command_options,
            "GIT COMMANDS"
        )


        # =========================
        # GIT COMMANDS
        # =========================

        if command == "status":

            os.system("cls")

            git.git_status(project_directory)

            input("\nPress Enter to continue...")


        elif command == "pull":

            os.system("cls")

            git.git_pull(project_directory)

            input("\nPress Enter to continue...")


        elif command == "push":

            os.system("cls")

            git.git_push(project_directory)

            input("\nPress Enter to continue...")


        elif command == "log":

            os.system("cls")

            git.git_log(project_directory)

            input("\nPress Enter to continue...")


        elif command == "branch":

            os.system("cls")

            git.git_branch(project_directory)

            input("\nPress Enter to continue...")


        elif command == "fetch":

            os.system("cls")

            git.git_fetch(project_directory)

            input("\nPress Enter to continue...")


        elif command == "add":

            os.system("cls")

            git.git_add(project_directory)

            input("\nPress Enter to continue...")


        elif command == "commit":

            os.system("cls")

            msg = input("Enter commit message: ")

            git.git_commit(
                project_directory,
                msg
            )

            input("\nPress Enter to continue...")


        elif command == "quick_push":

            os.system("cls")

            msg = input("Enter commit message: ")

            git.git_quick_push(
                project_directory,
                msg
            )

            input("\nPress Enter to continue...")


        elif command == "switch":

            os.system("cls")

            branch_name = input(
                "Enter branch name: "
            )

            git.git_switch(
                project_directory,
                branch_name
            )

            input("\nPress Enter to continue...")


        elif command == "merge":

            os.system("cls")

            branch_name = input(
                "Enter branch to merge: "
            )

            git.git_merge(
                project_directory,
                branch_name
            )

            input("\nPress Enter to continue...")


        elif command == "back":

            break


        elif command == "exit":

            raise SystemExit


os.system("cls")

print("Git Manager closed.")