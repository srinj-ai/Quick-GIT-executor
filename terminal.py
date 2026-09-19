import os
import pandas as pd
import gitquick as git

from prompt_toolkit import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.key_binding import KeyBindings


# ============================================================
# CONFIG
# ============================================================

git.load_environment()

target_directory = os.getenv("DIRECTORY")

if not target_directory:
    raise RuntimeError(
        "DIRECTORY is not set.\n"
        "Add DIRECTORY=r'C:\\path\\to\\projects' to your .env file."
    )


# ============================================================
# STYLES
# ============================================================

CYAN = "bold cyan"
WHITE = "bold white"
GRAY = "ansibrightblack"
GREEN = "bold green"
YELLOW = "bold yellow"
RED = "bold red"
BLUE = "bold blue"
MAGENTA = "bold magenta"

# IMPORTANT:
# prompt_toolkit uses "bg:cyan", NOT "bg=cyan"
SELECTED = "bold black bg:cyan"


# ============================================================
# MENU
# ============================================================

def menu(options, title, subtitle=None):

    selected = 0

    def get_text():

        lines = []

        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        lines.append(
            (CYAN,
             "╭──────────────────────────────────────────────────────────╮\n")
        )

        lines.append(
            (CYAN, "│")
        )

        lines.append(
            (WHITE, "                        GITQUICK")
        )

        lines.append(
            (CYAN, "                         │\n")
        )

        lines.append(
            (CYAN, "│")
        )

        lines.append(
            (GRAY, "                  Terminal Git Manager")
        )

        lines.append(
            (CYAN, "                    │\n")
        )

        lines.append(
            (CYAN,
             "╰──────────────────────────────────────────────────────────╯\n\n")
        )


        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        lines.append(
            (WHITE, f"  {title}\n")
        )

        if subtitle:
            lines.append(
                (GRAY, f"  {subtitle}\n")
            )

        lines.append(
            (
                GRAY,
                "  ────────────────────────────────────────────────────────\n\n"
            )
        )


        # ----------------------------------------------------
        # OPTIONS
        # ----------------------------------------------------

        for index, option in enumerate(options):

            name = option[0]

            if index == selected:

                lines.append(
                    (
                        SELECTED,
                        f"  >  {name}  \n"  # ❯
                    )
                )

            else:

                lines.append(
                    (
                        WHITE,
                        f"     {name}\n"
                    )
                )


        # ----------------------------------------------------
        # FOOTER
        # ----------------------------------------------------

        lines.append(
            (
                GRAY,
                "\n  ────────────────────────────────────────────────────────\n"
            )
        )

        lines.append(
            (
                GRAY,
                "  ↑ ↓  Navigate     ENTER  Select     Q  Quit\n"
            )
        )

        return lines


    # --------------------------------------------------------
    # UI
    # --------------------------------------------------------

    control = FormattedTextControl(
        get_text
    )

    window = Window(
        content=control,
        always_hide_cursor=True
    )

    layout = Layout(window)


    # --------------------------------------------------------
    # KEYBOARD
    # --------------------------------------------------------

    bindings = KeyBindings()


    @bindings.add("up")
    def move_up(event):

        nonlocal selected

        selected = (
            selected - 1
        ) % len(options)

        event.app.invalidate()


    @bindings.add("down")
    def move_down(event):

        nonlocal selected

        selected = (
            selected + 1
        ) % len(options)

        event.app.invalidate()


    @bindings.add("enter")
    def select(event):

        event.app.exit(
            result=options[selected][1]
        )


    @bindings.add("q")
    def quit_menu(event):

        event.app.exit(
            result="exit"
        )


    @bindings.add("escape")
    def escape(event):

        event.app.exit(
            result="back"
        )


    # --------------------------------------------------------
    # APPLICATION
    # --------------------------------------------------------

    app = Application(
        layout=layout,
        key_bindings=bindings,
        full_screen=True,
        mouse_support=False
    )

    return app.run()


# ============================================================
# LOAD PROJECTS
# ============================================================

git.get_folder(target_directory)

df = pd.read_csv(
    "folders_with_path.csv"
)

project_options = []

