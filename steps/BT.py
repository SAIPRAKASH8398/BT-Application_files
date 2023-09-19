from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import logging
import time


@step(u"I open browser with '{url}'")
def open_url(context,url):
    context.driver = webdriver.Firefox(executable_path='C:\\Users\\Sai Prakash\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe')
    context.driver.maximize_window()
    context.driver.get(url)
    time.sleep(10)

@step(u'I check for the cookies pop up "{xpath}"')
def check_cookies(context, xpath):
    try:
        context.driver.switch_to.frame(0)
        if context.driver.find_element(By.XPATH, xpath).is_displayed():
            context.driver.find_element(By.XPATH, xpath).click()
        else:
            logging.info("Accept cookies not exists")
    except Exception:
        logging.info('Please check')


@step(u'I hover mouse on "{drop_down}" and select the option "{select_element}"')
def hover(context, drop_down, select_element):
    try:
        context.driver.switch_to.default_content()
        context.action = ActionChains(context.driver)
        context.drop = context.driver.find_element(By.XPATH, drop_down)
        context.action.move_to_element(context.drop).perform()
        time.sleep(2)
        context.sel = context.driver.find_element(By.XPATH, select_element)
        context.action.move_to_element(context.sel).click().perform()
        time.sleep(5)
    except Exception as err:
        logging.info("Failed to hover", err)

@step(u'check the number of banners "{count}" "{xpath}"')
def banner_count(context,count, xpath):
    context.banner = context.driver.find_elements(By.XPATH, xpath)
    time.sleep(10)
    if len(context.banner) == int(count):
        assert True
    else:
        assert False

@step(u'scroll down until the option visible "{xpath}" and "{title}"')
def scroll_click_and_check_title(context, xpath, title):
    try:
        time.sleep(10)
        # context.action.move_to_element(xpath).click().perform()
        ## actions.click();
        context.tit = context.driver.find_element(By.XPATH, xpath)
        context.tit.location_once_scrolled_into_view
        time.sleep(5)
        context.tit.click()
        time.sleep(15)
        if context.driver.title == title:
            assert True
        else:
            assert False
    except Exception as err:
        logging.info("Title not fetched", err)

@step(u'I check element "{xpath}"')
def check_exists_by_xpath(context,xpath):
    try:
        context.driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False, 'Expected text not found'
    return True, 'Expected text found'

@step(u'I close opened browser')
def close_browser(context):
    context.driver.quit()

