import re

from model.contact import Contact


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def test_contacts_info_on_home_page_vs_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname1", lastname="lastname1", homephone="781236223",
                                   email="ivanov@gmail.com", mobilephone="+79119685588", workphone="88124568995",
                                   secondaryphone="88124568988", address="Spb Nevskiy 36-89", email2="ivanov@mail.ru",
                                   email3="ivanov@ya.ru"))
    for index in range(len(db.get_contact_list())):
        contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)[index]
        contact_from_db = db.get_contact_list()[index]
        assert clear(contact_from_home_page.firstname) == clear(contact_from_db.firstname)
        assert clear(contact_from_home_page.lastname) == clear(contact_from_db.lastname)
        assert clear(contact_from_home_page.address) == clear(contact_from_db.address)
        assert clear(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_home_page(
            contact_from_db)
        assert clear(contact_from_home_page.all_email_from_home_page) == merge_emails_like_from_home_page(
            contact_from_db)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.homephone, contact.mobilephone,
                                                            contact.workphone, contact.secondaryphone]))))


def merge_emails_like_from_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
