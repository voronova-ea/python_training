from pytest_bdd import given, when, then
from model.group import Group
import random


@given('a group list')
def group_list(db):
    return db.get_group_list()


@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(app, db):
    app.group.check(db, Group(name="test"))
    return db.get_group_list()


@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then('the new group list is equal to the old list without the deleted group')
def verify_group_deleted(app, db, non_empty_group_list, random_group, check_ui):
    old_group = non_empty_group_list
    new_groups = db.get_group_list()
    old_group.remove(random_group)
    assert old_group == new_groups
    app.group.ui_check(db, check_ui)
