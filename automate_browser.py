from selenium import webdriver
import time


def search(x):
    browser = webdriver.Firefox()
    browser.get('https:\www.google.com')
    search =browser.find_element_by_css_selector('.gLFyf')
    search.send_keys(x)
    search.submit()
    time.sleep(10)
    #browser.quit()

