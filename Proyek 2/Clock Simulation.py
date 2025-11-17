from datetime import datetime, timedelta
import time

# starting point
sim_time = datetime(2025, 1, 1, 0, 0, 0)  # Start at Jan 1, 8:00 AM

while True:
    print(sim_time.strftime("%Y-%m-%d %H:%M"))

    time.sleep(1)           # real time
    sim_time += timedelta(hours=1)  # jump 1 hour