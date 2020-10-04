#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试文件

import pytest
import sys

import yaml

print(sys.path.append('..'))
from  pythoncode.calc import Calculator

# 模块级别
def setup_module():
    print('模块级别setup')

def teardown_module():
    print('模块级别teardown')

# 函数级别 类外面的使用def定义的叫做函数
# 在类里面使用def定义的叫方法
def setup_function():
    print('函数级别setup')

def teardown_function():
    print('函数级别 teardown')


class TestCalc:
    # setup_class每个类里面 执行前后分别 执行
    def setup_class(self):
        self.cal = Calculator()
        print('类级别 setup')

    def teardown_class(self):
        print('类级别 teardown')

    # 函数级别 每条类里面的测试用例前后分别执行 setup teardown
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")


    @pytest.mark.add
    @pytest.mark.parametrize('a, b, result',[
        (1,1,2),
        (2,2,4),
        (100,100,200),
        (0.1,0.1,0.2),
        (-1,-1,-2)
    ]
    ,ids=['int','int','bignum','float','fushu']  )
    def test_add(self, a, b, result):
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    @pytest.mark.add
    def test_add1(self):
        # cal = Calculator()
        assert 3 == self.cal.add(1, 2)

    @pytest.mark.decrease
    @pytest.mark.parametrize('a, b, result', yaml.safe_load(open("yaml/calc_decrease.yml")))
    def test_decrease(self,a, b, result,calc):
        assert result == self.cal.decrease(a,b)

    @pytest.mark.multiply
    @pytest.mark.parametrize('a, b, result', yaml.safe_load(open("yaml/calc_multiply.yml")))
    def test_multiply(self, a, b, result):
        assert result == self.cal.multiply(a, b)

    @pytest.mark.div
    @pytest.mark.parametrize('a, b, result', yaml.safe_load(open("yaml/calc_div.yml")))
    def test_div(self, a, b, result):
        assert result == self.cal.div(a, b)