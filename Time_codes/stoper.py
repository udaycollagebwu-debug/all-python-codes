import time
import winsound  # works on Windows

start = time.time()
input("Press Enter to stop...")  # wait until you press Enter
end = time.time()

elapsed = round(end - start, 2)
print("Elapsed time:", elapsed, "seconds")

# play a beep sound
winsound.Beep(1000, 500)  # frequency=1000Hz, duration=500ms
