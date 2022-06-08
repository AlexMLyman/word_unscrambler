from itertools import permutations
import spacy
#use spacy to load list of English words
nlp = spacy.load("en_web_core_lg")
english_vocab = set(nlp.vocab.strings)
#if you want to add any words to the vocabulary, put them in this list.
extra_vocab = []
[english_vocab.add(element) for element in extra_vocab]
word_to_unscramble = ''
#perform permutation
for word in permutations(word_to_unscramble):
    if ''.join(word) in english_vocab:
        print(''.join(word))

