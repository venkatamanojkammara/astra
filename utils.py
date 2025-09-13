import pyautogui
import subprocess
import pyperclip
from langchain.agents import tool
import os
from typing import Dict


@tool
def write_code(code: str):
    """
    Write the given code in the current active window.
    Args:
        code (str): The code to be written.
    Returns:
        Sucess message after writing the code.
    """
    try:
        print(f"Trying to write the code...")
        pyautogui.hotkey('ctrl', 'home')
        for line in code.split('\n'):
            pyperclip.copy(line)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
        print(f"Action Completed: Written the code.")
        return f"Result: Written the code."
    except Exception as e:
        print(f"Action Failed: Error writing the code: {e}.")
        return f"Error writing the code: {e}."
    

@tool
def write_text(text: str):
    """
    Write the given text in the current active window.
    Args:
        text (str): The text to be written.
    Returns:
        Sucess message after writing the text.
    """
    try:
        print(f"Trying to write the text {text[:50]}...")
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')
        print(f"Action Completed: {text[:50]}... was written.")
        return f"Result: {text[:50]}... was written."
    except Exception as e:
        print(f"Action Failed: Error writing the text: {e}.")
        return f"Error writing the text: {e}."



def update_files_list():
    # Generate a simple file list for common user folders on Windows
    user_home = os.path.expanduser("~")
    roots = [
        os.path.join(user_home, "Desktop"),
        os.path.join(user_home, "Downloads"),
        os.path.join(user_home, "Documents"),
        os.path.join(user_home, "Videos"),
        os.path.join(user_home, "Pictures"),
        os.path.join(user_home, "Music"),
    ]
    entries = []
    for root in roots:
        if not os.path.isdir(root):
            continue
        for dirpath, _, filenames in os.walk(root):
            if any(part in {".git", ".vscode", "__pycache__", "node_modules", "venv", ".venv"} for part in dirpath.split(os.sep)):
                continue
            for fn in filenames:
                entries.append(os.path.join(dirpath, fn))
    with open("files.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(entries))
    


def get_files_list():
    update_files_list()
    with open("files.txt", "r", encoding="utf-8") as f:
        return f.read()



def run_command(command: str) -> Dict[str, str]:
    """Run a shell command on Windows, preferring Git Bash if available, otherwise PowerShell."""
    try:
        bash_path = r"C:\Program Files\Git\bin\bash.exe"
        if os.path.exists(bash_path):
            proc = subprocess.run([bash_path, "-lc", command], capture_output=True, text=True, timeout=30)
        else:
            # Fallback to PowerShell
            proc = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", command], capture_output=True, text=True, timeout=30)
        return {"output": proc.stdout, "error": proc.stderr}
    except subprocess.TimeoutExpired:
        return {"output": "", "error": "Command timed out."}
    except Exception as e:
        return {"output": "", "error": str(e)}
