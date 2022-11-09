from selenium.webdriver.common.by import By
from demo_wechat_PO.page_object.addmember_page import AddmemberPage
from demo_wechat_PO.page_object.base_page import BasePage
from demo_wechat_PO.page_object.contact_page import ContactPage


class IndexPage(BasePage):
    def goto_addmember(self):
        self.driver.find_element(By.LINK_TEXT, "通讯录").click()
        self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        return AddmemberPage()

    def goto_contact(self):
        return ContactPage()