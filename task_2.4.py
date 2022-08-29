from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from math import log, sin
import pyperclip

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/explicit_wait2.html')
	WebDriverWait(browser, 13).until(expected_conditions.text_to_be_present_in_element(("id", 'price'), '$100'))
	browser.find_element("id", 'book').click()
	browser.find_element("id", 'answer').send_keys(
		str(log(abs(12 * sin(int(browser.find_element("id", 'input_value').text)))))
	)
	browser.find_element("id", 'solve').click()
	alert = browser.switch_to.alert
	alert_text = alert.text
	addToClipBoard = alert_text.split(': ')[-1]
	pyperclip.copy(addToClipBoard)
finally:
	browser.quit()
