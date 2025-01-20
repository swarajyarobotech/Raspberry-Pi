import RPi.GPIO as GPIO
import time

# Set up GPIO mode and pin
GPIO.setmode(GPIO.BCM)
servo_pin = 17  # Change to your servo's GPIO pin

GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM for controlling the servo
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz PWM frequency
pwm.start(0)  # Start PWM with 0% duty cycle

# Function to rotate servo to 90 degrees
def rotate90():
    duty_cycle = 7.5  # 90 degrees corresponds to 7.5% duty cycle
    pwm.ChangeDutyCycle(duty_cycle)
    print("Rotating to 90 degrees")

# Function to return servo to original position
def returnToOriginal():
    time.sleep(5)  # Wait for 5 seconds
    duty_cycle = 2.5  # 0 degrees corresponds to 2.5% duty cycle
    pwm.ChangeDutyCycle(duty_cycle)
    print("Returning to original position")

# Main function
def main():
    rotate90()  # Rotate servo to 90 degrees
    time.sleep(1)  # Hold at 90 degrees for 1 second
    returnToOriginal()  # Return servo to original position

if __name__ == "__main__":
    try:
        main()
    finally:
        pwm.stop()  # Stop PWM
        GPIO.cleanup()  # Clean up GPIO settings
