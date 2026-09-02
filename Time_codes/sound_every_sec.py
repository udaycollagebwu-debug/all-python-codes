import time
import winsound

def sound_every_sec(duration):
    for i in range(duration):
        print(f"Time elapsed: {i + 1} seconds")
        winsound.Beep(1000, 500) 
        time.sleep(1)



duration = int(input("Enter duration in seconds: "))
sound_every_sec(duration)