# -*- coding: utf-8 -*-
from model.group import Group


def test_group_add(app):
    app.group.create(Group(name="test group", header="test", footer="test"))


def test_empty_group_add(app):
    app.group.create(Group(name="", header="", footer=""))