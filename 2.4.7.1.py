from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    #browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
        )
    #button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
#    message = browser.find_element(By.ID, "verify_message")
#    message = browser.find_element_by_css_selector("#verify_message")

    assert "successful" in message.text

finally:
    browser.quit()

