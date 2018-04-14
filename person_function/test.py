from .date_processing import dedup
from .flatten import flatten
import unittest


class TestDedup(unittest.TestCase):

    def setUp(self):
        self.testlist = [1, 5, 2, 1, 9, 1, 5, 10]
        self.testlist_reslut = [1, 5, 2, 9, 10]
        self.testdict = [{'x': 1, 'y': 2},
                         {'x': 1, 'y': 3},
                         {'x': 1, 'y': 2},
                         {'x': 2, 'y': 4}]
        self.testdict_reslut = [{'x': 1, 'y': 2},
                                {'x': 1, 'y': 3},
                                {'x': 2, 'y': 4}]
        self.d = lambda d: (d['x'], d['y'])

    def tearDown(self):
        pass

    def test_dedup_list(self):
        self.assertEqual(list(dedup(self.testlist)), self.testlist_reslut)

    def test_dedup_dict(self):
        self.assertEqual(list(dedup(self.testdict, key=self.d)),
                         self.testdict_reslut)


class TestFlatten(unittest.TestCase):

    def setUp(self):
        self.testitems = [1,2,[3,4,[5,6],7],8]
        self.test_reslut = [1,2,3,4,5,6,7,8]

    def tearDown(self):
        pass

    def test_flatten(self):
        self.assertEqual(list(flatten(self.testitems)), self.test_reslut)
