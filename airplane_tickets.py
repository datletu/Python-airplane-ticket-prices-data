from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import time

#Generate the date list
start = datetime(2023,8,1)
end = datetime(2023,8,31)
datelist = []
while start <= end:
    datelist.append(start.date())
    start += timedelta(days=1)
    
#list of prices of each day
price_list = []

# Create a new Chrome web driver instance
service = Service(executable_path='C:\Program Files\Chrome Driver\chromedriver.exe')
driver = webdriver.Chrome(service = service)

#looping through each date in the dates range
for date in datelist:
    print(date)

    
    # Open kiwi.com in the Chrome web driver
    driver.get(f'https://www.kiwi.com/en/search/results/da-nang-vietnam/singapore-singapore/{str(date)}/')

    # Wait for the page to load
    time.sleep(5)

    # Simulate pressing the F12 key
    webdriver.ActionChains(driver).key_down(Keys.F12).key_up(Keys.F12).perform()

    # Wait for a moment to see the result
    time.sleep(2)

    # Get the page source after pressing F12
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    #Get the price from the price source and add to price_list
    soup.findAll("span", class_='length-4')
    price_element = soup.find("span", class_='length-4')
    price = int(price_element.text.split('$')[-1])
    price_list.append(price)

# Close the web driver
driver.quit()

#y-axis of graph
y = np.array(price_list)

#generate datelist in matplotlib format
start = datelist[0]
end = (datelist[-1]+timedelta(days=1))
days = mdates.drange(start,end,timedelta(days=1))

#format the x-axis for readability
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))

#draw the graph
plt.plot(days,y)
plt.gcf().autofmt_xdate()
plt.show()