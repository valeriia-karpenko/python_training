import time

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("homephone", contact.homephone)

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init contact creation
        wd.find_element_by_name("theform").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select group
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(3)
        self.contact_cache = None

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # change contact data
        self.fill_contact_form(contact)
        # submit changing contact
        wd.find_element_by_xpath('input[@name="update"])[2]').click()
        self.return_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.return_home_page()
        element_row = wd.find_elements_by_name("entry")[index]
        element = element_row.find_elements_by_tag_name("td")[7]
        element.find_element_by_tag_name("a").click()

    def modify_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # change contact data
        self.fill_contact_form(contact)
        # submit changing contact
        wd.find_elements_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()
        self.contact_cache = None

    def return_home_page(self):
        wd = self.app.wd
        # return to home page
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                # homephone = all_phones[0]
                # mobilephone = all_phones[1]
                # workphone = all_phones[2]
                # secondaryphone = all_phones[3]
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.modify_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        id = wd.find_element_by_link_text("id").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, id=id)
