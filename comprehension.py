import random  # Import the random module

guessesTaken = 0  # Assign 0 to guessesTaken variable

print('Hello! What is your name?')  # Print out the user a question about his/her name
myName = input()  # Store the input from the user in a variable called myName

number = random.randint(1, 20)  # Generate a random number between 1 and 20 and assign it to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Print out the name of the user and that the script is thinking of a number

while guessesTaken < 6:  # Create a while loop to iterate through the actions in it until guessesTaken variable reaches value 6
    print('Take a guess.')  # Print out a message to user to take a guess
    guess = input()  # Store the input value in the guess variable
    guess = int(guess)  # Convert the value of guess to integer

    guessesTaken += 1  # Add +1 to guessesTaken variable every time we iterate through the above code

    if guess < number:  # Check if guess variable is lower than number variable
        print('Your guess is too low.')  # Print out that the user's guess is too low

    if guess > number:  # Check if guess variable is higher than number variable
        print('Your guess is too high.')  # Print out that the user's guess is too high

    if guess == number:  # Check if guess variable is equal to number variable
        break  # If the above statement is True, break out of the while loop

if guess == number:  # Check if guess variable is equal to number variable
    guessesTaken = str(guessesTaken)  # Convert guessesTaken variable to string
    # Print out the user that he guessed the number including his name and the number of guesses taken
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:  # Check if guess variable is not equal to number variable
    number = str(number)  # Convert the number variable to string
    print('Nope. The number I was thinking of was ' + number)  # Print out the user he has not guessed the number and also the value of the number variable
