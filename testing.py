import unittest
from flag import ArgumentError, verification, flag


class ExceptionTestCase(unittest.TestCase):

    def test_invalid_type(self):
        self.assertRaises(ArgumentError, verification, 'abc')

    def test_negative_number(self):
        self.assertRaises(ArgumentError, verification, -1)

    def test_odd_number(self):
        self.assertRaises(ArgumentError, verification, 3)


class FlagsTestCase(unittest.TestCase):

    def test_flag_0(self):
        self.assertEqual(flag(0), '##\n'
                                  '##')

    def test_flag_2(self):
        self.assertEqual(flag(2), '########\n'
                                  '#      #\n'
                                  '#  **  #\n'
                                  '#  **  #\n'
                                  '#      #\n'
                                  '########')

    def test_flag_4(self):
        self.assertEqual(flag(4), '##############\n'
                                  '#            #\n'
                                  '#            #\n'
                                  '#     **     #\n'
                                  '#    *oo*    #\n'
                                  '#    *oo*    #\n'
                                  '#     **     #\n'
                                  '#            #\n'
                                  '#            #\n'
                                  '##############')

    def test_flag_6(self):
        self.assertEqual(flag(6), '####################\n'
                                  '#                  #\n'
                                  '#                  #\n'
                                  '#                  #\n'
                                  '#        **        #\n'
                                  '#       *oo*       #\n'
                                  '#      *oooo*      #\n'
                                  '#      *oooo*      #\n'
                                  '#       *oo*       #\n'
                                  '#        **        #\n'
                                  '#                  #\n'
                                  '#                  #\n'
                                  '#                  #\n'
                                  '####################')
