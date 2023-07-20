# OSU CS 362 Summer 2023
# Assignment: HW1
# Student Name: Anthony Wu
# Sutdnet ID: wuant


import unittest
from credit_card_validator import credit_card_validator


class TestCreditCard(unittest.TestCase):
    def test1(self):
        """Verifies input of all zeros rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("0000000000000000"))

    def test2(self):
        """Verifies input with prefix of 1 rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("1000000000000000"))

    def test3(self):
        """Verifies input of empty string rejected
        returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator(""))

    def test4(self):
        """Verifies input of 15 digits with prefix 4 rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("400000000000006"))

    def test5(self):
        """Verifies input of 16 digits with prefix of 34 rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("3400000000000000"))

    def test6(self):
        """Verifies input for visa shorther than 16 rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("400000000000006"))

    def test7(self):
        """Verifies valid lengths and check bits for visa accepted
        returns True
        Picked using Category Partition Testing"""
        self.assertTrue(credit_card_validator("4000000000000002"))

    def test8(self):
        """Verifies valid lengths but invalid check bits for visa rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("4000000000000000"))

    def test9(self):
        """Verifies invalid longer length for visa rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("40000000000000006"))

    def test10(self):
        """Verifies input for mastercard shoter than 16 rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("540000000000007"))

    def test11(self):
        """Verifies mastercard with valid lengths and check bits accepted
        returns True
        Picked using Category Partition Testing"""
        self.assertTrue(credit_card_validator("5400000000000005"))

    def test12(self):
        """Verifies mastercard with valid length/invalid check bits rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("5400000000000000"))

    def test13(self):
        """Verifies mastercard longer than 16 rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("54000000000000007"))

    def test14(self):
        """Verifies input for mastercard shoter than 16 rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("222100000000000"))

    def test15(self):
        """Verifies mastercard with valid lengths and check bits accepted
        returns True
        Picked using Category Partition Testing"""
        self.assertTrue(credit_card_validator("2221000000000009"))

    def test16(self):
        """Verifies mastercard with valid length/invalid check bits rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("2221000000000000"))

    def test17(self):
        """Verifies mastercard longer than 16 rejected
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("22210000000000009"))

    def test18(self):
        """Verifies input for amex shoter than 15 rejected
        returns False
        Picked using Category Partition Testing"""
        print(unittest.TestCase)
        self.assertFalse(credit_card_validator("34000000000000"))

    def test19(self):
        """Verifies amex with valid lengths and check bits accepted
        returns True
        Picked using Category Partition Testing"""
        print(unittest.TestCase)
        self.assertTrue(credit_card_validator("340000000000009"))

    def test20(self):
        """Verifies amex with valid length but invalid check bits rejected
        returns False
        Picked using Category Partition Testing"""
        print(unittest.TestCase)
        self.assertFalse(credit_card_validator("340000000000000"))

    def test21(self):
        """Verifies amex longer than 15 rejected
        returns False
        Picked using Category Partition Testing"""
        print(unittest.TestCase)
        self.assertFalse(credit_card_validator("3400000000000000"))

    def test22(self):
        """Verifies input for amex shoter than 15 rejected
        returns False
        Picked using Category Partition Testing"""
        print(unittest.TestCase)
        self.assertFalse(credit_card_validator("37000000000009"))

    def test23(self):
        """Verifies amex with valid lengths and check bits accepted
        returns True
        Picked using Category Partition Testing"""
        print(unittest.TestCase)
        self.assertTrue(credit_card_validator("370000000000002"))

    def test24(self):
        """Verifies amex with valid length but invalid check bits rejected
        returns False
        Picked using Category Partition Testing"""
        print(unittest.TestCase)
        self.assertFalse(credit_card_validator("370000000000000"))

    def test25(self):
        """Verifies amex longer than 15 rejected
        returns False
        Picked using Category Partition Testing"""
        print(unittest.TestCase)
        self.assertFalse(credit_card_validator("3700000000000007"))

    def test26(self):
        """Verifies mastercard with wrong prefix rejected
        returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("2220000000000000"))

    def test27(self):
        """Verifies mastercard with wrong prefix rejected
        returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("2100000000000000"))

    def test28(self):
        """Verifies mastercard with wrong prefix rejected
        returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("2800000000000000"))

    def test29(self):
        """Verifies mastercard with wrong prefix rejected
        returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("2900000000000000"))

    def test30(self):
        """Verifies mastercard with valid prefix/invalid check bits rejected
        returns False
        Picked using Boundary Testing"""
        self.assertFalse(credit_card_validator("2721000000000004"))

    def test31(self):
        """Verifies visa with valid length and invalid check bits rejected
        returns False
        Picked using Boundary Testing"""
        self.assertFalse(credit_card_validator("49999999999999967"))

    def test32(self):
        """Verifies amex with valid lengths and invalid check bits rejected
        returns False
        Picked using Boundary Testing"""
        self.assertFalse(credit_card_validator("340000000000008"))

    def test33(self):
        """Verifies input with prefix of 1 rejected
        returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("1000000000000008"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
