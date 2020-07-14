# Youtube-Transcript-Scraper
## Description
Automates the process of getting the transcript from Youtube videos using Selenium to navigate the page and scrape the data. After running correctly the script will download the transcript into same location as script as *Name_of_Video*.txt. Chromedriver does offer a headless mode (No UI) which can be used to let it run much faster. Would suggest doing this if user plans use this to gather many Youtube transcripts for some NLP or ML project.

**This script will open a FireFox window but will close upon completion**

## Requirements
Geckodriver which can be downloaded here -> https://github.com/mozilla/geckodriver/releases


Firefox browser which can be downloaded here -> https://www.mozilla.org/en-US/firefox/new/


Selenium can be installed via pip.

## Usage

    python transcript_scraper.py url

Will not run without a Youtube URL in the argument to prevent user error.
