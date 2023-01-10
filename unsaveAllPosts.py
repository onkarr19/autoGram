from main import *


def unsave_all_posts():
    driver.get(f'https://www.instagram.com/{username}/saved/all-posts/')
    sleep(4)

    div = driver.find_elements_by_class_name('v1Nh3')
    div[0].find_element_by_tag_name('a').click()

    for i in range(len(div)):
        sleep(4)
        driver.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[4]/div/div/button').click()
        driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()


try:
    login(username, password)
    unsave_all_posts()

finally:
    driver.close()
