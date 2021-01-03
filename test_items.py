import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(3)
    assert len(browser.find_elements_by_css_selector("button.btn-add-to-basket")), "Button not exist"
