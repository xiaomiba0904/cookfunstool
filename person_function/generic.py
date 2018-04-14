# 根据singledispatch简化的多参数泛型装饰器
# 可以模仿实现Java的函数重载机制
from inspect import signature
from functools import update_wrapper


class MultiDispatch(object):
    """multi-dispatch generic decorator"""
    def __init__(self):
        self.registry = {}
        self.sign = None

    def _dispatch(self, cls):
        try:
            func = self.registry[cls]
        except KeyError:
            func = self.registry[object]
        return func

    def register(self, *cls, func=None):
        if func is None:
            return lambda f: self.register(*cls, func=f)
        if len(cls) != len(self.sign.parameters):
            raise TypeError('参数类型数量与函数参数数量不符')
        self.registry[cls] = func
        return func

    def __call__(self, func):
        self.registry[object] = func
        self.sign = signature(func)
        def wrapper(*args, **kwargs):
            cls = tuple(arg.__class__ for arg in args)
            return self._dispatch(cls)(*args, **kwargs)
        wrapper.register = self.register
        wrapper.dispatch = self._dispatch
        update_wrapper(wrapper, func)
        return wrapper

if __name__ == '__main__':
    dispatch = MultiDispatch()

    @dispatch
    def add(a, b):
        return a + b

    @dispatch.register(dict, dict)
    def _(a, b):
        import copy
        tmp = copy.deepcopy(a)
        tmp.update(b)
        return tmp

    objs = (
        (1, 2),
        ('a', 'b'),
        ([10,20], [30, 40]),
        ({"name":'jon'}, {'age': 18})
    )
    for obj in objs:
        print(add(*obj))




