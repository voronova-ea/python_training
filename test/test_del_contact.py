from model.contact import Contact


def test_delete_first_contact_from_main_page(app):
    app.contact.check(Contact(firstname="Homer", middlename="Jay", lastname="Simpson"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_from_main_page()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_first_contact_from_edit_form(app):
    app.contact.check(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                              address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                              homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                              phone2="", notes=""))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_from_edit_form()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