for _, row in df.iterrows():

    folder_name = row["Folder_Name"]

    project_path = os.path.join(
        target_directory,
        folder_name
    )

    project_options.append(
        (
            f"●  {folder_name}",
            project_path
        )
    )


# ============================================================
# MAIN LOOP
# ============================================================

while True:

    selected_project = menu(
        project_options + [
            ("●  Exit", "exit")
        ],
        "SELECT PROJECT",
        "Choose a repository to manage"
    )


    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if selected_project == "exit":
        break


    project_directory = selected_project

    project_name = os.path.basename(
        os.path.normpath(
            project_directory
        )
    )


    # ========================================================
    # GIT COMMAND MENU
    # ========================================================

    while True:

        command_options = [

            ("●  Quick Push", "quick_push"),

            ("●  Git Status", "status"),

            ("●  Git Pull", "pull"),

            ("●  Git Push", "push"),

            ("●  Git Log", "log"),

            ("●  Git Branch", "branch"),

            ("●  Git Fetch", "fetch"),

            ("●  Git Add", "add"),

            ("●  Git Commit", "commit"),

            ("●  Git Switch", "switch"),

            ("●  Git Merge", "merge"),

            ("●  Back to Projects", "back"),

            ("●  Exit", "exit")
        ]


        command = menu(
            command_options,
            "GIT COMMANDS",
            f"●  {project_name}"
        )


        # ====================================================
        # STATUS
        # ====================================================

        if command == "status":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  Git Status\n")

            git.git_status(
                project_directory
            )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # PULL
        # ====================================================

        elif command == "pull":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  Git Pull\n")

            git.git_pull(
                project_directory
            )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # PUSH
        # ====================================================

        elif command == "push":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  Git Push\n")

            git.git_push(
                project_directory
            )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # LOG
        # ====================================================

        elif command == "log":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  Git Log\n")

            git.git_log(
                project_directory
            )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # BRANCH
        # ====================================================

        elif command == "branch":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  Git Branch\n")

            git.git_branch(
                project_directory
            )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # FETCH
        # ====================================================

        elif command == "fetch":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  Git Fetch\n")

            git.git_fetch(
                project_directory
            )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # ADD
        # ====================================================

        elif command == "add":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  Git Add\n")

            git.git_add(
                project_directory
            )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # COMMIT
        # ====================================================

        elif command == "commit":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  Git Commit\n")

            msg = input(
                "Commit message: "
            ).strip()

            if msg:

                git.git_commit(
                    project_directory,
                    msg
                )

            else:

                print(
                    "\nCommit cancelled."
                )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # QUICK PUSH
        # ====================================================

        elif command == "quick_push":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  QUICK PUSH")
            print("   ● Add → Commit → Push\n")

            msg = input(
                "Commit message: "
            ).strip()

            if msg:

                git.git_quick_push(
                    project_directory,
                    msg
                )

            else:

                print(
                    "\nQuick Push cancelled."
                )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # SWITCH
        # ====================================================

        elif command == "switch":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  Git Switch\n")

            branch_name = input(
                "Branch name: "
            ).strip()

            if branch_name:

                git.git_switch(
                    project_directory,
                    branch_name
                )

            else:

                print(
                    "\nSwitch cancelled."
                )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # MERGE
        # ====================================================

        elif command == "merge":

            os.system("cls")

            print(f"●  {project_name}\n")
            print("●  Git Merge\n")

            branch_name = input(
                "Branch to merge: "
            ).strip()

            if branch_name:

                git.git_merge(
                    project_directory,
                    branch_name
                )

            else:

                print(
                    "\nMerge cancelled."
                )

            input(
                "\nPress Enter to continue..."
            )


        # ====================================================
        # BACK
        # ====================================================

        elif command == "back":

            break


        # ====================================================
        # EXIT
        # ====================================================

        elif command == "exit":

            raise SystemExit


# ============================================================
# EXIT SCREEN
# ============================================================

os.system("cls")

print()
print("╭──────────────────────────────────────────────╮")
print("│                                              │")
print("│              ⚡ GITQUICK                     │")
print("│                                              │")
print("│          Git Manager closed.                 │")
print("│                                              │")
print("╰──────────────────────────────────────────────╯")
print()