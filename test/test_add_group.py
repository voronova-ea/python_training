# -*- coding: utf-8 -*-
from model.group import Group


def test_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test group", header="test", footer="test"))
    app.session.logout()



def test_empty_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

