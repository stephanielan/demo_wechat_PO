import time
from selenium.webdriver.common.by import By
from demo_wechat_PO.page_object.base_page import BasePage
from demo_wechat_PO.page_object.contact_page import ContactPage


class AdddepPage(BasePage):
    def add_dep(self):
        self.driver.find_element(By.NAME, "name").send_keys("开发部")
        self.driver.find_element(By.LINK_TEXT, "选择所属部门").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "div.jstree:nth-child(1)").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        return ContactPage()