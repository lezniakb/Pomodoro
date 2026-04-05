from winotify import Notification, audio
import time
import os

image = os.path.abspath("./static/tomato.png")

if not os.path.exists(image):
    print("[-] Pomodoro image couldn't be loaded! Script will continue without it.")

noti = Notification(
    app_id="Pomodoro",
    title="Time's up!",
    msg="Your time has come to an end.",
    duration="short",
    icon=image
)
noti.set_audio(audio.Reminder, loop=False)

def pomodoro():
    timer = None
    while not timer:
        try:
            timer = float(input("Set the timer (in minutes): "))
        except ValueError as exception:
            print(f"[-] Couldn't process the provided value.\nException: {exception}\n")
    seconds = timer * 60
    time.sleep(seconds)
    noti.show()
    print("Pomodoro finished its job successfully")


if __name__ == "__main__":
    pomodoro()
