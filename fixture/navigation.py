from selenium.webdriver.support.ui import Select


class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page_by_url(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("(//input[@value='Send e-Mail'])")) > 0):
            wd.get(self.app.base_url)

    def open_home_page_by_button(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("(//input[@value='Send e-Mail'])")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_group_contact_page(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_value(group.id)
        wd.find_element_by_xpath("//input[@name='remove']")

    def return_to_group_contact_page(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text('group page \"%s\"' % group.name).click()