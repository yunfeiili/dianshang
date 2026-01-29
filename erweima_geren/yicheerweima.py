from pickle import FALSE

import pytest


@pytest.fixture(autouse=False)
def ceshishuju():
    print("\n数据准备")

class Test_log:

    def test_01(self,ceshishuju):

        print("这个是测试数据01")
        assert 1==1

    def test_02(self,ceshishuju):
        print("这个是测试数据02")

    @pytest.mark.parametrize("x, y, expected", [
        pytest.param(1, 2, 3, id='positive_numbers'),
        pytest.param(-1, -1, -2, id='negative_numbers'),
    ])
    def test_add_named(self,ceshishuju,x, y, expected,):
        assert x + y == expected



from segno import helpers

def erweima_01():

    a = helpers.make_mecard(name='李先生',
                            phone='13762616230',
                            email='1538699506@qq.com',
                            city="常德",
                            videophone="1211312",
                            nickname= "云飞",
                            birthday= "1998-10-19"
                            )

    a.save(r'./李先生.png', scale=35)

def erweima_02():
    # a = helpers.make_vcard(
    #     name="李先生",
    #     displayname= "liyunfei",
    # )
    # a.save(r"./测试02.png",scale=10, border=2)
    import segno

    # 生成vCard二维码
    qr = segno.helpers.make_vcard(
        name='李云飞',  # 姓和名用分号分隔
        nickname='云飞',
        displayname='(测试)',
        phone='13762616230',
        email='1538699506@qq.com',
        city='湖南省-常德市-澧县',
        org='ABC科技有限公司',
        birthday= "1998-10-13"
    )

    # 保存二维码（可调整尺寸和边框）
    qr.save('zhangwei_vcard.png', scale=10, border=2)  # scale控制像素大小，border控制白边

erweima_01()
erweima_02()
