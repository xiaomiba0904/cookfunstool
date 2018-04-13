from collections import namedtuple
from fluentPython.strategPattern import PROMOS

Customer = namedtuple('Customer', 'name fidelity')


class LineItem(object):
    """商品"""

    def __init__(self, product, quantity, price):
        """
        :param product: 产品名称
        :param quantity: 数量
        :param price: 单价
        """
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order(object):
    """上下文"""
    def __init__(self, customer, cart, promotion=None):
        """
        :param customer: 顾客
        :param cart: 购物车
        :param promotion: 折扣策略
        """
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion


    def total(self):
        return sum(item.total() for item in self.cart)


    def designate_promo(self):
        """指定折扣"""
        if self.promotion is None:
            return 0
        else:
            return self.promotion(self)

    def base_promo(self):
        """最佳折扣策略"""
        return max(promo(self) for promo in PROMOS)

    def all_promo(self):
        """所有折扣总和"""
        return sum(promo(self) for promo in PROMOS)

    def due(self):
        if self.promotion is not None:
            return self.total() - self.designate_promo()
        max_promo = max(self.designate_promo(), self.base_promo(), self.all_promo())
        return self.total() - max_promo

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}'
        return fmt.format(self.total(), self.due())

