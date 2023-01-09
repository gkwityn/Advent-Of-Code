import unittest
from day8_pt1 import is_right_visible
from day8_pt1 import is_left_visible
from day8_pt1 import get_row
from day8_pt1 import get_col


class TestVisibleMethods(unittest.TestCase):

    matrix = [[1, 2, 3], 
              [4, 5, 6],
              [7, 8, 9]]

    def test_get_row(self):

        my_row = get_row(0, 0, self.matrix)
        self.assertEqual(my_row, [1, 2, 3])

        my_row = get_row(0, 1, self.matrix)
        self.assertEqual(my_row, [1, 2, 3])

        my_row = get_row(0, 2, self.matrix)
        self.assertEqual(my_row, [1, 2, 3])
        
        my_row = get_row(1, 0, self.matrix)
        self.assertEqual(my_row, [4, 5, 6])

        my_row = get_row(1, 0, self.matrix)
        self.assertEqual(my_row, [4, 5, 6])

        my_row = get_row(1, 1, self.matrix)
        self.assertEqual(my_row, [4, 5, 6])

        my_row = get_row(1, 2, self.matrix)
        self.assertEqual(my_row, [4, 5, 6])

        my_row = get_row(2, 0, self.matrix)
        self.assertEqual(my_row, [7, 8, 9])

        my_row = get_row(2, 1, self.matrix)
        self.assertEqual(my_row, [7, 8, 9])

        my_row = get_row(2, 2, self.matrix)
        self.assertEqual(my_row, [7, 8, 9])
        

    def test_get_col(self):

        my_col = get_col(0, 0, self.matrix)
        self.assertEqual(my_col, [1, 4, 7])

        my_col = get_col(1, 0, self.matrix)
        self.assertEqual(my_col, [1, 4, 7])

        my_col = get_col(2, 0, self.matrix)
        self.assertEqual(my_col, [1, 4, 7])
        
        my_col = get_col(0, 1, self.matrix)
        self.assertEqual(my_col, [2, 5, 8])

        my_col = get_col(1, 1, self.matrix)
        self.assertEqual(my_col, [2, 5, 8])

        my_col = get_col(2, 1, self.matrix)
        self.assertEqual(my_col, [2, 5, 8])

        my_col = get_col(0, 2, self.matrix)
        self.assertEqual(my_col, [3, 6, 9])

        my_col = get_col(1, 2, self.matrix)
        self.assertEqual(my_col, [3, 6, 9])

        my_col = get_col(2, 2, self.matrix)
        self.assertEqual(my_col, [3, 6, 9])

    def test_is_left_visible(self):
        line = [9, 0, 0, 0]
        index = 0
        result = is_left_visible(line, index)
        self.assertTrue(result)

        line = [1, 9, 0, 0]
        index = 1
        result = is_left_visible(line, index)
        self.assertTrue(result)

        line = [1, 1, 9, 0]
        index = 2
        result = is_left_visible(line, index)
        self.assertTrue(result)

        line = [1, 7, 8, 9]
        index = 2
        result = is_left_visible(line, index)
        self.assertTrue(result)

        #Test Failure
        line = [1, 9, 8, 0]
        index = 2
        result = is_left_visible(line, index)
        self.assertFalse(result)

        line = [1, 9, 8, 9]
        index = 2
        result = is_left_visible(line, index)
        self.assertFalse(result)

    def test_is_right_visible(self):
        line = [9, 0, 0, 0]
        index = 0
        result = is_right_visible(line, index)
        self.assertTrue(result)
        
        line = [0, 0, 0, 9]
        index = 3
        result = is_right_visible(line, index)
        self.assertTrue(result)

        line = [0, 9, 3, 1]
        index = 1
        result = is_right_visible(line, index)
        self.assertTrue(result)

        line = [0, 9, 9, 1]
        index = 2
        result = is_right_visible(line, index)
        self.assertTrue(result)
        

   


if __name__ == '__main__':
    unittest.main()
