import unittest
from .promo import *
from .pattern import *


class TestPattern(unittest.TestCase):

    def setUp(self):
        self.client_1 = Customer('小明', 0)
        self.client_2 = Customer('小红', 1100)

    def test_fidelityPromo(self):
        cart = [LineItem('香蕉', 4, 0.5),
                LineItem('苹果', 10, 1.5),
                LineItem('草莓', 5, 5.0)]

        order1 = Order(self.client_1, cart, FidelityPromo())
        self.assertEqual(order1.total(), order1.due())

        order2 = Order(self.client_2, cart, FidelityPromo())
        self.assertEqual(order2.total() * (1 - 0.05), order2.due())

    def test_bulkItemPromo(self):
        cart = [
            LineItem('香蕉', 30, 0.5),
            LineItem('苹果', 10, 1.5)
        ]
        order = Order(self.client_1, cart, BulkItemPromo())
        self.assertEqual(order.total(), order.due() + cart[0].total() * 0.1)

    def test_largeOrderPromo(self):
        cart = [LineItem(str(item_code), 1, 1.0)
                for item_code in range(10)]
        order = Order(self.client_1, cart, LargeOrderPromo())
        self.assertEqual(order.total(), order.due() + 0.7)

    def test_all_promo(self):
        cart = [LineItem('香蕉', 4, 0.5),
                LineItem('苹果', 20, 1.5),
                LineItem('草莓', 5, 5.0)]
        order = Order(self.client_2, cart, FidelityPromo())
        self.assertTrue(order.all_promo() >= order.base_promo() >= order.designate_promo())