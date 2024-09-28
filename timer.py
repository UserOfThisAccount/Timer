import time


def countdown_time(seconds):
    while seconds:
        hours, mins = divmod(seconds, 3600)
        mins, secs = divmod(seconds, 60)
        timer = f"{hours:02d}:{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Times Up!")


try:
    user_input = int(input("Enter the time in seconds: "))
    if user_input < 0:
        print("Please, provide a non negeative integer: ")
    else:
        countdown_time(user_input)
except ValueError:
    print("Invalid! PLease, enter an integer")
