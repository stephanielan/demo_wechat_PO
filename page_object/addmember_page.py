import time
from selenium.webdriver.common.by import By
from demo_wechat_PO.page_object.base_page import BasePage
from demo_wechat_PO.page_object.contact_page import ContactPage


class AddmemberPage(BasePage):
    def goto_contact(self):
        self.driver.find_element(By.ID, "username").send_keys("test09")
        time.sleep(1)
        self.driver.find_element(By.ID, "memberAdd_acctid").click()
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("account09")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("15900000009")
        self.driver.find_element(By.LINK_TEXT, "保存").click()
        return ContactPage()

    def get_members(self):
        return [name_list]