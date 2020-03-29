from model.contact import Contact


def test_contact_edit(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="New Homer", middlename="New Jay", lastname="New Simpson",
                                           nickname="New Hommy", title="New Some", company="New NPS",
                                           address="New Springfield", home="09", mobile="09", work="09",
                                           fax="09", email1="new_h.simpson@gmail.com", email2="new_h.simpson@somemail.com",
                                           email3="new_h.simpson@someelsemail.com", homepage="new_facebook.com", bday="1",
                                           bmonth="June", byear="1999", aday="1", amonth="June", ayear="2029",
                                           address2="New Something", phone2="007", notes="Best friend"))
    app.session.logout()


def test_contact_edit_empty_fields(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                           address="", home="", mobile="", work="", fax="", email1="", email2="",
                                           email3="", homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-",
                                           ayear="", address2="", phone2="", notes=""))
    app.session.logout()