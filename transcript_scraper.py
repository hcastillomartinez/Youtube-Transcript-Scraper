from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# place your own path to webdriver
path = r'C:\\Users\\damia\\Downloads\\geckodriver\\geckodriver.exe'

def get_title(url):
    driver = webdriver.Firefox(executable_path=path)
    driver.get(url)
    title = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-video-primary-info-renderer"]'))
    ret = title.text
    driver.close()
    driver.quit()
    return ret


def get_transcript(url):
    driver = webdriver.Firefox(executable_path=path)
    driver.get(url)
    moreActionsButton = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//button[@id="button"][@aria-label="More actions"]'))

    # select more actions button
    moreActionsButton.click()

    openTrans = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath('//paper-item[@class="style-scope ytd-menu-service-item-renderer"][@role="option"]'))

    # open transcript window
    openTrans.click()

    # make sure transcript window is open
    testTrans = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//div[@class="cue style-scope ytd-transcript-body-renderer"][@role="button"]'))

    transcript = driver.find_elements_by_xpath('//div[@class="cue style-scope ytd-transcript-body-renderer"][@role="button"]')
    title = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-video-primary-info-renderer"]')).text
    
    # write out transcript to file named after the video title
    f = open(title+".txt", "w+")
    for element in transcript:
        f.write(element.text)
        f.write('\n')
    
    f.close()

    # close the driver
    driver.close()
    driver.quit()

    return title


if len(sys.argv) < 2:
    print('Not enough arguments.')
else:
    url = sys.argv[1]
    # prints title
    print(get_title(url))
