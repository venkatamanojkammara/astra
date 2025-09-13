import time
import pyautogui
import subprocess
from langchain.agents import tool


@tool
def play_song(song_name: str):
    """
    Plays a song by searching for the song.
    Args:
        song_name (str): The name of the song to be played.
    Returns:
        Sucess message after playing the song.
    """
    try:
        print(f"trying to play the {song_name} song...")
        pyautogui.hotkey('ctrl', 'k')
        time.sleep(2)
        pyautogui.write(song_name, interval=0.2)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        print(f"Action Completed: Playing the {song_name} song...")
        return f"result: Playing the {song_name} song..."
    except Exception as e:
        print(f"Action Failed: Error playing the {song_name} song: {e}.")
        return f"Error playing the {song_name} song: {e}."


@tool
def pause_song():
    """
    Pauses the currently playing the song in spotify, if playing any.
    Returns:
        Sucess message after pausing the song.
    """
    try:
        subprocess.Popen('spotify')
        time.sleep(5)
        pyautogui.press('space')
        print("Action Completed: Paused the currently playing song...")
        return "result: Paused the currently playing song..."
    except Exception as e:
        print(f"Action Failed: Error pausing the song: {e}.")
        return f"Error pausing the song: {e}."
    

@tool
def resume_song():
    """
    Resumes the currently paused song in spotify, if any.
    Returns:
        Sucess message after resuming the song.
    """
    try:
        subprocess.Popen('spotify')
        time.sleep(5)
        pyautogui.press('space')
        print("Action Completed: Resumed the currently paused song...")
        return "result: Resumed the currently paused song..."
    except Exception as e:
        print(f"Action Failed: Error resuming the song: {e}.")
        return f"Error resuming the song: {e}."


@tool
def next_song():
    """
    Skips to the next song in spotify and plays it.
    Returns:
        Sucess message after skipping to the next song.
    """
    try:
        subprocess.Popen('spotify')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'right')
        print("Action Completed: Skipped to the next song and playing... ")
        return "result: Skipped to the next song and playing..."
    except Exception as e:
        print(f"Action Failed: Error skipping to the next song: {e}.")
        return f"Error skipping to the next song: {e}."
    

@tool
def previous_song():
    """
    Goes back to the previous song in spotify and plays it.
    Returns:
        Sucess message after going back to the previous song.
    """
    try:
        subprocess.Popen('spotify')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'left')
        print("Action Completed: Went back to the previous song and playing...")
        return "result: Went back to the previous song and playing..."
    except Exception as e:
        print(f"Action Failed: Error going back to the previous song: {e}.")
        return f"Error going back to the previous song: {e}."


@tool
def control_volume(action: str, volume_times: int):
    """
    Controls the music volume in spotify by either increasing or decreasing it.
    Args:
        action (str): The action to be performed, either 'volumeup' or 'volumedown'.
        volume_times (str): The number of times to increase or decrease the volume.
    Returns:
        Message indicating the result of the volume control action.
    """
    try:
        if action.lower() in ['volumeup', 'volumedown']:
            for _ in range(volume_times):
                pyautogui.press(action)
            print(f"Action Completed: {action}d the volume {volume_times} times.")
            return f"result: {action} by {volume_times} times."
        else:
            print("Enter a valid action: 'volumeup' or 'volumedown'.")
    except Exception as e:
        print(f"Action Failed: Error controlling the volume: {e}.")
        return f"Error controlling the volume: {e}."

