# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.group.modify_first_group(Group(name="dfgdfgdfgfd", header="ruytuykyu", footer="fhdfhf64546dh"))


def test_modify_empty_group(app):
    app.group.modify_first_group(Group(name="", header="", footer=""))

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New name"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
