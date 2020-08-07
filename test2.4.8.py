# python -m pip install selenium

try:
    from selenium import webdriver
    import time
    import math
    import os
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    link = "http://suninjuly.github.io/explicit_wait2.html"

    with webdriver.Chrome() as browser:
        try:
            0  # browser = webdriver.Chrome()
            browser.implicitly_wait(12)
            browser.get(link)


            price = WebDriverWait(browser, 5).until(
                EC.text_to_be_present_in_element((By.ID, "price"),"$100")
            )
            button=browser.find_element_by_css_selector("button.btn[id='book']")
            button.click()

            x_element = browser.find_element_by_id("input_value")
            x = x_element.text
            y = calc(x)

            input1 = browser.find_element_by_id("answer")
            input1.send_keys(y)

            button2 = browser.find_element_by_css_selector("button.btn[type='submit']")
            button2.click()

        except Exception as e:
            print(f': {e}')
        finally:
            time.sleep(3)
            browser.quit()
except Exception as e:
    print(f': {e}')

a = input()