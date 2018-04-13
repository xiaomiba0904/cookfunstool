from abc import ABC, abstractmethod


class Promotion(ABC):
    """策略抽象基类"""
    @abstractmethod
    def __call__(self, order):
        """返回折扣金额（正值）"""


class FidelityPromo(Promotion):
    """为积分为1000或以上的顾客提供5%折扣"""

    def __call__(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """单个商品为20个或以上时提供10%折扣"""

    def __call__(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):
    """订单中的不同商品达到10个以上是提供7%折扣"""

    def __call__(self, order):
        discount_items = {item.product for item in order.cart}
        if len(discount_items) >= 10:
            return order.total() * 0.07
        return 0

