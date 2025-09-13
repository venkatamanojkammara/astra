import pyautogui
import datetime
import time
from utils import run_command, update_files_list
from langchain.agents import tool


@tool
def get_current_datetime():
    """
    Get the current date and time in a human-readable format.
    Returns:
        str: The current date and time as a formatted string.
    """
    print("Action: Getting the current date and time.")
    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"Action Completed: Current date and time is {date_time}.")
    return f"result: Current date and time is {date_time}."


@tool
def open_application(app_name: str):
    """
    Opens an application by using its name. 
    Args:
        app_name (str): The application name to be opened.
    Returns:
        Sucess message after opening the application.
    """
    try:
        print(f"Trying to open the {app_name} application...")
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.write(app_name, interval=0.2)
        time.sleep(2)
        pyautogui.press('enter')
        print(f"Action Completed: Opened the {app_name} application.")
        return f"Result: Opened the {app_name} application."
    except Exception as e:
        print(f"Action Failed: Error opening the {app_name} application: {e}.")
        return f"Error opening the {app_name} application: {e}."
    

@tool
def open_file(file_path: str):
    """
    Opens a file using the default application associated with its file type.
    Args:
        file_path: The path to the file to open.
    Returns:
        A success message or an error message.
    """
    try:
        print(f"Action: Opening file: '{file_path}'")
        update_files_list()
        run_command(f"start \"\" \"{file_path}\"")
        return {"result": f"Successfully opened file: {file_path}"}
    except Exception as e:
        print(f"Error opening file '{file_path}': {e}")
        return {"error": f"Error opening file '{file_path}': {e}"}


@tool
def open_folder(folder_path: str):
    """
    Opens a folder using the file explorer.
    Args:
        folder_path (str): The path of the folder to be opened.
    Returns:
        Sucess message after opening the folder.
    """
    try:
        print(f"Trying to open {folder_path}...")
        run_command(f"start \"\" \"{folder_path}\"")
        print(f"Action Completed: Opened the {folder_path}.")
        return f"Result: Opened the {folder_path}."
    except Exception as e:
        print(f"Action Failed: Error opening the {folder_path}: {e}.")
        return f"Error opening the {folder_path}: {e}."



def execute_command(command: str) -> dict:
    """
    Perform OS related tasks by running a command.
    Use bash commands for this.
    Technical Constraints:
    *   Shell: Target `bash` on Linux.
    *   File/Directory Names: Assume names may contain SPACES. Use proper quoting (e.g., double quotes `""`) to handle them correctly.
    *   Wildcards: Use wildcards outside quotes for file matching (globbing), e.g., `rm *.tmp`, `mv "target dir/"?.txt ./`. Avoid constructs like `rm "*.tmp"`.
    Args:
        command(str): the command to execute
    """
    if "*" in command:
        command = command.replace("*", '"*"')
    output = run_command(command)
    print(command, output)
    return {"output": output.get("output"), "error": output.get("error")}