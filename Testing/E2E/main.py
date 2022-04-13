from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

exec_path = r'your path'
my_url = "your path"


def test_valid_number_without_check():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,
                              executable_path=exec_path)
    driver.get(my_url)

    input_number = driver.find_element(By.ID, "exampleInputNumber")
    submit_button = driver.find_element(By.ID, "SubmitBtn")

    input_number.send_keys(3)
    submit_button.send_keys(Keys.RETURN)
    time.sleep(2)

    input_answer = driver.find_element(By.ID, "answerInput")
    if input_answer.get_attribute("placeholder") == "a^3+3a^2b+3ab^2+b^3":
        print("Ответ корректен")
    else:
        print("Ошибка, данные не совпадают")


def test_valid_number_with_check():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,
                              executable_path=exec_path)
    driver.get(my_url)

    input_number = driver.find_element(By.ID, "exampleInputNumber")
    submit_button = driver.find_element(By.ID, "SubmitBtn")
    check_square = driver.find_element(By.ID, "exampleCheck1")

    input_number.send_keys(17)
    check_square.click()
    submit_button.send_keys(Keys.RETURN)
    time.sleep(2)

    input_answer = driver.find_element(By.ID, "answerInput")
    if input_answer.get_attribute("placeholder") == (
            "a^17+17a^16b+136a^15b^2+680a^14b^3+2380a^13b^4+6188a^12b^5+12376a^11b^6+19448a^10b^7+24310a^9b^8" +
            "+24310a^8b^9+19448a^7b^10+12376a^6b^11+6188a^5b^12+2380a^4b^13+680a^3b^14+136a^2b^15+17ab^16+b^17"):
        print("Ответ корректен")
    else:
        print("Ошибка, данные не совпадают")


def test_invalid_data():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options,
                              executable_path=exec_path)
    driver.get(my_url)

    input_number = driver.find_element(By.ID, "exampleInputNumber")
    submit_button = driver.find_element(By.ID, "SubmitBtn")

    input_number.send_keys(3.3)
    submit_button.send_keys(Keys.RETURN)
    time.sleep(2)

    input_answer = driver.find_element(By.ID, "answerInput")
    if input_answer.get_attribute("placeholder") == "Something went wrong, please check your data":
        print("Ответ корректен")
    else:
        print("Ошибка, данные не совпадают")


if __name__ == '__main__':
    test_valid_number_without_check()
    test_valid_number_with_check()
    test_invalid_data()
