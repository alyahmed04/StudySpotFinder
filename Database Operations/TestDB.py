import mysql.connector

config = {
  'user': 'placeholder',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'studyspot',
  'raise_on_warnings': True
}

class TestDB:
    def __init__ (self):
        self.create_test_table()
    def create_test_table(self):
        pass
        #intentionally blank
        #create a test table with preset values for use in test cases
    def __del__(self):
        self.drop_test_table()
    def drop_test_table(self):
        #deletes the test table after the testing is complete
        #intentially blank
        pass
