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

    if check_ui:
        assert sorted(map(app.contact.clean_spaces, db.get_contact_list()), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


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

    if check_ui:
        assert sorted(map(app.contact.clean_spaces, db.get_contact_list()), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)