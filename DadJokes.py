# Lab Module 5: Dad Jokes
# Emily Smith


# Importing the Random Module:
import random

print("Welcome to the Dad Joke Generator!\n")

# List of Dad Jokes
dad_jokes = ["Why don't eggs tell jokes? They might crack up!",
             "Why are libraries so tall? Because they have so many stories.",
             "Want to hear a construction joke? I'm still working on it.",
             "Where do fruits go on vacation? Pear-is.",
             "Why didn't the chef season his dish? He ran out of thyme.",
             "Why did the math book look sad? It had too many problems.",
             "What do you call cheese that isn't yours? Nacho cheese.",
             "Why are ghosts bad liars? You can see right through them.",
             "What kind of tree fits in your hand? A palm tree!",
             "Want to hear a joke about pizza? Never mind...it's too cheesy."]

# Total Number of Dad Jokes
print("We have " + str(len(dad_jokes)) + " dad jokes in our collection.\n")

# Display Random Jokes Using a for Loop 4 Times
print("Here are 4 random dad jokes:\n")

for i in range(4):
    print(random.choice(dad_jokes))

# Ending the Program
print("\nThank you for using the Dad Joke Generator!")