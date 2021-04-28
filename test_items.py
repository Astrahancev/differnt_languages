import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    ass = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(10)
    print(ass)
