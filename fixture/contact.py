from selenium.webdriver.support.ui import Select


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
        self.app.navigation.open_home_page()
        # Init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        # Submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # return to home page
        self.app.navigation.return_to_home_page()

    def open_edit_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.open_edit_form()
        self.fill_form(contact)
        # Submit contact editing
        wd.find_element_by_xpath("(//input[@value='Update'])").click()
        # return to home page
        self.app.navigation.return_to_home_page()

    def delete_first_contact_from_main_page(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # init deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        # submit deletion
        wd.switch_to_alert().accept()

    def delete_first_contact_from_edit_form(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        self.open_edit_form()
        # submit deletion from edit form
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
