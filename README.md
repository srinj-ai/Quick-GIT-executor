# GitQuick (Quick-GIT-executor)

**GitQuick** is an interactive Terminal User Interface (TUI) and wrapper tool for effortlessly managing multiple Git repositories from a single terminal menu. Built with Python, `prompt_toolkit`, and `pandas`, GitQuick simplifies daily repository management and speeds up common developer workflows such as staging, committing, and pushing changes.

---

## Features

- **Interactive TUI Menu**: Easily navigate through local projects and Git actions using intuitive keyboard controls.
- **Multi-Repository Directory Scanning**: Automatically detects and lists all subdirectories under a specified root directory.
- **Quick Push Workflow**: Stage all changes, prompt for a commit message, and push to remote in a single streamlined action.
- **Comprehensive Git Support**: Executable commands include:
  - `Git Status`
  - `Git Pull`
  - `Git Push`
  - `Git Log` (graph & decorated format)
  - `Git Branch`
  - `Git Fetch`
  - `Git Add` (stages all modified and untracked files)
  - `Git Commit`
  - `Git Switch`
  - `Git Merge`
- **Automatic `.env` Parsing**: Automatically loads configuration variables such as project directory location without requiring global system environment edits.

---

## Prerequisites

- **Python**: Version 3.7 or higher
- **Git**: Installed and accessible from your system command line/terminal (`git --version`)

### Dependencies

- [`prompt_toolkit`](https://github.com/prompt-toolkit/python-prompt-toolkit): Interactive terminal UI rendering and key bindings.
- [`pandas`](https://pandas.pydata.org/): Lightweight management and CSV serialization of target folders.

---

## Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/Quick-GIT-executor.git
   cd Quick-GIT-executor
   ```

2. **Install Dependencies**

   Install required Python packages via pip:

   ```bash
   pip install pandas prompt_toolkit
   ```

3. **Configure Environment Variables**

   Create a `.env` file in the root directory (you can copy `.env.example` as a template):

   ```bash
   cp .env.example .env
   ```

   Edit `.env` to specify your root projects directory:

   ```env
   DIRECTORY = r"C:\path\to\your\projects"
   ```

---

## Usage Guide

Launch the terminal application by running:

```bash
python terminal.py
```

### Keyboard Controls

| Key | Description |
| --- | --- |
| `↑` / `↓` | Navigate through menu options |
| `ENTER` | Select current highlighted option |
| `ESC` | Go back to project selection |
| `Q` | Quit the application |

### Workflows

1. **Selecting a Project**: Upon launch, GitQuick scans the root directory specified in `.env` and renders a list of project folders. Use arrow keys to highlight a folder and press `ENTER`.
2. **Executing Actions**: Select from available Git actions. For commands requiring user input (such as `Commit`, `Quick Push`, `Switch`, or `Merge`), GitQuick will prompt for details directly in the terminal before running the operation.

---

## Project Structure

```
Quick-GIT-executor/
├── gitquick.py       # Core module wrapping subprocess Git commands & .env loader
├── terminal.py       # Interactive menu UI built using prompt_toolkit
├── .env.example      # Sample configuration file for environment variables
├── .gitignore        # Standard Git ignore rules
├── LICENSE           # MIT License file
└── README.md         # Project documentation and usage guide
```

---

## License

This project is licensed under the [MIT License](LICENSE).
