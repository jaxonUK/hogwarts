"""
__author__ = 'jaxon'
__time__ = '2020/6/4 5:33 下午'
"""
from appium.webdriver.common.mobileby import MobileBy


def ex(fu):
    def hello():
        print("hello")
        fu()
        print("good")
    return hello
@ex
def tmp():
    print("tom")

def aa():
    a = (1)
    b = []
    try:
        if isinstance(a, tuple):
            b = [1, 2]
            print('111')
        else:
            b = []
            if len(b) > 0:
                print('112111', b)
                return b,('8888')
            else:
                raise Exception
    except Exception as e:
        print('pppp')

def bb(func):
    a = [1]
    print(func.__name__)
    return len(a) < 0

@bb
def cc():
    return "111"

if __name__ == '__main__':
    # ex(tmp)()
    # tmp()
    # print(aa())
    pass
