from model.contact import Contact
from random import randrange


def test_contact_fields_value_on_home_page(app, db):
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
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.firstname == app.contact.remove_end_or_begin_spaces(contact_from_edit_page.firstname)
    assert contact_from_home_page.lastname == app.contact.remove_end_or_begin_spaces(contact_from_edit_page.lastname)
    assert contact_from_home_page.address == app.contact.remove_end_or_begin_spaces(contact_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)


