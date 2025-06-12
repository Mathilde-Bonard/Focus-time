import time, subprocess, psutil
from datetime import datetime, timedelta

def check_if_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

def app_block (minutes, process_name):
    # Convert the input
    lock_time = int(minutes)
    # Start is taking the current time, end is a calculation of the end time (start + input in minutes)
    start = datetime.now()
    end = start + timedelta(minutes = lock_time)

    # Loop to check the time and prevent the use of several applications
    # When the current time (now) corresponds to the end time 
    # end the loop
    test = False
    while test == False :
        now = datetime.now()

        if check_if_process_running(process_name):
        # Employing the taskkill command to terminate the process
            subprocess.run(f"taskkill /f /im {process_name}", shell=True)
        if now >= end :
            test = True

        # sleep() takes seconds in parameters
        # allows the while loop to check the time each seconds that goes by
        time.sleep(1)

    print("c'est fini !")