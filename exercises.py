from datetime import date

# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
# print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    alphabet = "abcdefghijlkmnopqrstuvwxyz"
    vowels = "aeiou"
    inp = input("Enter a letter (a-z or A-Z): ").lower()
    while not inp or inp not in alphabet:
        inp = input("Letter is not in acceptable range: ")
    
    if inp in vowels: print(f"The letter {inp} is a vowel.")
    else: print(f"The letter {inp} is a consonant.")

# Call the function
# check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    voting_age = 18
    inp = input("Please enter your age: ")
    try:
        age = int(inp)
    except:
        age = 0
        
    if age >= voting_age: print("you are eligible to vote.")
    else: print("You are not eligible to vote.")
    

# Call the function
# check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    inp = input("Input a dog's age: ")
    try:
        dog_age = int(inp)
    except:
        dog_age = -1
    
    if dog_age >= 0:
        first_2_years = min(2, dog_age)
        rest_years = dog_age - first_2_years
        age = first_2_years*10 + rest_years*7
        print(f"The dog's age in dog years is {age}.")
    else:
        print("Your dog doesn't exist.")

# Call the function
# calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    yes = ('y', 'yes')
    cold = input("Is it cold outside? (Y/N): ").lower() in yes
    rain = input("Is it raining outside? (Y/N): ").lower() in yes
    scenario = 2*int(cold) + int(rain)
    
    match scenario:
        case 3:
            return print("Wear a waterproof coat.")
        case 2:
            return print("Wear a warm coat.")
        case 1:
            return print("Carry an umbrella.")
        case 0:
            return print("Wear light clothing.")

# Call the function
# weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    months = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
    month = input("Enter the month of the year (Jan - Dec): ").lower()
    while not month or month not in months:
        month = input("Invalid month code: ")
    month_num = months.index(month)+1
    
    long_months = (1, 3, 5, 7, 8, 10, 12)
    max_days = 30 + int(month_num in long_months)
    if month_num == 2: max_days -= 2

    valid_days = [str(i) for i in range(1, max_days+1)]
    day = input("Enter the day of the month: ")
    while day not in valid_days:
        day = input("Invalid day: ")
    day = int(day)
    
    inp_date = date(2024, month_num, day)
    winter_end = date(2024, 3, 19)
    spring_end = date(2024, 6, 20)
    summer_end = date(2024, 9, 21)
    fall_end = date(2024, 12, 20)
    
    season = "Winter"
    if inp_date <= fall_end: season = "Fall"
    if inp_date <= summer_end: season = "Summer"
    if inp_date <= spring_end: season = "Spring"
    if inp_date <= winter_end: season = "Winter"
    
    print(f"{month.capitalize()} {day} is in {season}.")

# Call the function
# determine_season()

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    success = "Congratulations, you guessed correctly!"
    failed = "Sorry, you failed to guess the number in five attempts."
    low = "Guess is too low."
    high = "Guess is too high."
    secret = 69
    guesses = 5
    winner = False
    
    while guesses >= 1:
        if guesses == 1: print("Last chance!")
        inp = input(f"Guess a number 0-100 ({guesses} guess{'es' if guesses > 1 else ''} remain{'s' if guesses==1 else ''}): ")
        try:
            inp = int(inp)
        except:
            print("Not a valid number.")
            guesses -= 1
            continue
        
        if inp == secret:
            winner = True
            break
        print(low if inp < secret else high)
        guesses -= 1
    
    print(success if winner else failed)

# Call the function
guess_number()
