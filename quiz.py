#Introduction
name = input("Please, allow me introduce myself. I am a K-2SO, reprogrammed Imperial security droid. \nTo proceed further, please, tell me your name: ")
print(f"{name}? Now, that's a name I've not heard in a long time. A long time.")

yes_no = input("I need to ask you few questions. Do you want to take a little quiz? ")

if yes_no.lower() == "yes":
    print("Great! This is where the fun begins!")
elif yes_no.lower() == "no":
    print("Goodbye, old friend. May the Force be with you.")
    quit()
else:
    print("Sorry, lady. I don't understand frog.")
    quit()

#Counting accurate answers
accuracy = 0

#Questions and correct answers
questions = {
    "What is Jedi/Sith lightsaber powered by?": ["kyber crystal"],
    "Who owned Anakin Skywalker and Shmi Skywalker?": ["toydarian watto"],
    "Who discovered the secrets to immortality?": ["yoda"],
    "Which planet was Padme Amidala the queen of?": ["naboo"]
}

#Iterating through questions and correct answers
for question, alternatives in questions.items():
    correct = alternatives[0]

    answer = input(f"{question} ")
    if answer.lower() == correct:
        print("Good... Good...")
        accuracy += 1
    else:
        print("Incorrect! Next question!")

#Storing prefilled responses
response1 = f"You've got {accuracy} correct out of {len(questions)}."

response2 = ["Amazing. Every word of what you just said was wrong.",
            "Why do I get the feeling that I've picked up another pathetic life form?",
            "The ability to speak does not make you intelligent.",
            "Great, kid, don't get cocky.",
            "You're a much wiser man than I am. I foresee you will become a great Jedi knight."
            ]

#Printing a suitable response
if accuracy == 0:
    print(f"{response1} {response2[0]}")
elif accuracy == 1:
    print(f"{response1} {response2[1]}")
elif accuracy == 2:
    print(f"{response1} {response2[2]}")
elif accuracy == 3:
    print(f"{response1} {response2[3]}")
else:
    print(f"{response1} {response2[4]}")