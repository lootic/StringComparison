import unittest
from comparison_set import ComparisonSet

class ComparisonSetTest(unittest.TestCase):
    def test_add_element_check_if_is_contained(self):
        comparison_set = ComparisonSet()
        comparison_set.add('asd')
        self.assertTrue(comparison_set.contains('asd'))

    def test_add_two_elements_check_if_both_are_contained(self):
        comparison_set = ComparisonSet()
        comparison_set.add('asddasasd')
        comparison_set.add('asddsadas')
        self.assertTrue(comparison_set.contains('asddasasd'))
        self.assertTrue(comparison_set.contains('asddsadas'))

    def test_add_two_elements_check_if_substring_and_superstring_is_contained(self):
        comparison_set = ComparisonSet()
        comparison_set.add('asddasasd')
        comparison_set.add('asddsadas')
        print
        print comparison_set
        self.assertFalse(comparison_set.contains('asdd'))
        self.assertFalse(comparison_set.contains('asddsadass'))

    def test_add_single_string_find_common_prefix(self):
        comparison_set = ComparisonSet()
        comparison_set.add('asddasasd')

        self.assertEqual(comparison_set.common_prefix('asddafass'), 'asdda')
        self.assertEqual(comparison_set.common_prefix('asddasasddsads'), 'asddasasd')
        self.assertEqual(comparison_set.common_prefix('asdda'), 'asdda')
        self.assertEqual(comparison_set.common_prefix('fasfs'), '')

if __name__ == '__main__':
    unittest.main()
