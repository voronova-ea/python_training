from model.group import Group
import random


def test_group_edit(app, db, json_groups, check_ui):
    group_data = json_groups
    app.group.check(db, Group(name="name", header="header", footer="footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_data.id = group.id
    app.group.edit_group_by_id(group.id, group_data)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(group_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # опциональная проверка, если при запуске указан check_ui
    app.group.ui_check(db, check_ui)