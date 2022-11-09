from demo_wechat_PO.page_object.iindex_page import IndexPage


class TestAdddeps:
    def test_adddeps(self):
        index = IndexPage()
        name_list= index.goto_contact().goto_adddep().add_dep().get_deps()
        return [name_list]