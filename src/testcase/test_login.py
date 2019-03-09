import paramunittest
import pytest
from readconfig import ReadConfig
import os
# import sys
# sys.path.append("os.path.dirname(os.path.abspath(sys.argv[0]))")
from common.configrequest import ConfigRequest
from common.readexcel import ReadExcel

# filename = './TestData/LoginData.xlsx'
# filename = 'D:/InterfaceTest/TestData/LoginData.xlsx'
# print(filename)
# sheetname = 0
read = ReadExcel("LoginData.xlsx", "Sheet1")
caselist = read.get_caselist()
headers = {'Content-Type': 'application/json'}

# @paramunittest.parametrized(*caselist)
# class TestLogin(paramunittest.ParametrizedTestCase):
class TestLogin():
    # def setParameters(self, case_id, case_name, precondition, method, url, request_data, expect_result, test_result):
    #     self.case_name = case_name
    #     self.url = url
    #     self.request_data = request_data
    #     self.expect_result = expect_result

    @pytest.mark.parametrize("case_id, case_name, precondition, method, url, request_data, expect_result, test_result",caselist)
    def test_login(self,case_id, case_name, precondition, method, url, request_data, expect_result, test_result):
        config = ReadConfig()
        fxchat_test_host = config.get_host("hostname")
        config_request = ConfigRequest()
        res = config_request.post_method(fxchat_test_host + url, data=request_data, headers=headers)
        # content = res.json()
        if res.status_code !=200:
            assert not True
        else:
            if res['message'] == expect_result:
                assert True
        # self.assertEqual(content['message'], expect_result)