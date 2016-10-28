import unittest
import mostCommonLetters


class TestMostCommonLetters(unittest.TestCase):
    def test_first_input(self):
        text = "His name is Slim Shady!"

        expected = '''Most common letters:

S: 4 ####################
I: 3 ###############
A: 2 ##########
H: 2 ##########
M: 2 ##########
D: 1 #####
E: 1 #####
L: 1 #####
N: 1 #####
Y: 1 #####'''

        actual = mostCommonLetters.get_graphic_data(
            mostCommonLetters.compute_data(mostCommonLetters.collect_data(text)))

        self.assertEqual(expected, actual)

    def test_second_input(self):
        text = "aaaAaAAxAAaA"

        expected = '''Most common letters:

A: 11 ####################
X:  1 ##'''

        actual = mostCommonLetters.get_graphic_data(
            mostCommonLetters.compute_data(mostCommonLetters.collect_data(text)))

        self.assertEqual(expected, actual)

    def test_third_input(self):
        text = "cbad"

        expected = '''Most common letters:

A: 1 ####################
B: 1 ####################
C: 1 ####################
D: 1 ####################'''

        actual = mostCommonLetters.get_graphic_data(
            mostCommonLetters.compute_data(mostCommonLetters.collect_data(text)))

        self.assertEqual(expected, actual)

    def test_empty_string(self):
        text = ''

        with self.assertRaises(ValueError):
            mostCommonLetters.get_graphic_data(
                mostCommonLetters.compute_data(mostCommonLetters.collect_data(text)))

    def test_string_with_no_letters(self):
            text = '4995#$%*($38643*^'

            with self.assertRaises(ValueError):
                mostCommonLetters.get_graphic_data(
                    mostCommonLetters.compute_data(mostCommonLetters.collect_data(text)))

if __name__ == '__main__':
    unittest.main()