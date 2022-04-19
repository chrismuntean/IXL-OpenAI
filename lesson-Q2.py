from pickle import TRUE
from selenium import webdriver
import time
import os
import openai
import re

options = webdriver.ChromeOptions() #for some reason you need this to work
options.add_experimental_option("detach", True) #stack overflow clutched up

openai.api_key = "<ENTER_OPENAI_API_KEY_HERE>"

###
driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe') #get driver (change accordingly to where u hide your drivers)
driver.get('https://www.ixl.com/signin/desmet') #change this to your skools login page
driver.find_element_by_xpath('//*[@id="siusername"]').send_keys('<ENTER_USERNAME_HERE>') #ur username
driver.find_element_by_xpath('//*[@id="sipassword"]').send_keys('<ENTER_PASSWORD_HERE>') #ur password (trust me bro im not stealing it)
driver.find_element_by_xpath('//*[@id="custom-signin-button"]').click()
time.sleep(1)
driver.get('https://www.ixl.com/math/geometry/converse-of-the-pythagorean-theorem') #get your lesson url
##

smartscore = 0

#do this shit
while TRUE:
    time.sleep(1.5)
    ai_input_parent = driver.find_element_by_class_name('math')
    ai_input_parent_try2 = driver.find_element_by_class_name('ixl-html-crate')
    ai_input_before_line_strip = ai_input_parent_try2.find_elements_by_tag_name('DIV')[0].get_attribute('innerText')

    ai_input = os.linesep.join([s for s in str(ai_input_before_line_strip).splitlines() if s])
    def remove_last_line_from_string(ai_input):
        return ai_input[:ai_input.rfind('\n')]
    ai_input = remove_last_line_from_string(ai_input)

    print(ai_input)

    ai_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=ai_input,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    ai_response_strip = re.sub("[^0-9]", "", ai_response.choices[0]['text'])
    print(ai_response.choices[0]['text'])
    print(ai_response_strip)
    
    math = ai_response_strip

    if math == 'Yes, it is a right triangle.':
        driver.find_element_by_xpath('/html/body/main/div/article/section/div/div[1]/section/section[2]/section/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/div').click()
    else:
        driver.find_element_by_xpath('/html/body/main/div/article/section/div/div[1]/section/section[2]/section/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div').click()

    driver.find_element_by_xpath('/html/body/main/div/article/section/div/div[1]/section/section[2]/div/button').click()
    time.sleep(5)

    check = driver.find_element_by_class_name('current-smartscore').get_attribute('innerText')
    if int(check) < int(smartscore):
        next_btn = driver.find_element_by_xpath('/html/body/main/div/article/section/div/div[4]/section/div[1]/div[3]/button')
        next_btn.location_once_scrolled_into_view
        next_btn.click()

    smartscore = driver.find_element_by_class_name('current-smartscore').get_attribute('innerText')
