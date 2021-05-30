import numpy as np

class Matrix():
    def __init__(self):
        self.matrixes = {}
        self.currentWord = None
        self.coordl1 = None
        self.coordl2 = None


    def checkLangMatrix(self, lang):
        if lang in self.matrixes:
            return self.matrixes[lang]
        else:
            self.matrixes.update({lang: np.zeros((28,28),dtype=int)})
            return self.matrixes[lang]
    

    def updateLangMatrix (self, lang, matrix):
        self.matrixes.update({lang: matrix})


    def addLetters(self, lttrs:str):
        line = lttrs.strip()

        # parse the input we got from mapper.py
        m_split = lttrs.split(':')
        lang = m_split[0]
        word = m_split[1]

        matrix = self.checkLangMatrix(lang)

        if self.currentWord == word:
            matrix[self.coordl1][self.coordl2] += 1
        else:
            try:
                l1, l2 = list(word)
                if l1 == ' ':
                    l1 = '_'
                elif l2 == ' ':
                    l2 = '_'
            except ValueError:
                print('error', word)

            unil1, unil2 = ord(l1), ord(l2)
            # a-z gets 0-25 punctuation and spaces 26 everything else 27
            self.coordl1 = unil1 - 97 if unil1 >= 97 and unil1 <= 122 else 26 if unil1 < 97 else 27
            self.coordl2 = unil2 - 97 if unil2 >= 97 and unil2 <= 122 else 26 if unil2 < 97 else 27
            self.current_word = word
            matrix[self.coordl1][self.coordl2] += 1
        
        self.updateLangMatrix(lang, matrix)



    def saveAll(self):
        for lang in self.matrixes:
            np.savetxt(f'outputs/{lang}_matrix.np', self.matrixes[lang])