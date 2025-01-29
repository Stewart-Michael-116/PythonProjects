# Portfolio Project
# import dependencies. This requires Python 3.8
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
import nltk
import pandas as pd

# Fix issue with database and time object
nltk.download('punkt_tab')
time.clock = time.time

# Create chatbot
chatbot = ChatBot('Michael\'s Bot')

# Create different trainers
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
list_trainer = ListTrainer(chatbot)

# Read in augmented dataset
dataset = pd.read_csv('question_answer_pairs.txt', delimiter='\t', encoding='utf-8')

# train on each row in the dataframe
for index, row in dataset.iterrows():
    list_trainer.train([
        str(row['Question']),
        str(row['Answer'])
    ])

# Train on these corpuses
corpus_trainer.train(
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.greetings"
)

# Intro message
print('\n\nHello! welcome to Michael\'s first chatbot. Please type and have a conversation.\nType exit or Exit to leave the conversation.')

# Get a response to the input text 'I would like to book a flight.
userInput = "" 

# add illegal words here!
illegal_words = ["bomb", "explosion", "gun"]

# while loop for chatbot to continue talking to user.
while(1):
    userInput = input("")

    if any(word in userInput for word in illegal_words):
        print("I am not allowed to answer this question. Shutting down.")
        break

    if userInput == "exit" or userInput == "Exit":
        break
    response = chatbot.get_response(userInput)

    print(response)