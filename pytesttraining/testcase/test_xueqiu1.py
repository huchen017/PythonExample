import pytest
from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu1:
    @pytest.fixture()
    def open_app(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["autoGrantPermissions"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(2)
        # return driver
        # # yield driver
        # # driver.quit()

    # def test_search(self,open_app):
    #     # driver = open_app
    #     sleep(5)
    #     element_add_attention_tab = self.driver.find_element_by_xpath("//android.widget.TextView[@text='自选']/parent::android.widget.RelativeLayout")
    #     element_add_attention_tab.click()
    #     self.driver.find_element_by_id("action_create_cube").click()
    #     element_search_input = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    #     self.driver.implicitly_wait(3)
    #     element_search_input.send_keys("阿里巴巴")
    #     element_add_attention = self.driver.find_element_by_xpath("//android.widget.TextView[@text='BABA']/parent::android.widget.LinearLayout/parent::android.widget.LinearLayout/following-sibling::"
    #                                                       "android.widget.LinearLayout[@resource-id='com.xueqiu.android:id/add_attention']")
    #     resourceId = self.driver.find_element_by_id("add_attention").find_element_by_class_name("android.widget.TextView").get_attribute("resourceId")


        # if resourceId == "com.xueqiu.android:id/follow_btn":
        #     element_add_attention.click()
        #     self.driver.find_element_by_xpath("//android.widget.TextView[@text='下次再说']").click()
        #     assert len(self.driver.find_element_by_xpath("//android.widget.TextView[@text='BABA']/parent::android.widget.LinearLayout/parent::android.widget.LinearLayout/following-sibling::"
        #                                          "android.widget.LinearLayout[@resource-id='com.xueqiu.android:id/add_attention']/*[resource-id='com.xueqiu.android:id/followed_btn']")) == 1
        #     self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
        #     self.driver.find_element_by_id("com.xueqiu.android:id/iv_close").click()
        #     assert self.driver.find_element_by_id("portfolio_stockName").get_attribute("text") == "阿里巴巴"
        # else:
        #     self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
        #     assert self.driver.find_element_by_id("portfolio_stockName").get_attribute("text") == "阿里巴巴"

    def load(self):
        locations=["x","y"]
        while locations[-1] != locations[-2]:
            element = self.driver.find_element_by_xpath("//*[@text='自选' and contains(@resource-id,'tab_name')")
            locations.append(element.location)
            print(locations)

    # def test_main_swipe(self):
    #     self.load()
    #     for i in range(1,10):
    #         sleep(1)
    #         self.driver.swipe(start_x=1348, start_y=200, end_x=200,end_y=600)

    def test_touch(self,open_app):
        locations = ["x"]
        for i in range(1,5):
            element = self.driver.find_element_by_xpath("//*[@text='自选' and contains(@resource-id,'tab_name')]")
            locations.append(element.location)
            if locations[-1] == locations[-2]:
                break
            print(element.location)
        self.driver.find_element_by_xpath("//*[@text='自选' and contains(@resource-id,'tab_name')]").click()

        element = self.driver.find_element_by_xpath("//*[@text='阿里巴巴']")
        TouchAction(self.driver).long_press(element).perform()
        self.driver.find_element_by_xpath("//*[@text='删除']").click()

