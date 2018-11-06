import random
class Word:

    def __init__(self, db_file_name):
        try:
            db = open(db_file_name, 'r')
        except FileNotFoundError:
            print('file can\'t find')
            return

        lines = db.readlines()
        db.close()

        self.word_db = []
        self.count = len(lines)
        for line in lines:
            self.word_db.append(line.rstrip())


    def random_word(self):
        picker = random.randrange(self.count)
        return self.word_db[picker]