"""Test cases"""

import unittest
import club_functions


class TestGetAverageClubCount(unittest.TestCase):
    """Test cases for function club_functions.get_average_club_count.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_odd_clubs(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', \
                                   'Rock N Rollers', 'Chess Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 3.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
        
    def test_01_one_person_no_clubs(self):
        param = {'Claire Dunphy': []}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_even_clubs(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', \
                                   'Rock N Rollers']}
        actual = club_functions.get_average_club_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
        
    def test_01_one_person_longer_even_clubs(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', \
                                   'Wizard of Oz Fan Club', 'Rock N Rollers', \
                                   'Smash Club', 'Comics R Us', 'Comet Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 6.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_longer_odd_clubs(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', \
                                   'Wizard of Oz Fan Club', 'Rock N Rollers', \
                                   'Smash Club', 'Comics R Us', 'Comet Club', \
                                   'Chess Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 7.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
        
    def test_01_even_people_both_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association'], 'Jack \
        Sparrow': ['Movie Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
        
    def test_01_even_people_odd_and_even_clubs(self):
        param = {'Claire Dunphy': ['Parent Teacher Association'], 'Jack \
        Sparrow': ['Movie Club', 'Chess Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg) 
        
    def test_01_odd_people_all_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association'], 'Jack \
        Sparrow': ['Movie Club'], 'Matt Hughes': ['Movie Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)        
        
    def test_01_odd_people_all_even_clubs(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', 'Chess Club'],\
                 'Jack Sparrow': ['Movie Club', 'Chess Club'], \
                 'Matt Hughes': ['Movie Club', 'Chess Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)          
        
        


if __name__ == '__main__':
    unittest.main(exit=False)
