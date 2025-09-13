from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from langchain_tools.web_model import get_xpath
from urllib.parse import urljoin
import pyautogui as pg
from time import sleep
from langchain.agents import tool


driver = None
last_clicked_xpath = None

key_map = {
    'enter': Keys.ENTER, 'tab': Keys.TAB, 'backspace': Keys.BACKSPACE,
    'space': Keys.SPACE, 'shift': Keys.SHIFT, 'ctrl': Keys.CONTROL,
    'alt': Keys.ALT, 'esc': Keys.ESCAPE, 'up': Keys.ARROW_UP, 
    'down': Keys.ARROW_DOWN, 'left': Keys.ARROW_LEFT, 'right': Keys.ARROW_RIGHT,
    'delete': Keys.DELETE, 'home': Keys.HOME, 'end': Keys.END,
    'pageup': Keys.PAGE_UP, 'pagedown': Keys.PAGE_DOWN, 'insert': Keys.INSERT,
    'f1': Keys.F1, 'f2': Keys.F2, 'f3': Keys.F3, 'f4': Keys.F4,
    'f5': Keys.F5, 'f6': Keys.F6, 'f7': Keys.F7, 'f8': Keys.F8,
    'f9': Keys.F9, 'f10': Keys.F10, 'f11': Keys.F11, 'f12': Keys.F12,
    'command': Keys.COMMAND, 'meta': Keys.META, 
    'semicolon': Keys.SEMICOLON, 'equals': Keys.EQUALS,
    'numpad0': Keys.NUMPAD0, 'numpad1': Keys.NUMPAD1, 'numpad2': Keys.NUMPAD2,
    'numpad3': Keys.NUMPAD3, 'numpad4': Keys.NUMPAD4, 'numpad5': Keys.NUMPAD5,
    'numpad6': Keys.NUMPAD6, 'numpad7': Keys.NUMPAD7, 'numpad8': Keys.NUMPAD8,
    'numpad9': Keys.NUMPAD9, 'multiply': Keys.MULTIPLY, 'add': Keys.ADD,
    'separator': Keys.SEPARATOR, 'subtract': Keys.SUBTRACT, 'decimal': Keys.DECIMAL,
    'divide': Keys.DIVIDE, 'clear': Keys.CLEAR,
    'help': Keys.HELP, 'pause': Keys.PAUSE, 
    
    }


@tool
def launch_browser():
    """
    Starts a new Chrome browser session using Selenium WebDriver if one is not already running.
    This function must be called before any other browser interaction functions.
    It maximizes the browser window upon launch. Subsequent calls do nothing if a browser is active.

    Returns:
        dict: A dictionary confirming the browser is launched or already running.
    """
    global driver
    if driver is None:
        print("INFO: Launching new Chrome browser...")
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        try:
            driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()), options=options)
            print("INFO: Browser launched successfully.")
            return {"result": "Browser launched successfully."}
        except Exception as e:
            print(f"ERROR: Failed to launch browser: {e}")
            return {"error": f"Failed to launch browser: {e}"}
    else:
        print("INFO: Browser already running.")
        return {"result": "Browser already running."}
    

@tool
def navigate_current_tab(url: str) -> dict:
    """
    Navigates the currently active browser tab to the specified web address (URL).
    Requires the browser to be launched first via 'launch_browser'.
    The URL must be a complete web address, including 'http://' or 'https://'.
    Args:
        url (str): The full URL to load in the current tab.
    Returns:
        dict: A dictionary confirming navigation or reporting an error.
    """
    global driver
    if driver is None:
        return {"error": "Browser not launched. Call 'launch_browser' first."}
    try:
        print(f"INFO: Navigating current tab to: {url}")
        driver.get(url)
        print(f"INFO: Navigation complete for {url}")
        return {"result": f"Successfully navigated to {url}"}
    except Exception as e:
        print(f"ERROR: Failed to navigate to {url}: {e}")
        return {"error": f"Failed to navigate to {url}: {e}"}


