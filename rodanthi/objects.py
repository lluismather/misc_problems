import nltk
import text

class objects:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.text = nltk.corpus.gutenberg.words('austen-emma.txt')
        self.display_text = None
        self.counter = 0
        self.word_count = 600
        self.update()

    def update(self):
        self.display_text = ' '.join(self.text[self.counter:self.counter + self.word_count])
