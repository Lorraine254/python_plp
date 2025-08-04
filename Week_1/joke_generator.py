import random
import time

# List of jokes
jokes = [["Why do programmers prefer dark mode? Because light attracts bugs."],
    "Why did the Python developer go on a diet? Because they had too many bytes!",
    "Why don’t Python programmers need glasses? Because they can clearly see self.",
    "How do you comfort a JavaScript bug? You console it.",]


# Defining a function to tell the joke
def tell_joke(joke):
    print("About to crack you up!")
    time.sleep(2)
    print("Here's a joke for you...\n")
    time.sleep(1)
    print(f"{joke}")
    time.sleep(2)
    print("Thanks for coming to my ted talk")

#select a random joke
selected_joke = random.choice(jokes)

# Tell the joke
tell_joke(selected_joke)