import RPi.GPIO as GPIO
import subprocess
import time

PIR_PIN = 17 # GPIO pin connected to PIR sensor output
SLEEP_MINUTES = 30 # Time in minutes before sleep (feel free to change)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

screen_on = True
last_motion = time.time()

def screen_off():
    subprocess.run(['xset', '-display', ':0', 'dpms', 'force', 'off'])

def screen_wake():
    subprocess.run(['xset', '-display', ':0', 'dpms', 'force', 'on'])
    subprocess.run(['xset', '-display', ':0', 's', 'reset'])

print("PIR monitor running...")

try:
    while True:
        motion = GPIO.input(PIR_PIN)

        if motion:
            last_motion = time.time()
            print("Motion detected...")
            if not screen_on:
                print("Motion detected, waking screen...")
                screen_wake()
                screen_on = True

        if screen_on and (time.time() - last_motion) > (SLEEP_MINUTES * 60):
            screen_off()
            screen_on = False
            print("No motion detected for 30 minutes, turning off screen...")

        time.sleep(2)  # Check every 2 seconds

except KeyboardInterrupt:
    GPIO.cleanup()
    print("PIR monitor stopped.")
