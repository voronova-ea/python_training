# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_add(app, orm, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = orm.get_contact_list()
    app.contact.create(contact)
    new_contacts = orm.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # опциональная проверка, если при запуске указан check_ui
    app.contact.ui_check(orm, check_ui)
