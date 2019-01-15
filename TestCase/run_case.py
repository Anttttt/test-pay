import unittest
from Public.HTMLTestReport import HTMLTestRunner
suite = unittest.TestSuite()  # 创建测试套件
all_cases = unittest.defaultTestLoader.discover('.', 'test_*.py')
# 找到某个目录下所有的以test开头的Python文件里面的测试用例
for case in all_cases:
    suite.addTests(case)  # 把所有的测试用例添加进来
with open('res.html', 'wb') as f:
    runner = HTMLTestRunner(stream=f, title='all_tests', description='所有测试情况')
    runner.run(suite)