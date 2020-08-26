from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys
import config
import itertools

# place your own path to webdriver

path = config.CHROME_PATH
chrome_options = Options()  
chrome_options.add_argument("--headless")

def get_title(url):
    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    driver.get(url)
    title = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-video-primary-info-renderer"]'))
    ret = title.text
    driver.close()
    driver.quit()
    return ret


def get_transcript(url):
    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
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

def get_trending_page():
    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    driver.get('https://www.youtube.com/feed/trending')
    videos = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_xpath('//a[@id="video-title"]'))
    # temp_names = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_xpath('//yt-formatted-string[@id="text"]'))
    # title = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-video-renderer"]')).text
    # print(title)
    for element in videos:
        try:
            # name = name_element.find_element_by_xpath('.//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]').text
            title = element.get_attribute('title')

            # get the data for views and the lenght of video
            data = element.get_attribute('aria-label').split()

            views = data[-2:][0]
            length = parse_length_data(data[-6:])
            # print(name)
        except:
            driver.close()
            driver.quit()
    
    driver.close()
    driver.quit()

# Used to parse the data used for length as time stamps
# can be shorter than expected at times
def parse_length_data(data):
    check = str(data[1])
    if check == 'minutes,' or check == 'hours,':
        return "%s %s %s %s" % (data[0], data[1], data[2], data[3])
        # return "%s %s" % (data[2], data[3])
    else:
        return "%s %s" % (data[2], data[3])


get_trending_page()