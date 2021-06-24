age_prompt = True
licence_prompt = True


class Age_Requirements:

    def __init__(self):
        while age_prompt:
            self.age = input("Please enter your age in digits:   ")
            if not self.age.isdigit():
                print("The input given is invalid.")
            elif int(self.age) > 150:
                print(f"You're clearly not {self.age} years old.")
            else:
                break
        while licence_prompt:
            self.drivers_licence = input("Do you have a valid driver's licence? (Yes/No):    ")
            if int(self.age) < 16 and self.drivers_licence.lower() == "yes":
                print("You're too young to have a driver's licence aren't you?")
                self.drivers_licence = False
                break
            elif self.drivers_licence.lower() == "yes":
                self.drivers_licence = True
                break
            elif self.drivers_licence.lower() == "no":
                self.drivers_licence = False
                break
            else:
                print("The input given is invalid, please try again.")

    def vote(self):
        if int(self.age) >= 18:
            return "Hooray! You can vote!"
        else:
            return "You're too young to vote."

    def drive(self):
        if user.drivers_licence:
            return "You can drive but don't drink and drive!"
        else:
            return "You cannot drive."

    def vote_and_drive(self):
        if int(self.age) < 18 and self.drivers_licence:
            return "You're too young to vote but you can drive!"
        if int(self.age) < 18 and self.drivers_licence == False:
            return "You're too young to vote and you can't drive."
        else:
            return "Hooray! You can vote and drive!"

    def drink(self):
        if 16 <= int(self.age) < 18:
            return "You can't legally drink but your mates might have your back."
        else:
            return "You can drink but don't drink and drive!"

    def young(self):
        if int(self.age) < 16:
            return "You're too young, go back to school!"
        else:
            return ""


user = Age_Requirements()
query_prompt = True

while query_prompt:
    user_response = input("\ntype 'vote' to see if you are eligible to vote"
                          "\ntype 'drive' to see if you are eligible to drive"
                          "\ntype 'vote and drive' to see if you are eligible to vote and drive"
                          "\ntype 'drink' to see if you are eligible to drink alcohol"
                          "\ntype 'exit' to close the program"
                          "\nWhat would you like to know?   ")
    print(user.young())
    if user_response.lower() == "exit":
        print("Thank you for using this program")
        query_prompt = False
    elif user_response.lower() == "vote":
        print(user.vote())
    elif user_response.lower() == "drive":
        print(user.drive())
    elif user_response.lower() == "vote and drive":
        print(user.vote_and_drive())
    elif user_response.lower() == "drink":
        print(user.drink())
    else:
        print("User input is invalid please try again.")
