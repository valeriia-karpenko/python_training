# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.open_contacts_page()
    app.contact.create(Contact(firstname="gfdgdfgdfg", middlename="sdfdfsdfsd", lastname="dfsdfsdf",
                               nickname="sdfdsfs", company="dfsdfds", address="fsdf"))


def test_add_empty_contact(app):
    app.contact.open_contacts_page()
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                               nickname="", company="", address=""))
