from pony.orm import *
from model.group import Group
from model.contact import Contact


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int)
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        email1 = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname, address=contact.address,
                           home=contact.home, mobile=contact.mobile, work=contact.work, email1=contact.email1,
                           email2=contact.email2, email3=contact.email3)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_groups_with_contact(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup
                                                   if (c.deprecated is None for c in g.contacts)))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_groups_for_contact(self, contact):
        orm_contact = self.get_contact_by_id(contact)
        return self.convert_groups_to_model(orm_contact.groups)

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = self.get_group_by_id(group)
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.get_group_by_id(group)
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    @db_session
    def get_contacts_in_any_groups(self):
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and len(c.groups) > 0))

    @db_session
    def get_contacts_not_in_any_groups(self):
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and len(c.groups) == 0))

    def get_group_by_id(self, group):
        return list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]

    def get_contact_by_id(self, contact):
        return list(select(c for c in ORMFixture.ORMContact if c.id == contact.id))[0]