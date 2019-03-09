from appium import webdriver
import pytest
import allure
from appium.webdriver.common.touch_action import TouchAction

@pytest.fixture()
def open_application():
    caps={}
    caps["platformName"] = "android"
    caps["deviceName"] = "demo"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps["unicodeKeyboard"] = True
    caps["resetKeyboard"] = True
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    yield driver
    driver.quit()

@allure.story("搜索拼多多的股票并查看详情")
def test_search(open_application):
    with allure.step("打开雪球APP"):
        driver = open_application
    with allure.step("开启雪球权限"):
        driver.find_element_by_id("com.xueqiu.android:id/open").click()
    with allure.step("同意雪球获取手机相关权限"):
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        driver.find_element_by_id("com.xueqiu.android:id/agree").click()
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    # element_close = driver.find_element_by_id("	com.xueqiu.android:id/ib_close")
    # element_close.click()
    with allure.step("点击搜索框"):
        element_search = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        element_search.click()
    with allure.step("输入搜索内容"):
        element_search_input = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        driver.implicitly_wait(3)
        element_search_input.send_keys("拼多多")
        driver.implicitly_wait(3)
        element_search_result = driver.find_element_by_id("com.xueqiu.android:id/stockName")
        assert element_search_result.get_attribute("text") == "拼多多"
        element_search_result.click()
        driver.implicitly_wait(3)
        element_title = driver.find_element_by_id("com.xueqiu.android:id/action_bar_stock_name")
        assert element_title.get_attribute("text") == "拼多多"
        element_subtitle = driver.find_element_by_id("com.xueqiu.android:id/action_bar_subtitle")
        assert element_subtitle.get_attribute("text") == "NASDAQ:PDD"


@allure.story("搜索股票并添加自选")
@pytest.mark.parametrize("stockName,stockCode",[
    ("阿里巴巴","BABA"),
    ("阿里巴巴","01688")])
# @pytest.allure.attach(name, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
def test_add_attention(open_application, stockName, stockCode):
    with allure.step("打开雪球APP"):
        driver = open_application
    with allure.step("开启雪球权限"):
        driver.find_element_by_id("com.xueqiu.android:id/open").click()
    with allure.step("同意雪球获取手机相关权限"):
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        driver.find_element_by_id("com.xueqiu.android:id/agree").click()
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    # element_close = driver.find_element_by_id("	com.xueqiu.android:id/ib_close")
    # element_close.click()
    with allure.step("点击搜索框"):
        element_search = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        element_search.click()
    with allure.step("输入搜索内容"):
        element_search_input = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        driver.implicitly_wait(3)
        element_search_input.send_keys(stockName)
        driver.implicitly_wait(3)
    with allure.step("点击股票的添加自选按钮"):
        # 将不同的股票添加自选，例如阿里巴巴的美股和港股，不同股票的添加自选的xpath是由股票的stockCode拼接而成
        element_add_attention = driver.find_element_by_xpath("//android.widget.TextView[@text='" + stockCode + "']/parent::android.widget.LinearLayout/parent::android.widget.LinearLayout/following-sibling::"
                                                          "android.widget.LinearLayout[@resource-id='com.xueqiu.android:id/add_attention']")
        element_add_attention.click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='下次再说']").click()
        driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
    with allure.step("验证股票是否已添加到自选tab"):
        '''进入自选页面'''
        TouchAction(driver).press(x=329,y=1750).release().perform()
        element_add_attention_tab = driver.find_element_by_xpath("//android.widget.TextView[@text='自选']/parent::android.widget.RelativeLayout")
        element_add_attention_tab.click()
        element_add_attention_item = driver.find_element_by_xpath("//android.widget.TextView[@text='" + stockCode + "']")
        assert element_add_attention_item.get_attribute("text") == stockCode







