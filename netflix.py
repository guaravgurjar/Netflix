import pyautogui 
import time

# Function to close the Netflix window
def close_netflix():
    # Move the mouse to the close button of the Netflix window
    pyautogui.moveTo(1342, 15)  # Adjust the coordinates based on your screen resolution

    # Click the close button
    pyautogui.click()

# Function to simulate watching Netflix for one hour
def watch_netflix():
    # Start the timer
    start_time = time.time()

    # Simulate watching for one hour (3600 seconds)
    while time.time() - start_time < 30:
        # You can add additional code here if needed
        # For example, check if the Netflix window is still active or if the video is playing
        # If required, you can use pyautogui to automate these actions as well

        # Sleep for a short interval
        time.sleep(5)  # Adjust the interval based on your needs

    # Close Netflix after one hour
    close_netflix()

# Call the function to watch Netflix
watch_netflix()
