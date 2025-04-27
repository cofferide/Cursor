import ctypes
import time


def prevent_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000003) #On Screen and Prevent Sleep

def allow_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000) #Enable Power Save

print("Windows Power Save Blocker by https://github.com/cofferide/ \nKeeping system awake... (Press Ctrl+C to stop)")

try:
    while True:
        prevent_sleep()
        time.sleep(30)
except KeyboardInterrupt:
    allow_sleep()
    print("\nSleep mode ON. Exiting.")
