from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

with open('/home/amir/projects/helloworld/htmlfiles/TeacherFaisal/file.txt', 'r') as file:
    conversation = file.read()

chatBot = ChatBot('ChatBot')

trainer = ListTrainer(chatBot)
trainer.train(conversation.split('\n'))

print("Hi, I am ChatBot")

while True:
    user_input = input(">>> ")
    if "hi" in user_input.lower():
        response = "Hi there!"
    elif "adjectives" in user_input.lower():
        response = '''Adjectives can be classified into different types based on their function or meaning, including:

Descriptive adjectives: These adjectives describe the physical or sensory qualities of a noun, such as "red," "tall," or "sweet."

Quantitative adjectives: These adjectives describe the quantity or amount of a noun, such as "few," "many," or "three."

Demonstrative adjectives: These adjectives point out or identify a particular noun, such as "this," "that," or "these."

Possessive adjectives: These adjectives indicate possession or ownership, such as "my," "your," or "their."

Interrogative adjectives: These adjectives are used to ask questions about a noun, such as "which," "what," or "whose."

Comparative adjectives: These adjectives compare two or more nouns or pronouns, such as "bigger," "stronger," or "more intelligent."

Superlative adjectives: These adjectives indicate the highest degree of a quality among a group of nouns or pronouns, such as "best," "biggest," or "most beautiful."

Adjectives can be used in different positions in a sentence, including before the noun ("the red car"), after the verb "to be" ("the car is red"), or after certain verbs of sensation ("the car looks red"). Adjectives can also be used to form comparative and superlative forms, such as "bigger" and "biggest," or "more beautiful" and "most beautiful.

and this is a video you can watch about adjectives : https://youtu.be/LiYxv0vudmc '''

    elif "thank you" in user_input.lower() or "thanks" in user_input.lower():
        response = "You're welcome!"
    else:
        response = chatBot.get_response(user_input)

    print(response)
