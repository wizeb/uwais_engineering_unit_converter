
# ENGINEERING UNIT CONVERTER PROJECT



# Function for converting measurements between millimeters and inches
def length_conversion():
    print("LENGTH CONVERSION")
    print("Option 1: Millimeters to Inches")
    print("Option 2: Inches to Millimeters")

    # Validate the user's conversion choice
    try:
        conversion_choice = int(input("Please Select an Option: \n"))
    except ValueError:
        print("Invalid! Please enter a valid number.")
        return

    if conversion_choice == 1:
        try:
            measurement_mm = float(input("Measurement in mm: \n"))

            # Prevent negative length measurements
            if measurement_mm < 0:
                print("Measurement cannot be negative.")
            else:
                # Convert millimeters to inches
                measurement_inch = measurement_mm / 25.4

                # Allow the user to choose the number of decimal places
                decimal_place = int(input("Decimal Places: \n"))

                # Prevent negative decimal places
                if decimal_place < 0:
                    print("Decimal places cannot be negative.")
                else:
                    print(f"{measurement_inch:.{decimal_place}f} inches")

        except ValueError:
            print("Invalid input! Please enter a number.")

    elif conversion_choice == 2:
        try:
            measurement_inch = float(input("Measurement in inch: \n"))

            # Prevent negative length measurements
            if measurement_inch < 0:
                print("Measurement cannot be negative.")
            else:
                # Convert inches to millimeters
                measurement_mm = measurement_inch * 25.4

                # Allow the user to choose the number of decimal places
                decimal_place = int(input("Decimal Places: \n"))

                # Prevent negative decimal places
                if decimal_place < 0:
                    print("Decimal places cannot be negative.")
                else:
                    print(f"{measurement_mm:.{decimal_place}f} mm")

        except ValueError:
            print("Invalid input! Please enter a number.")

    else:
        print("Invalid input! Please Select Option 1 or 2")


# Function for converting temperatures between Celsius and Fahrenheit
def temperature_conversion():
    print("TEMPERATURE CONVERSION")
    print("Option 1: Celsius to Fahrenheit")
    print("Option 2: Fahrenheit to Celsius")

    # Validate the user's conversion choice
    try:
        conversion_choice = int(input("Please Select an Option: \n"))
    except ValueError:
        print("Invalid! Please enter a valid number.")
        return

    if conversion_choice == 1:
        try:
            temp_celsius = float(input("Temperature in Celsius: \n"))

            # Convert Celsius to Fahrenheit
            temp_fahrenheit = (temp_celsius * 9/5) + 32

            # Allow the user to choose the number of decimal places
            decimal_place = int(input("Decimal Places: \n"))

            # Prevent negative decimal places
            if decimal_place < 0:
                print("Decimal places cannot be negative.")
            else:
                print(f"{temp_fahrenheit:.{decimal_place}f} °F")

        except ValueError:
            print("Invalid input! Please enter a number.")

    elif conversion_choice == 2:
        try:
            temp_fahrenheit = float(input("Temperature in Fahrenheit: \n"))

            # Convert Fahrenheit to Celsius
            temp_celsius = (temp_fahrenheit - 32) * 5/9

            # Allow the user to choose the number of decimal places
            decimal_place = int(input("Decimal Places: \n"))

            # Prevent negative decimal places
            if decimal_place < 0:
                print("Decimal places cannot be negative.")
            else:
                print(f"{temp_celsius:.{decimal_place}f} °C")

        except ValueError:
            print("Invalid input! Please enter a number.")

    else:
        print("Invalid conversion option!")


