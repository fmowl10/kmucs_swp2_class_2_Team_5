class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.answerBlank = []
        for j in range(len(self.secretWord)):
            self.answerBlank.append('_')


    def display(self):
        print('Current: ', ''.join(self.answerBlank))
        print('Tries: ', self.numTries)


    def guess(self, character):
        self.guessedChars += character
        n = self.secretWord.find(character)

        if n == -1:
            self.numTries += 1
        else:
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    self.answerBlank[i] = character

        if self.secretWord == ''.join(self.answerBlank):
            return True
        else:
            self.currentStatus = ''.join(self.answerBlank)
            return False