@tool
def open_url_in_new_tab(url: str) -> dict:
    """
    Opens a new browser tab, automatically switches focus to this new tab,
    and then navigates it to the specified URL.
    Requires the browser to be launched first. The URL must be complete.
    The URL must be a complete web address, including 'http://' or 'https://'.

    Args:
        url (str): The full URL to open in the new tab.

    Returns:
        dict: A dictionary confirming the action or reporting an error.
    """
    global driver
    if driver is None:
        return {"error": "Browser not launched. Call 'launch_browser' first."}
    try:
        print(f"INFO: Opening URL in new tab: {url}")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(url)
        print(f"INFO: Opened and navigated new tab to: {url}")
        return {"result": f"Opened new tab and navigated to {url}"}
    except Exception as e:
        print(f"ERROR: Failed to open URL in new tab: {e}")
        return {"error": f"Failed to open URL in new tab: {e}"}
    

@tool
def switch_to_tab(index: int) -> dict:
    """
    Changes the browser's active focus to a specific tab, identified by its position.
    Tabs are indexed starting from 1 (the leftmost tab is 1, the next is 2, etc.).
    Use this before actions like clicking or typing if you need to target a non-active tab.
    Requires the browser to be launched.

    Args:
        index (int): The 1-based index of the target browser tab.

    Returns:
        dict: A dictionary confirming the switch or reporting an error.
    """
    global driver
    if driver is None:
        return {"error": "Browser not launched. Call 'launch_browser' first."}
    try:
        tab_index = index - 1 # Convert 1-based to 0-based for list access
        if 0 <= tab_index < len(driver.window_handles):
            driver.switch_to.window(driver.window_handles[tab_index])
            print(f"INFO: Switched focus to tab {index}: {driver.current_url}")
            return {"result": f"Switched to tab {index}"}
        else:
            print(f"ERROR: Invalid tab index: {index}. Available tabs: {len(driver.window_handles)}")
            return {"error": f"Invalid tab index: {index}. Only {len(driver.window_handles)} tabs available."}
    except Exception as e:
        print(f"ERROR: Failed to switch tabs: {e}")
        return {"error": f"Failed to switch tabs: {e}"}


@tool
def close_current_tab() -> dict:
    """
    Closes the browser tab that is currently active.
    If other tabs remain open, focus automatically shifts to the last tab in the list.
    If it's the last tab, this might close the browser (behavior depends on browser/OS).
    Requires the browser to be launched.

    Returns:
        dict: A dictionary confirming the tab closure.
    """
    global driver
    if driver is None:
        return {"error": "Browser not launched. Call 'launch_browser' first."}
    try:
        print("INFO: Closing current tab...")
        current_handles = len(driver.window_handles)
        driver.close()
        sleep(0.5)
        if len(driver.window_handles) < current_handles:
             if driver.window_handles:
                 driver.switch_to.window(driver.window_handles[-1])
                 print(f"INFO: Closed tab. Switched focus to last tab: {driver.current_url}")
             else:
                 print("INFO: Closed the last tab. Browser might be closed now.")
             return {"result": "Current tab closed successfully."}
        else:
             print("WARN: Tab close command issued, but tab count didn't decrease.")
             return {"result": "Attempted to close tab, but it might still be open."}

    except Exception as e:
        if "NoSuchWindowException" in str(type(e)):
             print("INFO: Current tab/window already closed.")
             if driver.window_handles:
                 driver.switch_to.window(driver.window_handles[-1])
                 print(f"INFO: Switched focus to last tab: {driver.current_url}")
                 return {"result": "Current tab was already closed. Focus moved."}
             else:
                 print("INFO: Browser already closed.")
                 return {"result": "Browser was already closed."}
        else:
            print(f"ERROR: Failed to close tab: {e}")
            return {"error": f"Failed to close tab: {e}"}


