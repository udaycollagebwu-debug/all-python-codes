import time
import winsound

def forceClose(end):
    try:
        for i in range(1,end+1):
            print(i,end="\r")
            winsound.Beep(1000,200)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stop the clock forcefilly !!")
        winsound.Beep(1000,500)

print("You wand to stop the watch forsefully then press Control + C")
print("The code will run upto 1000 times")
forceClose(1000)