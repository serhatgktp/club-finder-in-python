"""A checker for types of functions in club_functions.py"""

import io
import unittest
import checker_generic
import club_functions as cf

TIMEOUT = 5


class CheckTest(unittest.TestCase):
    """Sanity checker for assignment functions."""

    def setUp(self):
        self.sample_file = io.StringIO('''Pritchett, Jay
Pritchett, Gloria
Delgado, Manny
Dunphy, Claire

Dunphy, Claire
Parent Teacher Association
Dunphy, Phil
Pritchett, Mitchell
Pritchett, Jay
''')
        self.p2f = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                                         'Rebecca Donaldson-Katsopolis'],
                    'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
                    'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
                    'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                                       'Joey Gladstone']}

        self.p2c = {'Michelle Tanner': ['Comet Club'],
                    'Danny R Tanner': ['Parent Council'],
                    'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
                    'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
                    'Joey Gladstone': ['Comics R Us', 'Parent Council']}

    def test00LoadProfiles(self):
        """Function load_profiles."""

        print('\nChecking load_profiles...')

        result = checker_generic.type_check_simple(
            cf.load_profiles, [self.sample_file], tuple)
        self.assertTrue(result[0], result[1])

        error_message = checker_generic.type_error_message(
            'load_profiles',
            'Tuple[Dict[str, List[str]], Dict[str, List[str]]]',
            result)

        self.assertTrue(isinstance(result[1], tuple), error_message)
        self.assertTrue(len(result[1]) == 2,
                        "load_profiles should return a 2-item tuple")

        self._is_dict_of_Ks_to_list_Vs(
            result[1][0], str, str,
            'load_profiles should return a 2-item tuple, and the first item'
            ' should be of type Dict[str, List[str]]')

        self._is_dict_of_Ks_to_list_Vs(
            result[1][1], str, str,
            'load_profiles should return a 2-item tuple, and the second item'
            ' should be of type Dict[str, List[str]]')

        print('  check complete')

    def test01GetAverageClubCount(self):
        """Function get_average_club_count."""

        self._check_simple_type(
            cf.get_average_club_count,
            [{'Jen Campbell': ['CS Profs']}],
            float)

    def test02GetLastToFirst(self):
        """Function get_last_to_first."""

        print('\nChecking get_last_to_first...')

        result = checker_generic.type_check_simple(
            cf.get_last_to_first, [self.p2f], dict)
        self.assertTrue(result[0], result[1])

        error_msg = 'get_last_to_first should return a Dict[str, List[str]]'

        self._is_dict_of_Ks_to_list_Vs(result[1], str, str, error_msg)

        print('  check complete')

    def test03InvertAndSort(self):
        """Function invert_and_sort."""

        print('\nChecking invert_and_sort...')

        result = checker_generic.type_check_simple(
            cf.invert_and_sort, [self.p2c], dict)
        self.assertTrue(result[0], result[1])

        for value in result[1].values():
            self.assertTrue(
                isinstance(value, list),
                'invert_and_sort should return a Dict[object, list].')

        print('  check complete')

    def test04GetClubsOfFriends(self):
        """Function get_clubs_of_friends."""

        print('\nChecking get_clubs_of_friends...')

        self._check_list_of_Ts(
            cf.get_clubs_of_friends,
            [self.p2f, self.p2c, 'Stephanie J Tanner'],
            str)

        print('  check complete')

    def test05RecommendClubs(self):
        """Function recommend_clubs."""
        print('\nChecking recommend_clubs...')

        result = self._check_list_of_Ts(
            cf.recommend_clubs,
            [self.p2f, self.p2c, 'Jesse Katsopolis'],
            tuple)

        msg = 'recommend clubs should return List[Tuple[str, int]'

        for item in result[1]:
            self.assertTrue(len(item) == 2, msg)
            self.assertTrue(isinstance(item[0], str), msg)
            self.assertTrue(isinstance(item[1], int), msg)

        print('  check complete')

    def _check_simple_type(self, func: callable, args: list, ret_type: type):
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.

        """

        print('\nChecking {}...'.format(func.__name__))
        result = checker_generic.type_check_simple(func, args, ret_type)
        self.assertTrue(result[0], result[1])
        print('  check complete')

    def _check_list_of_Ts(self, func: callable, args: list, ret_type: type):
        """Check that func called with arguments args returns a value of type
        ret_type.

        """

        result = checker_generic.returns_list_of_Ts(func, args, ret_type)
        self.assertTrue(result[0], result[1])
        return result

    def _is_dict_of_Ks_to_list_Vs(self, result: object, key_tp: type,
                                  val_tp: type, msg: str):
        """Check if result is a dict with keys of type key_tp and values
         of type list that are non-empty and with elements of type val_tp.

        """

        self.assertTrue(isinstance(result, dict), msg)

        for (key, val) in result.items():
            self.assertTrue(isinstance(key, key_tp), msg)
            self.assertTrue(isinstance(val, list), msg)
            # self.assertTrue(val != [],
            # msg + ' and the values should be non-empty lists')
            for item in val:
                self.assertTrue(isinstance(item, val_tp), msg)


checker_generic.ensure_no_io('club_functions')
TARGET_LEN = 79
print(''.center(TARGET_LEN, "="))
print(' Start: checking coding style '.center(TARGET_LEN, "="))
checker_generic.run_pyta('club_functions.py', 'pyta/a3_pyta.txt')
print(' End checking coding style '.center(TARGET_LEN, "="))

print(' Start: checking type contracts '.center(TARGET_LEN, "="))
unittest.main(exit=False)
print(' End checking type contracts '.center(TARGET_LEN, "="))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style')
print('  - checking type contract\n')
