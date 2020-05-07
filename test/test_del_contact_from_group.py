from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, orm):
    # check if at least one group exists else create
    app.group.check(orm, Group(name="test"))
    # check if at least one contact exists else create
    app.contact.check(orm, Contact(firstname="Homer", middlename="Jay", lastname="Simpson"))
    # select contact and group
    contact, group = select_contact_and_group_for_del(app, orm)
    old_list_groups_of_contact = orm.get_groups_for_contact(contact)
    app.contact.del_contact_from_group(contact.id, group)
    new_list_groups_of_contact = orm.get_groups_for_contact(contact)
    old_list_groups_of_contact.remove(group)
    assert sorted(old_list_groups_of_contact, key=Contact.id_or_max) == \
           sorted(new_list_groups_of_contact, key=Contact.id_or_max)


def select_contact_and_group_for_del(app, orm):
    contacts = orm.get_contact_list()
    # check all contacts: if some contact is added to groups, return this contact and its random group
    for contact in contacts:
        groups_of_contact = orm.get_groups_for_contact(contact)
        if len(groups_of_contact) > 0:
            return contact, random.choice(groups_of_contact)
    # else add random contact to group and return these contact and group
    contact = random.choice(contacts)
    group = random.choice(orm.get_group_list())
    app.contact.add_contact_to_group(contact.id, group)
    return contact, group