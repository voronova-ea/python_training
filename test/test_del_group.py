from model.group import Group


def test_delete_first_group(app):
    app.group.check(Group(name="test"))
    app.group.delete_first_group()
