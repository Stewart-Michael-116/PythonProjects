# Michael Stewart Critical Thinking 5
# Text Augmentation Script

# Import NLP Augmentation library and tokenizer
import nlpaug.augmenter.word as naw
import sacremoses
import pandas as pd
import numpy as np
import nltk
import random

# Replace Word
def replace_word_with_synonym(raw_sentence):
    # split words, choose a random one, get synonym
    sentence = str(raw_sentence)
    words = sentence.split()
    word_to_replace = random.choice(words)
    synonym = augmenter.augment(word_to_replace)
    
    new_words = []
    # replace it in array
    for word in words:
        if word == word_to_replace:
            new_words.append(synonym[0])
        else:
            new_words.append(word)

    separator = ' '
    return separator.join(new_words)

# Load augmenter and resources needed
nltk.download('averaged_perceptron_tagger_eng')
augmenter = naw.synonym.SynonymAug(aug_src='wordnet')

# Load dataset
raw_dataset = pd.read_csv('question_answer_pairs.txt', delimiter='\t', encoding='utf-8')
processed_dataset = raw_dataset.iloc[:,[1,2]]

processed_dataset = processed_dataset.map(replace_word_with_synonym)

print(processed_dataset.head())

processed_dataset.to_csv('augmented data set.txt', sep='\t', index=False)

print(replace_word_with_synonym('was Alessandro Volta taught in public schools?'))
# References
# https://www.geeksforgeeks.org/text-augmentation-techniques-in-nlp/
# https://www.youtube.com/watch?v=QF1FlfEMVOM
