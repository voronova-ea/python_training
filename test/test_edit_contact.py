from model.contact import Contact
import random


def test_contact_edit_all_fields(app, db, json_contacts, check_ui):
    contact_data = json_contacts
    app.contact.check(db, Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                              address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                              homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                              phone2="", notes=""))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_data.id = contact.id
    app.contact.edit_contact_by_id(contact.id, contact_data)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(contact_data)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(app.contact.clean_spaces, db.get_contact_list()), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



