# -*- coding: utf-8 -*-
from model.contact import Contact
import allure


def test_contact_add(app, orm, json_contacts, check_ui):
    contact = json_contacts
    with allure.step('Given a contact list'):
        old_contacts = orm.get_contact_list()
    with allure.step('When I add a contact %s to the list' % contact):
        app.contact.create(contact)
    with allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = orm.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        # опциональная проверка, если при запуске указан check_ui
        app.contact.ui_check(orm, check_ui)