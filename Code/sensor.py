# Import libraries
import time
from periphery import GPIO

# Configure GPIO pins
gpio_in = GPIO("/dev/gpiochip0", 9, "in")  # pin 11

def main():
    """Main function to read sensor value from pin 11"""
    try:
        while True:
            # Read the input pin
            input_value = gpio_in.read()
            
            # Print the sensor value
            print(f"Sensor value : {input_value}")
            
            # Delay for a short period of time
            time.sleep(0.1)

    except KeyboardInterrupt:
        # Clean up GPIO pins and exit
        gpio_in.close()
        print("\nExiting gracefully.")

# Main
if __name__ == '__main__':
    main()
