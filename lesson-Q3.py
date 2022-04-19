from pickle import TRUE
from selenium import webdriver
import time
import os

options = webdriver.ChromeOptions() #for some reason you need this to work
options.add_experimental_option("detach", True) #stack overflow clutched up

###
driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe') #get driver (change accordingly to where u hide your drivers)
driver.get('https://www.ixl.com/signin/desmet') #change this to your skools login page
driver.find_element_by_xpath('//*[@id="siusername"]').send_keys('<ENTER_USERNAME_HERE>') #ur username
driver.find_element_by_xpath('//*[@id="sipassword"]').send_keys('<ENTER_PASSWORD_HERE>') #ur password (trust me bro im not stealing it)
driver.find_element_by_xpath('//*[@id="custom-signin-button"]').click()
time.sleep(1)
driver.get('https://www.ixl.com/math/geometry/pythagorean-inequality-theorems') #get your lesson url

smartscore = 0

#do this shit
while TRUE:
    time.sleep(1.5)

    ai_input = driver.find_elements_by_class_name('decimal-scalar')
    tri1 = int(ai_input[0].get_attribute('innerText'))
    tri2 = int(ai_input[1].get_attribute('innerText'))
    tri3 = int(ai_input[2].get_attribute('innerText'))

    #lets do math
    tri1_sq = tri1*tri1
    tri2_sq = tri2*tri2
    tri3_sq = tri3*tri3

    check_run = int(driver.find_element_by_class_name('current-smartscore').get_attribute('innerText'))

    if check_run < 75:
        if tri1_sq+tri2_sq < tri3_sq: #obtuse
            driver.find_element_by_xpath('/html/body/main/div/article/section/div/div[1]/section/section[2]/section/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/span').click()
        elif tri1_sq+tri2_sq > tri3_sq: #acute
            driver.find_element_by_xpath('/html/body/main/div/article/section/div/div[1]/section/section[2]/section/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/span').click()
        elif tri1_sq+tri2_sq == tri3_sq: #right
            driver.find_element_by_xpath('/html/body/main/div/article/section/div/div[1]/section/section[2]/section/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/span').click()
        else: #not a triangle
            driver.find_element_by_xpath('/html/body/main/div/article/section/div/div[1]/section/section[2]/section/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div/div/span').click()

    driver.find_element_by_xpath('/html/body/main/div/article/section/div/div[1]/section/section[2]/div/button').click()
    time.sleep(5)

    check = driver.find_element_by_class_name('current-smartscore').get_attribute('innerText')
    if int(check) < int(smartscore):
        next_btn = driver.find_element_by_xpath('/html/body/main/div/article/section/div/div[4]/section/div[1]/div[3]/button')
        next_btn.location_once_scrolled_into_view
        next_btn.click()

    smartscore = driver.find_element_by_class_name('current-smartscore').get_attribute('innerText')
