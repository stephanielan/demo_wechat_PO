from demo_wechat_PO.page_object.iindex_page import IndexPage


class TestAddmembers:
    def test_addmembers(self):
        index = IndexPage()
        name_list= index.goto_addmember().get_members()
        return [name_list]

