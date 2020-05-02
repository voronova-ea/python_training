from model.group import Group
from model.contact import Contact


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean_spaces(group):
        return Group(id=group.id, name=group.name.strip() if group.name is not None else group.name)

    db_list = map(clean_spaces, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()

    def clean_spaces(contact):
        return Contact(id=contact.id,
                       firstname=contact.firstname.strip() if contact.firstname is not None else contact.firstname,
                       lastname=contact.lastname.strip() if contact.lastname is not None else contact.lastname)

    db_list = map(clean_spaces, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)