@tool
def perform_web_search(search_query: str) -> dict:
    """
    Attempts a web search using OS-level keyboard simulation (PyAutoGUI).
    It simulates pressing 'Ctrl+K' (common browser shortcut for address/search bar),
    types the query, and presses 'Enter'.
    Requires the browser window to be potentially active/focused on the OS level.

    Args:
        search_query (str): The text to search for on the web.

    Returns:
        dict: A dictionary confirming the action or reporting an error.
    """
    global driver
    if driver is None:
        return {"error": "Browser not launched. Call 'launch_browser' first."}
    try:
        print(f"INFO: Performing OS-level web search for: '{search_query}'")
        sleep(1) 
        pg.hotkey("ctrl", "k") 
        sleep(0.5)
        pg.write(search_query, interval=0.05) 
        sleep(0.5)
        pg.press("enter")
        print(f"INFO: OS-level search initiated for '{search_query}'")
        return {"result": f"OS-level search initiated for '{search_query}'."}
    except Exception as e:
        print(f"ERROR: Failed to perform OS-level web search: {e}")
        return {"error": f"Failed to perform OS-level web search: {e}"}


@tool
def type_text_into_element(text: str) -> dict:
    """
    Types the given text into the HTML input element that was most recently targeted
    by a successful 'click_element_by_description' call.
    **Crucially, this function depends on 'click_element_by_description' being called
    immediately prior on an input field or textarea.** It first clears the target field.
    Requires the browser to be launched.

    Args:
        text (str): The text content to type into the previously focused input field.

    Returns:
        dict: A dictionary confirming the typing action or reporting an error.
    """
    global driver, last_clicked_xpath
    if driver is None:
        return {"error": "Browser not launched. Call 'launch_browser' first."}
    if last_clicked_xpath is None:
        return {"error": "No element recently targeted by 'click_element_by_description'. Cannot type."}

    try:
        print(f"INFO: Attempting to type '{text}' into element: {last_clicked_xpath}")
        element = driver.find_element("xpath", last_clicked_xpath)

        if element.tag_name.lower() not in ['input', 'textarea']:
             print(f"WARN: Element {last_clicked_xpath} is not an input or textarea ({element.tag_name}). Typing might fail.")

        element.clear()
        sleep(0.2) 
       
        element.send_keys(text)
        print(f"INFO: Successfully typed '{text}' into element: {last_clicked_xpath}")
        return {"result": f"Successfully typed '{text}'."}
    except Exception as e:
        print(f"ERROR: Failed to type into element {last_clicked_xpath}: {e}")
        return {"error": f"Failed to type into element {last_clicked_xpath}: {e}"}


