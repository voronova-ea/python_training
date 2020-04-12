from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_selected_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_form(self, contact):
        wd = self.app.wd
        # Fill main fields in contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # Select day, month and year of birth
        self.change_selected_value("bday", contact.bday)
        self.change_selected_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        # Select day, month and year of anniversary
        self.change_selected_value("aday", contact.aday)
        self.change_selected_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        # Fill secondary information
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        # Init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        # Submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # return to home page
        self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def open_edit_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        self.open_edit_form()
        self.fill_form(contact)
        # Submit contact editing
        wd.find_element_by_xpath("(//input[@value='Update'])").click()
        # return to home page
        self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact_from_main_page(self):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # init deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        # submit deletion
        wd.switch_to_alert().accept()
        # wait message about deletion
        wd.find_element_by_xpath("//div[@id='content']/div[@class='msgbox']")
        self.contact_cache = None

    def delete_first_contact_from_edit_form(self):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        self.open_edit_form()
        # submit deletion from edit form
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        return len(wd.find_elements_by_name("selected[]"))

    def check(self, contact):
        if self.count() == 0:
            self.create(contact)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home_page_by_button()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("[name='entry']"):
                lastname = element.find_element_by_xpath("//tr[" + str(len(self.contact_cache) + 2) + "]/td[2]").text
                firstname = element.find_element_by_xpath("//tr[" + str(len(self.contact_cache) + 2) + "]/td[3]").text
                address = element.find_element_by_xpath("//tr[" + str(len(self.contact_cache) + 2) + "]/td[4]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id))
        return list(self.contact_cache)
