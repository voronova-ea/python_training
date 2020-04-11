from model.contact import Contact


def test_delete_first_contact_from_main_page(app):
    app.contact.check(Contact(firstname="Homer", middlename="Jay", lastname="Simpson"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_from_main_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)


def test_delete_first_contact_from_edit_form(app):
    app.contact.check(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                              address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                              homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                              phone2="", notes=""))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_from_edit_form()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
