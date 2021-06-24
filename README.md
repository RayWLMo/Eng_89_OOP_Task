# Control Flow Age and Permission Task
## Timings
30 Minutes
## Summary
Simple program to use control flow!
## Tasks
* Rules of what the program to do are followed, see below
### Starter code
```py
age = 19
drivers_licence = True

# - You can vote and drive
# - You can vote
# - You can drive
# - you can't legally drink but your mates might have your back (> 16)
# - Your too young, go back to school!

#  as a user I should be able to keep being prompted for input until I say 'exit'
```
## Acceptance Criteria
* class created with required function(s) 
* is a program that run continuously
* handles strings and integers
* has exist condition
* all business logic works
# Solution
Initially the while loop variables are defined
```python
age_prompt = True
licence_prompt = True
```
Class is named and attributes are defined using while loops so incorrect inputs aren't passed through
- `age` attribute has failsafes for both non `int` values and ages higher than `150`
```py
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
```
- `drivers_licence` only filters the answers `yes` and `no` and is aware if someone too young to have a licence says they have one
```py
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
```
Here, the functions `vote`, `drive`, `vote_and_drive`, `drink` are defined as well as the `young` function, which is to detect if the user is too young all the prompts
```py
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
```
Defining the variable as the function, so it can be called
```py
user = Age_Requirements()
query_prompt = True
```
While is defined so that the user is constantly prompted unless they want to exit
```py
while query_prompt:
    user_response = input("\ntype 'vote' to see if you are eligible to vote"
                          "\ntype 'drive' to see if you are eligible to drive"
                          "\ntype 'vote and drive' to see if you are eligible to vote and drive"
                          "\ntype 'drink' to see if you are eligible to drink alcohol"
                          "\ntype 'exit' to close the program"
                          "\nWhat would you like to know?   ")
    print(user.young())  # Tests if the user is underage
    # If the user requests to exit, the while loop is closed and the program stops
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
    else:  # Failsafe incase there is an invalid input
        print("User input is invalid please try again.")
```