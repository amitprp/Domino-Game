from unittest import TestCase
from Collection import Collection



class TestCollection(TestCase):
    def setUp(self):
        self.c1_check = Collection([3, 'Domino', 1])
        self.c2_check = Collection(['Domino', 3, 1])
        self.c3_check = Collection([3, 'Domino', 1])

    def test_get_collection(self):
        self.assertEqual([3, 'Domino', 1], self.c1_check.get_collection(), msg='get_collection_func: Error in getting '
                                                                               'collection')

    def test_add(self):
        self.assertRaises(NotImplementedError, Collection.add, [], 2, 3)

    def test__get_item__(self):
        self.assertEqual(1, self.c1_check[2], msg="Error in get item function")
        self.assertEqual(None, self.c1_check[3], msg="get_item: Error in None requirment")
        self.assertEqual(None, self.c1_check[-1], msg="get_item: Error in None requirment")

    def test__eq__(self):
        self.assertTrue(self.c1_check == self.c3_check, msg="eq_func: Error in True value")
        self.assertFalse(self.c1_check == self.c2_check, msg="eq_func:Error in False value")

    def test__ne__(self):
        self.assertFalse(self.c1_check != self.c3_check, msg="eq_func: Error in False value")
        self.assertTrue(self.c1_check != self.c2_check, msg="eq_func: Error in True value")

    def test__len__(self):
        self.assertEqual(3, len(self.c1_check), msg="len_func: Error in length")

    def test__contains__(self):
        self.assertTrue('Domino' in self.c1_check, msg="contains_func: Error, not contains when contains")
        self.assertFalse(2 in self.c1_check, msg="contains_func: Error, contains when not contains")

    def test__str__(self):
        self.assertEqual('3Domino1', str(self.c1_check), msg="str_func: Error in making a string")

    def test__repr__(self):
        self.assertTrue(str(self.c1_check) == self.c1_check.__repr__())


