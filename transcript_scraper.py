from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# replace with your own web driver executable
path = r'C:\\Users\\damia\\Downloads\\geckodriver\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path)
driver.get('https://www.youtube.com/watch?v=4nzI4RKwb5I')
moreActionsButton = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//button[@id="button"][@aria-label="More actions"]'))

# select more actions button
moreActionsButton.click()

openTrans = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath('//paper-item[@class="style-scope ytd-menu-service-item-renderer"][@role="option"]'))

# open transcript window
openTrans.click()

# make sure transcript window is open
testTrans = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//div[@class="cue style-scope ytd-transcript-body-renderer"][@role="button"]'))

transcript = driver.find_elements_by_xpath('//div[@class="cue style-scope ytd-transcript-body-renderer"][@role="button"]')

f = open("transcript.txt","w+")

for element in transcript:
    f.write(element.text)
    f.write('\n')

f.close()
driver.close()
driver.quit()
