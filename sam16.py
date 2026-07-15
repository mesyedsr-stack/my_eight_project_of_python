# Age Predictor

current_year = 2026

name = input("Enter your name: ")
birth = int(input("Enter your birth year: "))

if birth > current_year:
    print("Invalid birth year! Try again.")
else:
    age = current_year - birth

    if age <= 12:
        category = "Child"
    elif age <= 19:
        category = "Teenager"
    elif age <= 59:
        category = "Adult"
    else:
        category = "Senior Citizen"

    print("\nHello", name)
    print("Your age is", age)
    print("Your category is", category)
