import markovify
import sys
from os.path import isfile, join
from getFiles import getFiles


class markovBot:
    # Class to generate sentences of text given a single .txt file or a folder full of .txt files.

    dirname = ""
    modelList = []
    charLim = 140

    def __init__(self, dirname):
        # Initialize markov chain models 

        self.dirname = dirname

        # For the case where the directory name is a folder.
        if not isfile(self.dirname):
            fileList = getFiles(self.dirname)

            for fileName in fileList:
                with open(join(self.dirname, fileName)) as f:
                    text = f.read()

                text_model = markovify.Text(text)
                self.modelList.append(text_model)

            self.model_combo = markovify.combine(self.modelList)

        # Else, assume it's a single valid.txt file. 
        else:
            with open(self.dirname) as f:
                text = f.read()

            self.model_combo = markovify.Text(text)

    # generate num numbers of sentences of text.
    def generate_text(self, num):
        result = []
        for i in range(num):
            text = self.model_combo.make_sentence()
            while (not text):
                text = model_combo.make_sentence()

            if len(result) + len(text) < self.charLim:
                result.append(text)

        return result

