from model.contact import Contact
from random import randrange


def test_phones_on_home_page(app, db):
    app.contact.check(db, Contact(firstname="Homer", middlename="Jay", lastname="Simpson", nickname="Hommy",
                              title="Some", company="NPS", address="Springfield", home="027220", mobile="567890",
                              work="026789", fax="026790", email1="h.simpson@gmail.com",
                              email2="h.simpson@somemail.com",
                              email3="h.simpson@someelsemail.com", homepage="facebook.com", bday="10",
                              bmonth="May",
                              byear="1959", aday="10", amonth="May", ayear="2019", address2="Something",
                              phone2="070",
                              notes="Best friend"))
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app, db):
    app.contact.check(db, Contact(firstname="Homer", middlename="Jay", lastname="Simpson", nickname="Hommy",
                              title="Some", company="NPS", address="Springfield", home="027220", mobile="567890",
                              work="026789", fax="026790", email1="h.simpson@gmail.com",
                              email2="h.simpson@somemail.com",
                              email3="h.simpson@someelsemail.com", homepage="facebook.com", bday="10",
                              bmonth="May",
                              byear="1959", aday="10", amonth="May", ayear="2019", address2="Something",
                              phone2="070",
                              notes="Best friend"))
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2