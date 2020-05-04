from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, orm):
    app.group.check(orm, Group(name="test"))
    app.contact.check(orm, Contact(firstname="Homer", middlename="Jay", lastname="Simpson"))
    group = random.choice(orm.get_group_list())
    app.contact.check_contact_in_group(orm, group, random.choice(orm.get_contact_list()))
    old_list_contacts_in_group = orm.get_contacts_in_group(group)
    contact = random.choice(old_list_contacts_in_group)
    app.contact.del_contact_from_group(contact.id, group)
    new_list_contacts_in_group = orm.get_contacts_in_group(group)
    old_list_contacts_in_group.remove(contact)
    assert sorted(old_list_contacts_in_group, key=Contact.id_or_max) == sorted(new_list_contacts_in_group, key=Contact.id_or_max)