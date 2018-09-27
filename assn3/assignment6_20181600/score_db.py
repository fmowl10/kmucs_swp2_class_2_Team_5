"""
    this module written by kim jinseok
"""

import pickle

class ScoreDB:
    """
        ScoreDB manage data
    """
    ColumnName = ['Name', 'Age', 'Score']

    def __init__(self, file_name):
        self.file_name = file_name
        self.db = []

    def read(self):
        try:
            fH = open(self.file_name, 'rb')
        except FileNotFoundError:
            self.db = []
            return

        try:
            self.db =  pickle.load(fH)
        except pickle.PickleError:
            self.db = []
        fH.close()

    def write(self):
        fH = open(self.file_name, 'wb')
        pickle.dump(self.db, fH)
        fH.close()

    def add_record(self, name, age='0', score='0'):
        """
            add_record method add score data

            when method returns False
                name is None or its type is not str returns False
                age or score's can't convert to int
        """

        # age and score can be blank. but name can't
        if not isinstance(name, str) or name is None:
            return False

        try:
            record = {'Name': name, 'Age': int(age), 'Score': int(score)}
        except ValueError:
            return False

        self.db.append(record)
        return True

    def find(self, name):
        """
            find method get name whitch callee want to find
            returns list of record (name not exist in db than retuns empty list)

            when method returns None
                if method get wrong value than it returns None
        """
        if name is None or not isinstance(name, str):
            return None

        temp_db = []

        for record in self.db:
            if record['Name'] == name:
                temp_db.append(record)
        return temp_db

    def inc(self, name, amount):
        """
            inc method get name and amount and add amount to name's score
            lastly method returns True or False
            when method returns False
                get blank name or amount can't convert to int
                name not exitst in db
        """

        if name is None or not isinstance(name, str):
            return False

        for record in self.db:
            if record['Name'] == name:
                try:
                    record['Score'] += int(amount)
                except ValueError:
                    return False

    def del_record(self, name):
        """
            del_reocrd method get name which callee want to delete
            delete all record which Name is equle to 'name'
        """

        if name is None or not isinstance(name, str):
            return False
        self.db = [record for record in self.db if record['Name'] != name]
        return True

    def show(self, key_name):
        """
            show method get key and return sorted by key
            if got wrong argument then returns None
        """

        #type check first and logic
        if not isinstance(key_name, str) or not key_name in ScoreDB.ColumnName:
            return  None

        list_sorted = sorted(self.db, key=lambda person: person[key_name])
        return list_sorted
