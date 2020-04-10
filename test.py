import unittest
from sum import my_sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        '''
        Tests that it can sum a list of integers
        '''
        self.assertEqual(my_sum([1, 2, 3]), 6, 'Should be 6')

    def test_single_list(self):
        '''
        Tests that it works with list of one item
        '''
        self.assertEqual(my_sum([1]), 1, 'Should be 1')

    def test_tuple(self):
        '''
        Tests that it can sum a tuple
        '''
        self.assertEqual(my_sum((1, 2, 2)), 5, 'Should be 5')

    def test_bad_type(self):
        '''
        Tests that sum raises errors with bad inputs
        '''
        data = 'banana'
        with self.assertRaises(TypeError):
            result = my_sum(data)


if __name__ == '__main__':
    unittest.main()