# Function for converting weights between kilograms and pounds
def weight_conversion():
    print("WEIGHT CONVERSION")
    print("Option 1: Kilograms to Pounds")
    print("Option 2: Pounds to Kilograms")

    # Validate the user's conversion choice
    try:
        conversion_choice = int(input("Please Select an Option: \n"))
    except ValueError:
        print("Invalid! Please enter a valid number.")
        return

    if conversion_choice == 1:
        try:
            weight_kg = float(input("Weight in Kg: \n"))

            # Prevent negative weight measurements
            if weight_kg < 0:
                print("Measurement cannot be negative.")
            else:
                # Convert kilograms to pounds
                weight_lbs = weight_kg * 2.20462

                # Allow the user to choose the number of decimal places
                decimal_place = int(input("Decimal Places: \n"))

                # Prevent negative decimal places
                if decimal_place < 0:
                    print("Decimal places cannot be negative.")
                else:
                    print(f"{weight_lbs:.{decimal_place}f} lbs")

        except ValueError:
            print("Invalid input! Please enter a number.")

    elif conversion_choice == 2:
        try:
            weight_lbs = float(input("Weight in lbs: \n"))

            # Prevent negative weight measurements
            if weight_lbs < 0:
                print("Measurement cannot be negative.")
            else:
                # Convert pounds to kilograms
                weight_kg = weight_lbs / 2.20462

                # Allow the user to choose the number of decimal places
                decimal_place = int(input("Decimal Places: \n"))

                # Prevent negative decimal places
                if decimal_place < 0:
                    print("Decimal places cannot be negative.")
                else:
                    print(f"{weight_kg:.{decimal_place}f} kg")

        except ValueError:
            print("Invalid input! Please enter a number.")

    else:
        print("Invalid conversion option!")


# Function for converting speeds between km/h and m/s
def speed_conversion():
    print("SPEED CONVERSION")
    print("Option 1: km/h to m/s")
    print("Option 2: m/s to km/h")

    # Validate the user's conversion choice
    try:
        conversion_choice = int(input("Please Select an Option: \n"))
    except ValueError:
        print("Invalid! Please enter a valid number.")
        return

    if conversion_choice == 1:
        try:
            speed_kmh = float(input("Speed in km/h: \n"))

            # Prevent negative speed measurements
            if speed_kmh < 0:
                print("Measurement cannot be negative.")
            else:
                # Convert kilometers per hour to meters per second
                speed_ms = speed_kmh / 3.6

                # Allow the user to choose the number of decimal places
                decimal_place = int(input("Decimal Places: \n"))

                # Prevent negative decimal places
                if decimal_place < 0:
                    print("Decimal places cannot be negative.")
                else:
                    print(f"{speed_ms:.{decimal_place}f} m/s")

        except ValueError:
            print("Invalid input! Please enter a number.")

    elif conversion_choice == 2:
        try:
            speed_ms = float(input("Speed in m/s: \n"))

            # Prevent negative speed measurements
            if speed_ms < 0:
                print("Measurement cannot be negative.")
            else:
                # Convert meters per second to kilometers per hour
                speed_kmh = speed_ms * 3.6

                # Allow the user to choose the number of decimal places
                decimal_place = int(input("Decimal Places: \n"))

                # Prevent negative decimal places
                if decimal_place < 0:
                    print("Decimal places cannot be negative.")
                else:
                    print(f"{speed_kmh:.{decimal_place}f} km/h")

        except ValueError:
            print("Invalid input! Please enter a number.")

    else:
        print("Invalid conversion option!")


# Main program loop that displays the menu and handles user choices
while True:
    print("\n")
    print("ENGINEERING UNIT CONVERTER\n")

    print("1. Length Conversion")
    print("2. Temperature Conversion")
    print("3. Weight Conversion")
    print("4. Speed Conversion")
    print("5. Exit")

    # Validate the user's main menu input
    try:
        choice = int(input("Please Enter Your Choice: \n"))

    # Handle non-numeric input errors
    except ValueError:
        print("Please Enter a Valid Number")
        continue

    # Execute the function selected by the user
    if choice == 1:
        length_conversion()

    elif choice == 2:
        temperature_conversion()

    elif choice == 3:
        weight_conversion()

    elif choice == 4:
        speed_conversion()

    elif choice == 5:
        print("Thank You For Using Engineering Unit Converter")
        break

    else:
        print("Invalid Input! Please Select between 1 to 5")
