import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                groups.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups

    def get_contact_list(self):
        contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3,phone2"
                           " from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email1, email2, email3, phone2) = row
                contacts.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                        home=home, mobile=mobile, work=work, email1=email1, email2=email2,
                                        email3=email3, phone2=phone2))
        finally:
            cursor.close()
        return contacts

    def destroy(self):
        self.connection.close()