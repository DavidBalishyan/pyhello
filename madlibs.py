# Madlibs game
# Word game where you create a story by filling in the blanks with random words


print("Welcome to Mad Libs game!")
name = input("What is your name? ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")

story = f"Once upon a time there was a {adjective1} person named {name}. " \
        f"They really liked {adjective2} {noun1} and {adjective3} {noun2}. " \
        f"One day they saw a {animal} eating a {food}. " \
        f"This made them very happy."

print("Here is your story:")
print(story)