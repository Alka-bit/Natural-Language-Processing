import os
from tensorflow.keras.preprocessing.text import Tokenizer
#This lib helps vectorize a text corpus, by turning each text into either a sequence of integers (each integer being the index of a token in a dictionary) or into a vector where the coefficient for each token could be binary.

with open('../input/selected-poems-by-emily-dickinsonn/Selected-Poems-by-Emily-Dickinsonn.txt') as f:
    poem = f.readlines()
    print(poem)
    
tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(poem) #Updates internal vocabulary based on a list of sequences.

word_index = tokenizer.word_index
print(word_index)

