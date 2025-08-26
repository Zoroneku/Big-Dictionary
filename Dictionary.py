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
        
        synonyms = []
        for syn in synsets:
            synonyms.append(lemma.name() for lemma in syn.lemmas() if lemma.name() not in synonyms)

        return synonyms
    

    # returns a list of all antonyms of a word (not grouped by definition)
    def getAntonyms(self, word):
        synsets = wn.synsets(word)
        if not synsets:
            return False
        
        antonyms = []
        for syn in synsets:
            for lemma in syn.lemmas():
                antonyms.append(ant.name() for ant in lemma.antonyms() if ant.name() not in antonyms)
        
        return antonyms
