from nltk.corpus import wordnet as wn


class Dictionary:

    def __init__(self):
        pass


    # using wordnet, gets all definitions of a given word
    def define(self, word):
        synsets = wn.synsets(word)
        if not synsets:
            return False
        
        definitions = []
        for syn in synsets:
            definitions.append(syn.definition())
        
        return definitions
    

    # returns a list of all synonyms of a word (not grouped by definition)
    def getSynonyms(self, word):
        synsets = wn.synsets(word)
        if not synsets:
            return False
        
        synonyms = set()
        for syn in synsets:
            synonyms += set(lemma.name() for lemma in syn.lemmas())

        return synonyms
    

    # returns a list of all antonyms of a word (not grouped by definition)
    def getAntonyms(self, word):
        synsets = wn.synsets(word)
        if not synsets:
            return False
        
        antonyms = set()
        for syn in synsets:
            for lemma in syn.lemmas():
                antonyms += set(ant.name() for ant in lemma.antonyms())
        
        return antonyms
