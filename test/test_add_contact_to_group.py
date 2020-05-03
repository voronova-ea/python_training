from model.contact import Contact
from model.group import Group
import random


def test_create_contact_with_adding_to_group(app, orm, data_contacts):
    app.group.check(orm, Group(name="test"))
    contact = data_contacts
    group = random.choice(orm.get_group_list())
    old_list_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.create_and_add_to_group(contact, group.id)
    new_list_contacts_in_group = orm.get_contacts_in_group(group)
    old_list_contacts_in_group.append(contact)
    assert sorted(old_list_contacts_in_group, key=Contact.id_or_max) == sorted(new_list_contacts_in_group, key=Contact.id_or_max)


def test_add_contact_to_group(app, orm):
    app.group.check(orm, Group(name="test"))
    app.contact.check(orm, Contact(firstname="Homer", middlename="Jay", lastname="Simpson"))
    group = random.choice(orm.get_group_list())
    contact = random.choice(orm.get_contact_list())
    old_list_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact.id, group)
    new_list_contacts_in_group = orm.get_contacts_in_group(group)
    if contact not in old_list_contacts_in_group:
        old_list_contacts_in_group.append(contact)
    assert sorted(old_list_contacts_in_group, key=Contact.id_or_max) == sorted(new_list_contacts_in_group, key=Contact.id_or_max)