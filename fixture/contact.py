from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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

    def open_contact_edit_form_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_edit_form_by_index(index)
        self.fill_form(contact)
        # Submit contact editing
        wd.find_element_by_xpath("(//input[@value='Update'])").click()
        # return to home page
        self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def open_contact_view_form_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def delete_first_contact_from_main_page(self):
        self.delete_by_index_from_main_page(0)

    def delete_by_index_from_main_page(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # init deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        # submit deletion
        wd.switch_to_alert().accept()
        # wait message about deletion
        wd.find_element_by_xpath("//div[@class='msgbox']")
        self.contact_cache = None

    def delete_first_contact_from_edit_form(self):
        self.delete_by_index_from_edit_form(0)

    def delete_by_index_from_edit_form(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        self.open_contact_edit_form_by_index(index)
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
            rows = wd.find_elements_by_name("entry")
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                                                  all_phones_from_hom_pages=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_form_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address, home=home, work=work,
                       mobile=mobile, phone2=phone2)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_form_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)