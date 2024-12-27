import pytest


class TestDome:

    def test_01(self):
        print('----测试用例：test_01------')

    def test_02(self):
        print('----测试用例：test_02------')

    def setup_method(self):
        print("测试执行前的数据")
    # def setup_method(function):
    #     print("测试用例前置方法---setup_method---")

    def teardown_method(self):
        print("测试用例后置方法---teardown_method---")


    def setup_class(self):
        print("testdome类执行前准备的数据")



    def teardown_class(self):
        print("testdome类执行后删除的数据")