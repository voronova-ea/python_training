from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    app.group.check(db, Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    # опциональная проверка, если при запуске указан check_ui
    app.group.ui_check(db, check_ui)