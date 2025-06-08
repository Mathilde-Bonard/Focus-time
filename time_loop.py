from datetime import datetime, timedelta
import time

minutes = input("Temps de blocage souhaité en min : ")

lock_time = int(minutes)
start = datetime.now()
end = start + timedelta(minutes = lock_time)

# time.sleep(20)

# time_elapsed = datetime.now()-start

# if time_elapsed >= lock_time *60

print(start.strftime("%H:%M"))
print(end.strftime("%H:%M"))


# Loop to check the time and prevent the use of several applications
test = False
while test == False :
    # Get the time and store it in "now"
    now = datetime.now()
    # When the current time (now) corresponds to the end time (start + input in minutes)
    # test is true which end the loop
    if now >= end :
        test = True
    # sleep() takes seconds in parameters
    # allows the while loop to check the time each seconds that goes by
    time.sleep(1)

print("c'est fini !")
