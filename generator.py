import webapp2
import dbmodels
import logging
import random
from random import choice, randint
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
def word():
    word_length = randint(1, 12)
    if word_length == 1:
        return choice(VOWELS)
    w = ""
    while word_length > 0:
        w += choice([VOWELS, CONSONANTS][word_length % 2])
        word_length -= 1
    if random.random() > 0.8:
        logging.info("cap")
        w = w.capitalize()
        logging.info(w)
    return w

def sentence():
    sentence_length = randint(1, 12)
    s = [word().capitalize()]
    while sentence_length > 0:
        s.append(word())
        sentence_length -= 1
    return " ".join(s)+choice("?!.")

def paragraph():
    paragraph_length = randint(1, 12)
    p = []
    while paragraph_length > 0:
        p.append(sentence())
        paragraph_length -= 1
    return "\n".join(p)


        
                             
                             


              