@tool
def click_element_by_description(description: str) -> dict:
    """
    Finds an interactive element (button, link, input field, etc.) on the current webpage
    based on a natural language description provided by the user. It uses an external helper
    function (`get_xpath`) which analyzes the page's HTML (specifically the <body> content)
    to determine the most likely XPath for the described element.

    **Behavior:**
    1. Retrieves the current page's HTML body.
    2. Calls `get_xpath` with the HTML and the `description`.
    3. If `get_xpath` returns a valid XPath:
        a. **Stores this XPath globally** for potential use by `type_text_into_element`.
        b. Checks if the XPath identifies a link (`<a>` tag with an `href` attribute).
        c. **If it's a link:** It extracts the URL (`href`). If the URL is relative (starts with '/'), it converts it to an absolute URL based on the current page's address. Then, it **navigates the current tab** to this URL using the `navigate_current_tab` function's logic.
        d. **If it's not a link:** It finds the element using the XPath and performs a standard Selenium click action on it.
    4. If `get_xpath` fails or returns an invalid XPath, an error is reported.

    **Use this function to:** Interact with elements when you can describe them (e.g., "click the 'Submit' button", "find the search input field", "click the link named 'Privacy Policy'").

    **Important:** The success depends heavily on the quality of the `description` and the ability of the external `get_xpath` function to correctly identify the element on the current page structure. The found element's XPath is saved, overwriting any previously saved XPath.

    Args:
        description (str): A natural language phrase describing the element to click.
                           Examples: 'the login button', 'search input field',
                           'the link with text Read More', 'the checkbox for newsletter'.

    Returns:
        dict: A dictionary confirming the click/navigation action or reporting an error.
    """
    print(description)
    global driver, last_clicked_xpath
    if driver is None:
        return {"error": "Browser not launched. Call 'launch_browser' first."}

    try:
        print(f"INFO: Attempting to find element described as: '{description}'")
        try:
            body_element = driver.find_element("tag name", "body")
            current_html = body_element.get_attribute("outerHTML")
        except Exception as e:
            print(f"ERROR: Could not get page HTML: {e}")
            return {"error": f"Could not get page HTML: {e}"}

        try:
            xpath_response = get_xpath(current_html, description)
            if "xpath" not in xpath_response or not xpath_response["xpath"]:
                 print(f"ERROR: get_xpath did not return a valid XPath for '{description}'. Response: {xpath_response}")
                 return {"error": f"Could not determine XPath for description: '{description}'."}
            xpath = xpath_response["xpath"]
        except Exception as e:
            print(f"ERROR: Call to get_xpath failed for '{description}': {e}")
            return {"error": f"Failed to get XPath using description '{description}': {e}"}

        print(f"INFO: Extracted XPath: {xpath}")
        last_clicked_xpath = xpath
        is_link_xpath = ("//a" in xpath or "/a[" in xpath) and "@href" in xpath
        if is_link_xpath:
             try:
                 link_element = driver.find_element("xpath", xpath)
                 href = link_element.get_attribute('href')
                 if href:
                     print(f"INFO: XPath identifies a link. Extracted href: {href}")
                     if href.startswith("/"):
                         base_url = "/".join(driver.current_url.split("/", 3)[:3])
                         absolute_url = urljoin(base_url, href)
                         print(f"INFO: Converted relative URL to absolute: {absolute_url}")
                     elif href.startswith("http://") or href.startswith("https://"):
                         absolute_url = href
                     elif href.startswith("javascript:"):
                         print(f"INFO: Link has javascript href ('{href}'). Attempting standard click instead of navigation.")
                         link_element.click()
                         sleep(1)
                         print(f"INFO: Clicked javascript link described as '{description}'")
                         return {"result": f"Clicked javascript link described as '{description}'."}
                     else: 
                         print(f"WARN: Unhandled link type or relative path: {href}. Attempting standard click.")
                         link_element.click() 
                         sleep(1)
                         print(f"INFO: Clicked element described as '{description}' (non-standard link).")
                         return {"result": f"Clicked non-standard link described as '{description}'."}

                     
                     print(f"INFO: Navigating to link URL: {absolute_url}")
                     driver.get(absolute_url)
                     sleep(2) 
                     print(f"INFO: Navigation to link complete.")
                     return {"result": f"Navigated to link URL from description '{description}'."}
                 else:
                    print(f"WARN: Link element found but has no href attribute. Attempting standard click.")
                   
                    link_element.click()
                    sleep(1)
                    print(f"INFO: Clicked element described as '{description}' (link without href).")
                    return {"result": f"Clicked element described as '{description}' (link without href)."}

             except Exception as e:
                 print(f"ERROR: Failed to process link element {xpath}: {e}")
                 return {"error": f"Failed to process link element described as '{description}': {e}"}
        else:
            
            print(f"INFO: Element is not a standard link. Performing standard click.")
            element_obj = driver.find_element("xpath", xpath)
            element_obj.click()
            sleep(1) 
            print(f"INFO: Clicked element described as '{description}'")
            return {"result": f"Clicked element described as '{description}'."}

    except Exception as e:
        if "NoSuchElementException" in str(type(e)):
             print(f"ERROR: Element described as '{description}' not found on page with XPath {last_clicked_xpath}.")
             last_clicked_xpath = None 
             return {"error": f"Element described as '{description}' not found on page."}
        else:
            print(f"ERROR: Failed to click element described as '{description}': {e}")
            return {"error": f"Failed to click element described as '{description}': {e}"}


@tool
def close_browser() -> dict:
    """
    Closes all browser windows and tabs associated with the current WebDriver session,
    effectively ending the automation task. Call this function when all browser
    operations are complete.

    Returns:
        dict: A dictionary confirming the browser closure.
    """
    global driver, last_clicked_xpath
    if driver:
        try:
            print("INFO: Closing browser...")
            driver.quit()
            driver = None
            last_clicked_xpath = None
            print("INFO: Browser closed successfully.")
            return {"result": "Browser closed successfully."}
        except Exception as e:
            print(f"ERROR: Error closing browser: {e}")
            driver = None
            last_clicked_xpath = None
            return {"error": f"Error closing browser: {e}"}
    else:
        print("INFO: Browser already closed.")
        return {"result": "Browser was already closed."}