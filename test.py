import time, subprocess
from datetime import datetime, timedelta

def app_block (minutes):
    # Convert the input
    lock_time = int(minutes)
    process_name = "notepad.exe"

    start = datetime.now()
    # End of focus time
    end = start + timedelta(minutes = lock_time)

    # Loop to check the time and prevent the use of several applications
    test = False
    while test == False :
        # Get the time and store it in "now"
        now = datetime.now()
        # When the current time (now) corresponds to the end time (start + input in minutes)
        # test is true which end the loop
        if now >= end :
            test = True
        
        # Employing the taskkill command to terminate the process
        result = subprocess.run(f"taskkill /f /im {process_name}", shell=True)
        # sleep() takes seconds in parameters
        # allows the while loop to check the time each seconds that goes by
        time.sleep(1)

    print("c'est fini !")