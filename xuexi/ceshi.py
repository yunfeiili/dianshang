import pytest


# class TestDome:
#
#     def test_01(self):
#         print('----测试用例：test_01------')
#
#     def test_02(self):
#         print('----测试用例：test_02------')
#
#     def setup_method(self):
#         print("测试执行前的数据")
#     # def setup_method(function):
#     #     print("测试用例前置方法---setup_method---")
#
#     def teardown_method(self):
#         print("测试用例后置方法---teardown_method---")
#
#
#     def setup_class(self):
#         print("testdome类执行前准备的数据")
#
#
#
#     def teardown_class(self):
#         print("testdome类执行后删除的数据")
import openai

# 设置OpenAI API密钥
api_key1="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"

openai.api_key = api_key1


def generate_technical_article(topic, max_tokens=1500):
    prompt = f"Write a detailed technical article on: {topic}"

    # 调用OpenAI API生成文章
    response = openai.Completion.create(
    engine = "gpt-4o-mini",
    prompt = prompt,
    max_tokens = max_tokens,
    temperature = 0.7

)

    return response.choices[0].text.strip()

# 测试生成文章
if __name__ == "__main__":
    topic = "AI-based image recognition techniques"
    article = generate_technical_article(topic)
    print("生成的文章:\n", article)
