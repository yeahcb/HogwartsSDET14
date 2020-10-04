import pytest


@pytest.fixture()
def calc():
    print('【开始计算】')
    yield
    print('【计算结束】')



# @pytest.fixture(params=['user1','user2','user2'])
@pytest.fixture()
def login(request):
    print('登陆方法')
    print(request.param)
    # yield 激活fixture teardown方法
    yield ['username','password']
    print('teardown')