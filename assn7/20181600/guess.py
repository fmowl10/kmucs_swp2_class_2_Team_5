class Guess:

    def __init__(self, word):
        self.secret_word = word
        self.current_status = ('{:_^%d}' % len(word)).format('')
        self.num_tries = 0
        self.guessed_chars = []


    def display(self):
        current = 'Current: %s' % self.current_status
        tries = 'Tries: %d' % self.num_tries
        print(current + '\n' + tries)

    def guess(self, character):
        count = self.secret_word.count(character)
        self.guessed_chars.append(character)
        if count == 0:
            self.num_tries += 1
            return False
        idx = 0
        for _ in range(count):
            idx = self.secret_word.find(character, idx, len(self.secret_word))
            self.current_status = self.current_status[:idx] + \
                                character + self.current_status[idx + 1:]
            idx += 1
        if self.secret_word == self.current_status:
            return True