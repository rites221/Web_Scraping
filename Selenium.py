from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time  #to tackle the slow loading of the page

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'D:\Desktop\python_for_data_analysis\chromedriver.exe'

#KEEP THE CHROME DRIVER IN THE SAME PATH WHERE THE PYTHON SCRIPT IS WRITTEN

driver = webdriver.Chrome(executable_path=path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

#Dropdowm

Dropdown_country = Select(driver.find_element_by_id('country'))
Dropdown_country.select_by_visible_text('Spain') #To select the text by visibility
time.sleep(3) #it will wait for 3 seconds before executing the next line of the code. To tackle the loading of the page.

Dropdown_lag = Select(driver.find_element_by_id('league'))
Dropdown_lag.select_by_visible_text('La Liga') #To select the text by visibility
time.sleep(3)

Dropdown = Select(driver.find_element_by_id('season'))
Dropdown.select_by_visible_text('20/21') #To select the text by visibility
time.sleep(3)

matches = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home = match.find_element_by_xpath('./td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away_team.append(match.find_element_by_xpath('./td[4]').text)

driver.quit()

#Exporting data to CSV File with Pandas
df = pd.DataFrame({'date':date, 'home_team':home_team, 'score':score, 'away_team':away_team})
df.to_csv('football_data.csv',index=False)
print(df)

