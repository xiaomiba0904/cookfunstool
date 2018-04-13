import inspect
from . import promo

# 当前模块所有的策略子类
__all_promos = {cls for name, cls in inspect.getmembers(promo, inspect.isclass)
          if issubclass(cls , promo.Promotion)} - {promo.Promotion}
PROMOS = [promo() for promo in __all_promos]
