from selenium.webdriver.common.by import By
from demo_wechat_PO.page_object.addmember_page import AddmemberPage
from demo_wechat_PO.page_object.base_page import BasePage
from demo_wechat_PO.page_object.iindex_page import IndexPage


class ContactPage(BasePage):
    def goto_addmember(self):
        self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        return AddmemberPage()

    def goto_index(self):
        return IndexPage()

    def goto_adddep(self):
        self.driver.find_element(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.driver.find_element(By.LINK_TEXT, "添加部门").click()

    def get_deps(self):
        pass
