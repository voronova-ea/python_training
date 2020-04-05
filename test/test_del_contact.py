from model.contact import Contact


def test_delete_first_contact_from_main_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Homer", middlename="Jay", lastname="Simpson"))
    app.contact.delete_first_contact_from_main_page()


def test_delete_first_contact_from_edit_form(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                               homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                               phone2="", notes=""))
    app.contact.delete_first_contact_from_edit_form()
