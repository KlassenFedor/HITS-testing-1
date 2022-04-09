import unittest
from work_with_db import *


class InsertData(unittest.TestCase):

    insert_value(2)

    def test_inserting_correct_data(self):
        answer = 'Successfully'
        self.assertEqual(answer, insert_value(5))

    def test_inserting_incorrect_data(self):
        answer = 'Wrong data'
        self.assertEqual(answer, insert_value('STR'))

    def test_get_existing_value(self):
        answer = 'a^2+2ab+b^2'
        self.assertEqual(answer, get_value(2))

    def test_get_nonexistent_value(self):
        answer = "Result for this number doesn't exists now"
        self.assertEqual(answer, get_value(3))
        