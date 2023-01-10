from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
username = 'INSTAGRAM'
password = 'PASSWORD'


def login(usernm, passw):
    driver.get('https://www.instagram.com/accounts/login/')
    sleep(4)
    driver.find_element_by_name('username').send_keys(usernm)
    driver.find_element_by_name('password').send_keys(passw)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    sleep(4)


if __name__ == '__main__':
    try:
        login(usernm=username, passw=password)

    finally:
        driver.close()
