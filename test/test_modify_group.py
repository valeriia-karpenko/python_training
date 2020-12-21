# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(name="dfgdfgdfgfd", header="ruytuykyu", footer="fhdfhf64546dh"))
    app.session.logout()


def test_modify_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(name="", header="", footer=""))
    app.session.logout()
