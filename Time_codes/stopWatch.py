import time
import winsound

print("Stopwatch started... Press Ctrl+C to stop.")

start_time = time.time()  # record the start time

try:
    while True:
        elapsed_time = time.time() - start_time
        
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print(f"{minutes:02d}:{seconds:02d}", end="\r")
        winsound.Beep(1000,200)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopwatch stopped.")
    winsound.Beep(1000,700)
