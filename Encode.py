import os
import time

def turn_on_airplane_mode():
    os.system("netsh interface set interface \"Wi-Fi\" admin=disable")
    print("Airplane mode turned on.")

def turn_off_airplane_mode():
    os.system("netsh interface set interface \"Wi-Fi\" admin=enable")
    print("Airplane mode turned off.")

def use_airplane_mode_for_minutes(minutes):
    start_time = time.time()
    while True:
        turn_on_airplane_mode()
        time.sleep(10)
        turn_off_airplane_mode()
        time.sleep(10)

        elapsed_time = time.time() - start_time
        if elapsed_time >= minutes * 60:
            break

if __name__ == "__main__":
    # Uncomment the function you want to run
    #turn_on_airplane_mode()
    #turn_off_airplane_mode()
    use_airplane_mode_for_minutes(5) # Adjust this number to the number of minutes you want to use airplane mode
