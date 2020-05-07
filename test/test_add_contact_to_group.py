from model.contact import Contact
from model.group import Group
import random


def test_create_contact_with_adding_to_group(app, orm, data_contacts):
    app.group.check(orm, Group(name="test"))
    contact = data_contacts
    group = random.choice(orm.get_group_list())
    old_list_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.create(contact, group.id)
    new_list_contacts_in_group = orm.get_contacts_in_group(group)
    old_list_contacts_in_group.append(contact)
    assert sorted(old_list_contacts_in_group, key=Contact.id_or_max) == \
           sorted(new_list_contacts_in_group, key=Contact.id_or_max)


def test_add_contact_to_group(app, orm):
    # check if at least one group exists else create
    app.group.check(orm, Group(name="test"))
    # select contact and group
    contact, group = select_contact_and_group_for_adding(app, orm, Contact(firstname="Homer", middlename="Jay", lastname="Simpson"))
    old_list_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact.id, group)
    new_list_contacts_in_group = orm.get_contacts_in_group(group)
    old_list_contacts_in_group.append(contact)
    assert sorted(old_list_contacts_in_group, key=Contact.id_or_max) == \
           sorted(new_list_contacts_in_group, key=Contact.id_or_max)


def select_contact_and_group_for_adding(app, orm, contact_data):
    contacts = orm.get_contact_list()
    all_groups = orm.get_group_list()
    # check all contacts: if some contact is added not to all groups, return this contact and the group without it
    for contact in contacts:
        groups_of_contact = orm.get_groups_for_contact(contact)
        if len(groups_of_contact) < len(all_groups):
            for group in all_groups:
                if group not in groups_of_contact:
                    return contact, group
    # else create a new contact and return it and random group
    app.contact.create(contact_data)
    return sorted(orm.get_contact_list(), key=Contact.id_or_max)[len(contacts)], random.choice(all_groups)