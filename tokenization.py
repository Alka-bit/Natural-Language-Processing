import os
from tensorflow.keras.preprocessing.text import Tokenizer

with open('../input/selected-poems-by-emily-dickinsonn/Selected-Poems-by-Emily-Dickinsonn.txt') as f:
    poem = f.readlines()
    print(poem)
    
tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(poem)

word_index = tokenizer.word_index
print(word_index)

