class FlashCard:
    def __init__(self, french_word, english_word):
        self.french_word = french_word
        self.english_word = english_word
        self.has_been_learned = False

    def learned(self):
        self.has_been_learned = True

    def set_active(self, card):
        self = card
