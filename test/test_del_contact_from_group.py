from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, orm):
    # check if at least one contact is in any groups else add
    app.contact.check_contacts_in_any_groups(orm, Contact(firstname="Homer", middlename="Jay", lastname="Simpson"), Group(name="test"))
    contact = random.choice(orm.get_contacts_in_any_groups())
    old_list_groups_of_contact = orm.get_groups_for_contact(contact)
    group = random.choice(old_list_groups_of_contact)
    app.contact.del_contact_from_group(contact.id, group)
    new_list_groups_of_contact = orm.get_groups_for_contact(contact)
    old_list_groups_of_contact.remove(group)
    assert sorted(old_list_groups_of_contact, key=Contact.id_or_max) == \
           sorted(new_list_groups_of_contact, key=Contact.id_or_max)