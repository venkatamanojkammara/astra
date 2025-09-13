# -----------------
# GUI related tools
# -----------------
# 1. Open an application in desktop -> open_app(app_name)
# 2. Close an application in desktop -> close_app(app_name)
# 3. Close the current window -> close_window()
# 4. Open a new tab -> open_new_tab()
# 5. Close the current tab -> close_tab()
# 6. Refreshes Page -> refreshe_page()
# 7. Press Key 
# 8. Press Shortcut
# 9. Take a Screenshot
# 10. Send message 
# 11. Scrrol Page
# 12. Search text

import os
import time
import psutil
import pyautogui
import subprocess
import datetime
from langchain.agents import tool




@tool
def close_app(app_name: str):
    """
    Close an application by its name.
    Args:
        app_name (str): The name of the application (e.g., 'notepad', 'chrome', 'spotify').
    Returns:
        str: Success or error message.
    """
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] and app_name.lower() in proc.info['name'].lower():
                proc.terminate()
                print(f"Action Completed: Closed {app_name} application")
                return f"Action Completed: Closed {app_name} application"
        return f"Error: Application {app_name} not found."
    except Exception as e:
        print(f"Action Failed: Error closing the {app_name}")
        return f"Action Failed: Error closing {app_name}: {e}"

    
@tool
def close_window():
    """
    Closes the current window using Alt + F4 keys in the keyboard.
    Returns:
        Sucess message after closing the window.
    """
    try:
        pyautogui.hotkey('alt', 'f4')
        print("Action Completed: Closed the current window.")
        return "result: Closed the current window."
    except Exception as e:
        print(f"Action Failed: Error closing the window: {e}.")
        return f"Error closing the window: {e}."
    

@tool
def open_new_tab():
    """
    Opens a new tab using Ctrl + T keys from the keyboard in a browser.
    Return:
        Sucess message after opening a new tab.
    """
    try:
        pyautogui.hotkey("ctrl", "t")
        print("Action Completed: Opened a new tab.")
        return "result: Opened a new tab."
    except Exception as e:
        print(f"Action Failed: Error opening a new tab: {e}.")
        return f"Error opening a new tab: {e}."


@tool
def close_tab():
    """
    Close the current tab using Ctrl + W keys in the keyboard.
    Returns:
        Sucess message after closing the tab.
    """
    try:
        pyautogui.hotkey('ctrl', 'w')
        print("Action Completed: Closed the current tab.")
        return "result: Closed the current tab."
    except Exception as e:
        print(f"Action Failed: Error closing the tab: {e}.")
        return f"Error closing the tab: {e}."
    

@tool
def refresh_page():
    """
    Refreshes the current page using F5 key from the keyboard in a browser.
    Returns:
        Sucess message after refreshing the page.
    """
    try:
        pyautogui.press("f5")
        print("Action Completed: Refreshed the current page.")
        return "result: Refreshed the current page."
    except Exception as e:
        print(f"Action Failed: Error refreshing the page: {e}.")
        return f"Error refreshing the page: {e}."
    

@tool
def press_key(key: str):
    """
    Press a single key on the keyboard.
    Args:
        key (str): The key to be pressed.
    Returns:
        Sucess message after pressing the key.
    """
    try: 
        pyautogui.press(key)
        print(f"Action Completed: Pressed the {key} key.")
        return f"result: Pressed the {key} key."
    except Exception as e:
        print(f"Action Failed: Error pressing the key: {e}.")
        return f"Error pressing the key: {e}."
    

@tool
def press_shortcut(keys: str):
    """
    Press a combination of keys in the keyboard as a shortcut.
    Args:
        keys (str): The combination of keys to be pressed, separated by '+' 
    Example: 
        'win + r' or 'ctrl + shift + n'
    Returns:
        Sucess message after pressing the key combination.
    """
    try:
        key_list = [key.strip() for key in keys.split('+')]
        pyautogui.hotkey(*key_list)
        print(f"Action Completed: Pressed the {keys} keys.")
        return f"result: Pressed the {keys} keys."
    except Exception as e:
        print(f"Action Failed: Error pressing the {keys} keys: {e}.")
        return f"Error pressing the {keys} keys: {e}."


@tool
def take_screenshot(folder: str):
    """
    Takes a screenshot of the current screen and saves it as a PNG file in specific directory.
    Args:
        directory (str): The directory where the screenshot will be saved.
    Returns:
        sucess message after taking the screenshot and saving it to the directory.
    """
    try:
        directory = os.path.join(os.path.expanduser("~"), folder)
        os.makedirs(directory, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(directory, f"screenshot_{timestamp}.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(file_path)
        print(f"Action Completed: Screenshot saved at {file_path}.")
        return f"result: Screenshot saved at {file_path}."
    except Exception as e:
        print(f"Action failed: Error taking screenshot: {e}.")
        return f"Error taking screenshot: {e}."
    

@tool
def send_message_or_text(text: str):
    """
    Types the message/text in the active text field and sends it.
    Args:
        text (str): The message/text to be typed and sent.
    Returns: 
        Sucess message after typing and sending the text.
    """
    try:
        pyautogui.write(text, interval=0.1)
        pyautogui.press("enter")
        print(f"Action Completed: Typed and sent the text {text[:50]}...")
        return f"result: Typed and sent the text {text[:50]}..."
    except Exception as e:
        print(f"Action Failed: Error typing and sending the text: {e}.")
        return f"Error typing and sending the text: {e}."
    

@tool
def scroll_page(direction: str, amount: int):
    """
    Scrolls the page up or down by spefified amount.
    Args:
        direction (str): The direction to scroll, either 'up' or 'down'.
        amount (int): The amount to scroll. Positive values scroll up, negative values scroll down.
    Returns:
        Scuess message after scrolling the page.
    """
    try:
        if direction.lower() == 'up':
            pyautogui.scroll(amount)
            print(f"Action Completed: Scrolled up by {amount} units.")
            return f"result: Scrolled up by {amount} units."
        elif direction.lower() == 'down':
            pyautogui.scroll(-amount)
            print(f"Action Completed: Scrolled down by {amount} units.")
            return f"result: Scrolled down by {amount} units."
        else:
            return "Error scrolling the page: direction must be 'up' or 'down'."
    except Exception as e:
        print(f"Action Failed: Error scrolling the page: {e}.")
        return f"Error scrolling the page: {e}."


@tool
def search_text(text: str):
    """
    Searches for the specified text inside the applications.
    Args:
        text (str): The text to be searched.
    Returns:
        Sucess message after searching the text.
    """
    try:
        pyautogui.hotkey('ctrl', 'k')
        time.sleep(1)
        pyautogui.write(text, interval=0.2)
        time.sleep(1)
        pyautogui.press('enter')
        print(f"Action Completed: Searched for the text.")
        return f"Action Completed: Searched for the text."
    except Exception as e:
        print(f"Action Failed: Unable to search for the text: {e}.")
        return f"Action Failed: Unable to search for the text: {e}."