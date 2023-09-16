# singleton class, that allows the creation of the class object only once.
# we can achieve it by using __new__() magic method.
# __new__() checks the existence of the previous class instances cached on a class attribute.

class Singleton(object):
    _instance = None
    _max_count = 0

    # for limit it to only one count
    def __new__(cls, *args, **kwargs):
        cls._max_count += 1
        # The Singleton class in this example has a class attribute called ._instance that defaults to None
        # and works as a cache. The .__new__() method checks if no previous instance exists by testing
        # the condition cls._instance is None.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        # for limit, it upto max count
        elif cls._max_count < 5:
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            print("Warring max count reached.")

    def __init__(self):
        print("creating class object")

# Note: In the example above, Singleton doesn’t provide an implementation of .__init__().
# If you ever need a class like this with a .__init__() method, then keep in mind that
# this method will run every time you call the Singleton() constructor.
# This behavior can cause weird initialization effects and bugs.

# first __new__() will run every time and then __init__() is called if required. (based on conditions)


class TestMoney(object):
    def __init__(self):
        print("initializing class object")


if __name__ == "__main__":
    first = Singleton()
    second = Singleton()
    third = Singleton()
    fourth = Singleton()
    fifth = Singleton()
    sixth = Singleton()
    print(first==second)
    print(third==second)
    print(third==fourth)
    print(fourth==fifth)
    print(fifth==sixth)
    dummy = TestMoney()
    dummy2 = TestMoney()
