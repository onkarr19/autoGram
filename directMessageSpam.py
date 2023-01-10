from main import *


def send(message):
    driver.find_element_by_tag_name('textarea').send_keys(message)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div['
                                 '2]/div/div/div[3]/button').click()


def dm_spam(spam_to, spam_as, times):
    driver.get('https://www.instagram.com/direct/new/')
    sleep(2)
    div = driver.find_element_by_class_name('piCib')
    div = div.find_elements_by_tag_name('button')
    div[1].click()
    sleep(2)
    driver.find_element_by_name('queryBox').send_keys(spam_to)
    sleep(2)

    div = driver.find_elements_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div')
    div[0].click()
    sleep(2)

    driver.find_element_by_class_name('rIacr').click()

    sleep(3)
    for i in range(times):
        send(spam_as)


try:
    login(username, password)
    dm_spam(spam_to='Instagram', spam_as='You are getting spammed', times=50)

finally:
    driver.close()
