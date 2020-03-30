from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.navigation = NavigationHelper(self)

    def destroy(self):
        self.wd.quit()
