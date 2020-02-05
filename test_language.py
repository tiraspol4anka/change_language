import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_choose_language(browser):
    browser.get(link)
    x = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    y = x.text
    assert len("y") > 0, "buttun is ok"
    time.sleep(30)
