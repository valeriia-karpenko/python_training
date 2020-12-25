# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_contact(Contact(firstname="gyt", middlename="frewrwe", lastname="utyut",
                                       nickname="sdfdfgddsfs", company="fgfd", address="gffg"))


def test_modify_empty_contact(app):
    app.contact.modify_contact(Contact(firstname="", middlename="", lastname="",
                                       nickname="", company="", address=""))
