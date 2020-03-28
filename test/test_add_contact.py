# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact_add(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Homer", middlename="Jay", lastname="Simpson", nickname="Hommy",
                               title="Some", company="NPS", address="Springfield", home="027220", mobile="567890",
                               work="026789", fax="026790", email1="h.simpson@gmail.com", email2="h.simpson@somemail.com",
                               email3="h.simpson@someelsemail.com", homepage="facebook.com", bday="10", bmonth="May",
                               byear="1959", aday="10", amonth="May", ayear="2019", address2="Something", phone2="007",
                               notes="Best friend"))
    app.session.logout()


def test_empty_contact_add(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="", fax="", email1="", email2="", email3="",
                               homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="",
                               phone2="", notes=""))
    app.session.logout()