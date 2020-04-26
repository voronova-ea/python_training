from model.group import Group
from random import randrange
from data.groups import testdata
import pytest


def test_group_edit(app, data_groups):
    group = data_groups
    app.group.check(Group(name="name", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)