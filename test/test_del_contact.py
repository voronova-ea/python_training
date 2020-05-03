from model.contact import Contact
import random


def test_delete_first_contact_from_main_page(app, db, check_ui):
    app.contact.check(db, Contact(firstname="Homer", middlename="Jay", lastname="Simpson"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id_from_main_page(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    # опциональная проверка, если при запуске указан check_ui
    app.contact.ui_check(db, check_ui)


def test_delete_first_contact_from_edit_form(app, db, check_ui):
    app.contact.check(db, Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                              address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                              homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                              phone2="", notes=""))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id_from_edit_form(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    # опциональная проверка, если указан check_ui
    app.contact.ui_check(db, check_ui)