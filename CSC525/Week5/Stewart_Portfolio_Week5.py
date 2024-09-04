# Training Chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
import nltk

nltk.download('punkt_tab')
time.clock = time.time


# Create a new chat bot named Charlie
chatbot = ChatBot('Michael\'s Bot')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.greetings"
)

print('\n\nHello! welcome to Michael\'s first chatbot. Please type and have a conversation.\nType exit or Exit to leave the conversation.')

# Get a response to the input text 'I would like to book a flight.'
userInput = input("hello! please input a sentence for the chatbot\n") 

response = chatbot.get_response(userInput)

print(response)