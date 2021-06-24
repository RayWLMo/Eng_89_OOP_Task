age = 19
driver_license = True
user_prompt = True

while user_prompt:
    driver_license = input("Do you have a valid driver's licence (type 'exit' to close the program)? Yes/No    ")
    age = input("Please enter Your Age (press Enter to close):    ")
    if driver_license == "exit":
        print("Thank you for using this program")
        break
    elif int(age) < 16:
        print("You're too young, go back to school!")
    elif 16 <= int(age) < 18:
        print("You can't legally drink but your mates/aunties might have your back")
    elif 18 <= int(age) < 150 and driver_license.lower() == "yes":
        print("You can drive")
    elif 18 <= int(age) <= 150 and driver_license.lower() == "no":
        print("You can vote")
    elif 18 <= int(age) <= 150 and driver_license.lower() == "yes":
        print("You can vote and drive")
    elif int(age) > 150:
        print(f"You're clearly not {age} years old, please enter a valid age in digits")
    elif driver_license.lower() != "no" or driver_license.lower() != "yes":
        print("Driver's licence input entered is invalid, please enter a valid response")
    else:
        print(f"The age entered is invalid, please enter a valid age in digits")


