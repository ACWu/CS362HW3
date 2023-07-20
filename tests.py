# OSU CS 362 Summer 2023
# Assignment: HW3
# Student Name: Anthony Wu
# Sutdnet ID: wuant


from credit_card_validator import credit_card_validator
import random
import string
import unittest

class TestCase(unittest.TestCase):
    def generate_testcases(tests_to_generate=1000):
        """Verifies input of all zeros rejected
        returns False
        Picked using Category Partition Testing"""

        # Generate random test cases
        for i in range(tests_to_generate):

            #Generate credit card numbers
            cardnum = generate_cardnum()

            #Build test function
            message = 'Test Case: {}, Expected: {}, Result: {}'
            new_test = build_test_func(expected, cardnum, check_pwd, message)
            setattr(TestCase, 'test_{}'.format(cardnum), new_test)

    def generate_cardnum(self, prefix):
        return str(random.randint(99999999999999, 9999999999999999))

if __name__ == '__main__':
    unittest.main(verbosity=2)
