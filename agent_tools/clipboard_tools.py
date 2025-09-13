# Clipboard related tools
# 1. Paste content from clipboard -> paste_from_clipboard
# 2. Copy content to clipboard -> copy_to_clipboard
# 3. Get selected text by copy and paste -> get_selected_text

import time
import pyperclip
import pyautogui
from langchain.agents import tool


@tool
def paste_from_clipboard():
    """
    Get the text content from the system clipboard.
    Returns:
        str: The text content from the clipboard or an error message if the clipboard is empty.
    """
    try:
        clipboard_content = pyperclip.paste()
        if clipboard_content:
            print(f"Action Completed: Retrieved {len(clipboard_content)} characters from clipboard.")
            return clipboard_content
        print("Action Failed: Clipboard is empty.")
        return ""
    except Exception as e:
        print(f"Action Failed: Unable to access clipboard: {e}")
        return f"Error accessing clipboard: {e}"


@tool
def copy_to_clipboard(text:str):
    """
    Copying/setting the text to clipboard.
    Args:
        text (str): The text to be copied to the clipboard.
    Returns: 
        A sucess message after copying the text to clipboard.
    """
    try:
        print(f"Copying {text[:50]}... to clipboard.")
        pyperclip.copy(text)
        return f"Action Completed: Copied {len(text)} characters to clipboard."
    except Exception as e:
        print(f"Action Failed: Error setting content to clipboard. {e}")
        return f"Error setting content to clipboard. {e}"


@tool    
def get_selected_text():
    """
    Get the currently selected text on the screen.
    Returns:
        str: The currently selected text or an error message if no text is selected.
    """
    try:
        print("Getting the currently selected text on the screen.")
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)  # Wait for clipboard to update
        selected_text = pyperclip.paste()
        if selected_text:
            print(f"Action Completed: Retrieved {len(selected_text)} characters of selected text.")
            return selected_text
        else:
            print("Action Failed: No text is currently selected.")
            return ""
    except Exception as e:
        print(f"Action Failed: Error retrieving selected text. {e}")
        return f"Error retrieving selected text. {e}"
    
