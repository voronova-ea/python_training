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
    if check_ui:
        assert sorted(map(app.group.clean_spaces, db.get_group_list()), key=Group.id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.id_or_max)