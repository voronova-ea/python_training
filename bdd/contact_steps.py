from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(orm):
    return orm.get_contact_list()


@given('a contact with new <firstname>, <lastname>, <address>, <home> and <mobile> values')
def new_contact(firstname, lastname, address, home, mobile):
    return Contact(firstname=firstname, lastname=lastname, address=address, home=home, mobile=mobile)


@when('I add the contact to the list')
def add_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(app, db, contact_list, new_contact, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # опциональная проверка, если при запуске указан check_ui
    app.contact.ui_check(db, check_ui)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    app.contact.check(db, Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                  address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                                  homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",
                                  address2="",
                                  phone2="", notes=""))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I edit fields of the random contact to new values')
def edit_contact(app, random_contact, new_contact):
    new_contact.id = random_contact.id
    app.contact.edit_contact_by_id(random_contact.id, new_contact)


@then('the new contact list is equal to the old list with the edited contact')
def verify_contact_edited(app, db, non_empty_contact_list, random_contact, new_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # опциональная проверка, если при запуске указан check_ui
    app.contact.ui_check(db, check_ui)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_by_id_from_edit_form(random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(app, db, non_empty_contact_list, random_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    # опциональная проверка, если указан check_ui
    app.contact.ui_check(db, check_ui)

