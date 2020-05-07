from selenium.webdriver.support.ui import Select
from model.contact import Contact
import random
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
        if text is not None and text != '':
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_group_value(self, field_name, id):
        wd = self.app.wd
        if id is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_value(id)

    def fill_form(self, contact):
        wd = self.app.wd
        # fill main fields in contact form
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
        # select day, month and year of birth
        self.change_selected_value("bday", contact.bday)
        self.change_selected_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        # select day, month and year of anniversary
        self.change_selected_value("aday", contact.aday)
        self.change_selected_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        # fill secondary information
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def create(self, contact, group_id=None):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_form(contact)
        # add contact in group
        self.change_group_value("new_group", group_id)
        # submit contact creation
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

    def open_contact_edit_form_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        row = wd.find_element_by_xpath("//input[@value='%s']//parent::td//parent::tr" % id)
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_edit_form_by_index(index)
        self.fill_form(contact)
        # submit contact editing
        wd.find_element_by_xpath("(//input[@value='Update'])").click()
        # return to home page
        self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_edit_form_by_id(id)
        self.fill_form(contact)
        # submit contact editing
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
        # select contact
        wd.find_elements_by_name("selected[]")[index].click()
        # init deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        # submit deletion
        wd.switch_to_alert().accept()
        # wait message about deletion
        wd.find_element_by_xpath("//div[@class='msgbox']")
        self.contact_cache = None

    def delete_by_id_from_main_page(self, id):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        # select contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
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

    def delete_by_id_from_edit_form(self, id):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        self.open_contact_edit_form_by_id(id)
        # submit deletion from edit form
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        return len(wd.find_elements_by_name("selected[]"))

    def check(self, db, contact):
        if len(db.get_contact_list()) == 0:
            self.create(contact)

    def ui_check(self, db, check_ui):
        if check_ui:
            assert sorted(map(self.clean_spaces, db.get_contact_list()), key=Contact.id_or_max) == \
                   sorted(self.get_contact_list(), key=Contact.id_or_max)

    def check_contacts_in_group(self, orm, group, contact):
        if len(orm.get_contacts_in_group(group)) == 0:
            self.add_contact_to_group(contact.id, group)

    def check_contacts_not_in_groups(self, orm, contact):
        if len(orm.get_contacts_not_in_any_groups()) == 0:
            self.create(contact)

    contact_cache = None

    def get_list(self):
        wd = self.app.wd
        self.contact_cache = []
        rows = wd.find_elements_by_name("entry")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            lastname = cells[1].text
            firstname = cells[2].text
            address = cells[3].text
            id = cells[0].find_element_by_name("selected[]").get_attribute("value")
            all_emails = cells[4].text
            all_phones = cells[5].text
            self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                                              all_emails_from_home_page=all_emails,
                                              all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home_page_by_button()
            self.get_list()
        return list(self.contact_cache)

    def get_contact_list_of_group(self, group):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home_page_by_button()
            self.app.navigation.open_group_contact_page(group)
            # get list
            self.get_list()
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
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address, home=home, work=work,
                       mobile=mobile, phone2=phone2, email1=email1, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_form_by_index(index)
        text = wd.find_element_by_id("content").text
        _home = re.search("H: (.*)", text)
        if _home is not None:
            home = _home.group(1)
        else:
            home = ""
        _mobile = re.search("M: (.*)", text)
        if _mobile is not None:
            mobile = _mobile.group(1)
        else:
            mobile = ""
        _work = re.search("W: (.*)", text)
        if _work is not None:
            work = _work.group(1)
        else:
            work = ""
        _phone2 = re.search("P: (.*)", text)
        if _phone2 is not None:
            phone2 = _phone2.group(1)
        else:
            phone2 = ""
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def remove_end_or_begin_spaces(self, s):
        if s is not None:
            return re.sub('[ \t]+', " ", re.sub('^[ \t]+|[ \t]+$', "", s))

    def clean_spaces(self, contact):
        return Contact(id=contact.id,
                       firstname=contact.firstname.strip() if contact.firstname is not None else contact.firstname,
                       lastname=contact.lastname.strip() if contact.lastname is not None else contact.lastname)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home, contact.mobile, contact.work, contact.phone2]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.remove_end_or_begin_spaces(x),
                                    filter(lambda x: x is not None,
                                           [contact.email1, contact.email2, contact.email3]))))

    def add_contact_to_group(self, contact_id, group):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        # select contact
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        # select group
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group.id)
        # add to group
        wd.find_element_by_xpath("(//input[@value='Add to'])").click()
        self.app.navigation.return_to_group_contact_page(group)
        self.contact_cache = None

    def del_contact_from_group(self, contact_id, group):
        wd = self.app.wd
        self.app.navigation.open_home_page_by_button()
        self.app.navigation.open_group_contact_page(group)
        # select contact
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        # remove contact
        wd.find_element_by_xpath("//input[@name='remove']").click()
        self.app.navigation.return_to_group_contact_page(group)
        self.contact_cache = None