import unittest
from main import *


class AllSteps(unittest.TestCase):

    # positive tests:

    def test_doing_all_steps_by_int(self):
        answer = 'a+b'
        self.assertEqual(answer, do_all_steps(1))

    def test_doing_all_steps_by_int_bigger_than_1(self):
        answer = 'a^3+3a^2b+3ab^2+b^3'
        self.assertEqual(answer, do_all_steps(3))

    def test_doing_all_steps_by_biggest_possible_int(self):
        # answer too long, therefore it located in separated file
        file = open('./degree200.txt', 'r')
        answer = file.readline()
        file.close()
        self.assertEqual(answer, do_all_steps(200))

    def test_doing_all_steps_by_negative_int(self):
        answer = 'a+b'
        self.assertEqual(answer, do_all_steps(-1))

    def test_doing_all_steps_by_negative_int_less_than_1(self):
        answer = 'a^3+3a^2b+3ab^2+b^3'
        self.assertEqual(answer, do_all_steps(-3))

    def test_doing_all_steps_by_smallest_possible_int(self):
        # answer too long, therefore it located in separated file
        file = open('./degree200.txt', 'r')
        answer = file.readline()
        file.close()
        self.assertEqual(answer, do_all_steps(-200))

    def test_doing_all_steps_by_hex(self):
        answer = 'a^2+2ab+b^2'
        self.assertEqual(answer, do_all_steps(0x2))

    # negative tests

    def test_doing_all_steps_by_zero_raise_exception(self):
        with self.assertRaises(ValueError):
            do_all_steps(0)

    def test_doing_all_steps_by_string_raise_exception(self):
        with self.assertRaises(ValueError):
            do_all_steps('string')

    def test_doing_all_steps_by_list_raise_exception(self):
        with self.assertRaises(ValueError):
            do_all_steps([1, 2])

    def test_doing_all_steps_by_float_raise_exception(self):
        with self.assertRaises(ValueError):
            do_all_steps(2.1)

    def test_doing_all_steps_by_int_bigger_than_200(self):
        with self.assertRaises(ValueError):
            do_all_steps(201)

    def test_doing_all_steps_by_int_less_than_minus_200(self):
        with self.assertRaises(ValueError):
            do_all_steps(-201)


class Formula(unittest.TestCase):

    # positive tests:

    def test_doing_formula_by_zero(self):
        answer = '1'
        self.assertEqual(answer, formula(0))

    def test_doing_formula_by_int(self):
        answer = 'a+b'
        self.assertEqual(answer, formula(1))

    def test_doing_formula_by_int_bigger_than_1(self):
        answer = 'a^3+3a^2b+3ab^2+b^3'
        self.assertEqual(answer, formula(3))

    def test_doing_formula_by_biggest_possible_int(self):
        # answer too long, therefore it located in separated file
        file = open('./degree200.txt', 'r')
        answer = file.readline()
        file.close()
        self.assertEqual(answer, formula(200))

    def test_doing_formula_by_negative_int(self):
        answer = '1/(a+b)'
        self.assertEqual(answer, formula(-1))

    def test_doing_formula_by_negative_int_less_than_1(self):
        answer = '1/(a^3+3a^2b+3ab^2+b^3)'
        self.assertEqual(answer, formula(-3))

    def test_doing_formula_by_smallest_possible_int(self):
        # answer too long, therefore it located in separated file
        file = open('./degree200.txt', 'r')
        answer = '1/(' + file.readline() + ')'
        file.close()
        self.assertEqual(answer, formula(-200))

    def test_doing_formula_by_hex(self):
        answer = 'a^2+2ab+b^2'
        self.assertEqual(answer, formula(0x2))

    # negative tests

    def test_doing_formula_by_string_raise_exception(self):
        with self.assertRaises(ValueError):
            formula('string')

    def test_doing_formula_by_list_raise_exception(self):
        with self.assertRaises(ValueError):
            formula([1, 2])

    def test_doing_formula_by_float_raise_exception(self):
        with self.assertRaises(ValueError):
            formula(2.1)

    def test_doing_formula_by_int_bigger_than_200(self):
        with self.assertRaises(ValueError):
            formula(201)

    def test_doing_formula_by_int_less_than_minus_200(self):
        with self.assertRaises(ValueError):
            formula(-201)


class StringByDegreeNumbersAndRatio(unittest.TestCase):
    # positive tests:

    def test_doing_string_by_degree_of_numbers_and_ratio_by_integers(self):
        answer = '2ab'
        self.assertEqual(answer, get_new_string_by_degree_a_b_and_ratio(1, 1, 2))

    def test_doing_string_by_degree_of_numbers_and_ratio_by_zero_ratio(self):
        answer = ''
        self.assertEqual(answer, get_new_string_by_degree_a_b_and_ratio(1, 1, 0))

    def test_doing_string_by_degree_of_numbers_and_ratio_by_int_bigger_than_1(self):
        answer = '2a^2b^3'
        self.assertEqual(answer, get_new_string_by_degree_a_b_and_ratio(2, 3, 2))

    def test_doing_string_by_degree_of_numbers_and_ratio_by_hex_first_number(self):
        answer = '2a^2b^3'
        self.assertEqual(answer, get_new_string_by_degree_a_b_and_ratio(0x2, 3, 2))

    def test_doing_string_by_degree_of_numbers_and_ratio_by_hex_second_number(self):
        answer = '2a^2b^3'
        self.assertEqual(answer, get_new_string_by_degree_a_b_and_ratio(2, 0x3, 2))

    def test_doing_string_by_degree_of_numbers_and_ratio_by_hex_ratio(self):
        answer = '2a^2b^3'
        self.assertEqual(answer, get_new_string_by_degree_a_b_and_ratio(2, 3, 0x2))

    # negative tests

    def test_doing_string_by_degree_of_numbers_and_ratio_by_negative_first_number_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio(-2, 3, 2)

    def test_doing_string_by_degree_of_numbers_and_ratio_by_negative_second_number_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio(2, -3, 2)

    def test_doing_string_by_degree_of_numbers_and_ratio_by_negative_ratio_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio(2, 3, -2)

    def test_doing_string_by_degree_of_numbers_and_ratio_by_string_first_number_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio('2', 3, 2)

    def test_doing_string_by_degree_of_numbers_and_ratio_by_string_second_number_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio(2, '3', 2)

    def test_doing_string_by_degree_of_numbers_and_ratio_by_string_ratio_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio(2, 3, '2')

    def test_doing_string_by_degree_of_numbers_and_ratio_by_list_first_number_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio([2, 1], 3, 2)

    def test_doing_string_by_degree_of_numbers_and_ratio_by_list_second_number_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio(2, [2, 1], 2)

    def test_doing_string_by_degree_of_numbers_and_ratio_by_list_ratio_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio(2, 3, [2, 1])

    def test_doing_string_by_degree_of_numbers_and_ratio_by_float_first_number_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio(2.1, 3, 2)

    def test_doing_string_by_degree_of_numbers_and_ratio_by_float_second_number_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio(2, 3.1, 2)

    def test_doing_string_by_degree_of_numbers_and_ratio_by_float_ratio_raise_exception(self):
        with self.assertRaises(ValueError):
            get_new_string_by_degree_a_b_and_ratio(2, 3, 2.1)
