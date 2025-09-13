from agent_tools.clipboard_tools import (paste_from_clipboard, copy_to_clipboard, get_selected_text)
from agent_tools.gui_tools import (close_app, press_key, close_tab, close_window, open_new_tab, refresh_page, press_shortcut, take_screenshot, send_message_or_text, scroll_page, search_text)
from agent_tools.media_tools import (play_song, pause_song, resume_song, next_song, previous_song, control_volume)
from agent_tools.selenium_tools import (launch_browser, navigate_current_tab, open_url_in_new_tab, switch_to_tab, close_current_tab, perform_web_search, type_text_into_element, click_element_by_description, close_browser)
from agent_tools.utility_tools import (get_current_datetime, open_application, open_file, open_folder, execute_command)
from agent_tools.web_tools import (open_url, search_web)
from utils import (write_code, write_text)

from langchain.agents import Tool


tools = [
    Tool(
        name='PasteClipboard',
        func=paste_from_clipboard,
        description='Use this tool to paste text from the clipboard. No input is required.'
    ),
    Tool(
        name='CopyClipboard',
        func=copy_to_clipboard,
        description='Use this tool to copy the text to clipboard. Input should be the text to be copied.'
    ),
    Tool(
        name='GetSelectedText',
        func=get_selected_text,
        description='Use this tool to get the currently selected text. No input is to be provided.'
    ),
    
    Tool(
        name='CloseApp',
        func=close_app,
        description='Use this tool to close an application. Input should be the application name (app_name)'
    ),
    Tool(
        name='PressKey',
        func=press_key,
        description='Use this tool to press a single key on the keyboard. Input should be the key to be pressed, e.g., "enter", "tab", "escape", "up", "down", "left", "right", etc.'
    ),
    Tool(
        name='CloseTab',
        func=close_tab,
        description='Use this tool to close the current active tab in the application. No input is required.'
    ),
    Tool(
        name='CloseWindow',
        func=close_window,
        description='Use this tool to close the current active window. No input is required.'
    ),
    Tool(
        name='OpenNewTab',
        func=open_new_tab,
        description='Use this tool to open a new tab in the current application. No input is required.'
    ),
    Tool(
        name='RefreshPage',
        func=refresh_page,
        description='Use this tool to refresh the current page in the application. No input is required.'
    ),
    Tool(
        name='PressShortcut',
        func=press_shortcut,
        description='Use this tool to press a keyboard shortcut. Input should be the shortcut keys separated by "+", e.g., "ctrl+c", "ctrl+v", "alt+f4", etc.'
    ),
    Tool(
        name='searchText',
        func=search_text,
        description='Use this tool to search for a specific text. Input should be the text to be searched.'
    ),
    Tool(
        name='TakeScreenshot',
        func=take_screenshot,
        description='Use this tool to take a screenshot of the current screen. Input should be the directory path where the screenshot will be saved, e.g., "Pictures/Screenshots".'
    ),
    Tool(
        name='SendMessageOrText',
        func=send_message_or_text,
        description='Use this tool to send a message or text in the current active window. Input should be the text to be sent.'
    ),
    Tool(
        name='ScrollPage',
        func=scroll_page,
        description='Use this tool to scroll the current page. Input should be in the format "direction amount", where direction is either "up" or "down", and amount is the number of pixels to scroll, e.g., "down 300".'
    ),
    Tool(
        name='PlaySong',
        func=play_song,
        description='Use this tool to play a song. Input should be the name of the song to be played.'
    ),
    Tool(
        name='PauseSong',
        func=pause_song,
        description='Use this tool to pause the currently playing song. No input is required.'
    ),
    Tool(
        name='ResumeSong',
        func=resume_song,
        description='Use this tool to resume the paused song. No input is required.'
    ),
    Tool(
        name='NextSong',
        func=next_song,
        description='Use this tool to skip to the next song in the playlist. No input is required.'
    ),
    Tool(
        name='PreviousSong',
        func=previous_song,
        description='Use this tool to go back to the previous song in the playlist. No input is required.'
    ),
    Tool(
        name='ControlVolume',
        func=control_volume,
        description='Use this tool to control the volume. Input should be in the format "up amount" or "down amount", where amount is the percentage to increase or decrease the volume, e.g., "up 10".'
    ),
    Tool(
        name='LaunchBrowser',
        func=launch_browser,
        description='Use this tool to launch a web browser. No input is required.'
    ),
    Tool(
        name='NavigateCurrentTab',
        func=navigate_current_tab,
        description='Use this tool to navigate the current active tab to a specified URL. Input should be the URL to navigate to, e.g., "https://www.example.com".'
    ),
    Tool(
        name='OpenUrlInNewTab',
        func=open_url_in_new_tab,
        description='Use this tool to open a specified URL in a new tab. Input should be the URL to be opened, e.g., "https://www.example.com".'
    ),
    Tool(
        name='SwitchToTab',
        func=switch_to_tab,
        description='Use this tool to switch to a specific tab by its index. Input should be the index of the tab (0 for the first tab, 1 for the second tab, etc.).'
    ),
    Tool(
        name='CloseCurrentTab',
        func=close_current_tab,
        description='Use this tool to close the current active tab in the browser. No input is required.'
    ),
    Tool(
        name='PerformWebSearch',
        func=perform_web_search,
        description='Use this tool to type text into an active input field on a webpage. Input should be the text to be typed.'
    ),
    Tool(
        name='TypeTextIntoElement',
        func=type_text_into_element,
        description='Use this tool to type text into a specific element on a webpage based on its description. Input should be the text to be typed followed by the element description, separated by a semicolon, e.g., "hello world; search bar".'
    ),
    Tool(
        name='ClickElementByDescription',
        func=click_element_by_description,
        description='Use this tool to click an element on a webpage based on its description. Input should be the description of the element to be clicked, e.g., "first link", "submit button", etc.'
    ),
    Tool(
        name='CloseBrowser',
        func=close_browser,
        description='Use this tool to close the web browser. No input is required.'
    ),
    Tool(
        name='GetCurrentDatetime',
        func=get_current_datetime,
        description='Use this tool to get the current date and time. No input is required.'
    ),
    Tool(
        name='OpenApplication',
        func=open_application,
        description='Use this tool to open an application on your system. Input should be the name of the application to be opened, e.g., "notepad", "calculator", etc.',
    ),
    Tool(
        name='OpenFile',
        func=open_file,
        description='Use this tool to open a specific file on your system. Input should be the full path of the file to be opened, e.g., "C:/path/to/your/file.txt".'
    ),
    Tool(
        name='OpenFolder',
        func=open_folder,
        description='Use this tool to open a specific folder on your system. Input should be the full path of the folder to be opened, e.g., "C:/path/to/your/folder".'
    ),
    Tool(
        name='ExecuteCommand',
        func=execute_command,
        description='Use this tool to execute a system command. Input should be the command to be executed, e.g., "dir", "ls", "ping google.com", etc.'
    ),
    Tool(
        name='OpenUrl',
        func=open_url,
        description='Use this tool to open a specified URL in the default web browser. Input should be the URL to be opened, e.g., "https://www.example.com".'
    ),
    Tool(
        name='SearchWeb',
        func=search_web,
        description='Use this tool to perform a web search using a specified query. Input should be the search query, e.g., "python programming".'
    ),
    Tool(
        name='WriteCode',
        func=write_code,
        description='Use this tool to write code in the current active window. Input should be the code to be written.'
    ),
    Tool(
        name='WriteText',
        func=write_text,
        description='Use this tool to write text in the current active window. Input should be the text to be written.'
    )
]
