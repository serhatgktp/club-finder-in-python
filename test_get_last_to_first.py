"""Test Cases"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_different_last(self):
        param = {'Clare Dunphy': ['Phil Carter']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Carter': ['Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_more_friends_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy', 'Jeff Dunphy', 'Bill Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Bill', 'Clare', 'Jeff', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_more_friends_different_last(self):
        param = {'Clare Dunphy': ['Phil Carter', 'Jeff Bezos', 'Bill Gates']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Carter': ['Phil'], 'Bezos': ['Jeff'],\
                    'Gates': ['Bill']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_01_more_persons_no_friends_same_last(self):
        param = {'Clare Dunphy': [], 'Bill Dunphy': [], 'Jeff Dunphy': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Bill', 'Clare', 'Jeff']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
    def test_01_more_persons_no_friends_different_last(self):
        param = {'Clare Dunphy': [], 'Bill Gates': [], 'Jeff Bezos': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Gates': ['Bill'], 'Bezos': ['Jeff']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)            

    def test_01_more_persons_one_friend_different_last(self):
        param = {'Clare Dunphy': ['Elon Musk'],\
                 'Bill Gates': ['Hugh Jackman'], \
                 'Jeff Bezos': ['Jared Leto']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Gates': ['Bill'], 'Bezos': ['Jeff'], \
                    'Jackman': ['Hugh'], 'Musk': ['Elon'], 'Leto': ['Jared']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
    def test_01_more_persons_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Elon Dunphy'], \
                 'Bill Gates': ['Hugh Gates'], \
                 'Jeff Bezos': ['Jared Bezos']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Elon'], \
                    'Gates': ['Bill', 'Hugh'], 'Bezos': ['Jared', 'Jeff']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)            
        
    def test_01_more_persons_more_friends_mixed_last(self):
        param = {'Clare Dunphy': ['Elon Musk', 'Elena Jackman'],\
                 'Bill Gates': ['Hugh Jackman', 'Vivaldi Musk'], \
                 'Jeff Bezos': ['Jared Leto', 'Aaron Leto']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Gates': ['Bill'], 'Bezos': ['Jeff'], \
                    'Jackman': ['Elena', 'Hugh'], 'Musk': ['Elon', 'Vivaldi'], \
                    'Leto': ['Aaron','Jared']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    


if __name__ == '__main__':
    unittest.main(exit=False)
