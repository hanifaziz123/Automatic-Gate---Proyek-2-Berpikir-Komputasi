from datetime import datetime, timedelta
import time
import threading

# Starting point for simulation
sim_time = datetime(2025, 1, 1, 0, 0, 0)
SIM_START = sim_time  # Save start reference

# A lock to prevent simultaneous read/write conflicts
lock = threading.Lock()

def run_clock():
    global sim_time
    while True:
        time.sleep(1)  # 1 real second
        with lock:
            sim_time += timedelta(hours=1)  # 1 simulated hour

# Start the clock thread
threading.Thread(target=run_clock, daemon=True).start()

def konversiWaktuFull(dt):
    """Convert datetime to minutes since simulation start."""
    delta = dt - SIM_START
    return int(delta.total_seconds() // 60)

# MAIN INPUT LOOP
while True:
    cmd = input("Press 0 to show simulated minutes: ")

    if cmd == "0":
        with lock:
            print("Sim time:", sim_time.strftime("%Y-%m-%d %H:%M"))
            print("Minutes since start:", konversiWaktuFull(sim_time))
