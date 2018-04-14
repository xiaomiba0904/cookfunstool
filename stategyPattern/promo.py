from abc import ABC, abstractmethod

PROMOS = list()


class Promotion(ABC):
    """策略抽象基类"""
    @abstractmethod
    def __call__(self, order):
        """返回折扣金额（正值）"""

    def __str__(self):
        """优惠策略说明"""
        return 'Promotion<{}>'.format(self.__doc__)


def promotion_register(promo):
    """注册使用的策略装饰器"""
    if issubclass(promo, Promotion):
        PROMOS.append(promo())
    return promo


@promotion_register
class FidelityPromo(Promotion):
    """积分为1000或以上的顾客提供5%折扣"""

    def __call__(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


@promotion_register
class BulkItemPromo(Promotion):
    """单个商品为20个或以上时提供10%折扣"""

    def __call__(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


@promotion_register
class LargeOrderPromo(Promotion):
    """订单中的不同商品达到10个以上是提供7%折扣"""

    def __call__(self, order):
        discount_items = {item.product for item in order.cart}
        if len(discount_items) >= 10:
            return order.total() * 0.07
        return 0
