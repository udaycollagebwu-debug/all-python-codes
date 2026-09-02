import time
import winsound  # works on Windows

stopTime = int(input("Enter countdown time in seconds : "))
while stopTime > 0:
    print(stopTime)
    time.sleep(1)
    stopTime -= 1
    if stopTime == 0:
        print("Time's up!")
        winsound.Beep(1000, 1000)  