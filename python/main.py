from functions import *from config import *import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO libraryfrom time import sleep     # Import the sleep function from the time modulecurrentLedIndex = 0prevLedIndex = 0GPIO.setwarnings(False)    # Ignore warning for nowGPIO.setmode(GPIO.BOARD)   # Use physical pin numberingiothub_client_telemetry_sample_run()while True:    currentLed = ledsArray[currentLedIndex]    if(currentLed != prevLedIndex) :        prevLed = ledsArray[prevLedIndex]        GPIO.setup(prevLed, GPIO.OUT, initial=GPIO.LOW)    GPIO.setup(currentLed, GPIO.OUT, initial=GPIO.HIGH)    prevLedIndex = currentLedIndex    if(currentLedIndex >= 3) :        currentLedIndex = 0    else:        currentLedIndex = currentLedIndex + 1    sleep(delay)