# Python-airplane-ticket-prices-data
A Python program that retrieves the cheapest flight ticket price each day over a specified period.

I was booking an airplane ticket to travel from Danang to Singapore and was trying to find the best deal. Seeing how airplane fare fluctuates dramatically day by day, I was curious as to how it would change over a period of time. As looking up and noting down the cheapest fare for each day over a period of let's say a month was tedious work, I made a Python program to automate the processes.

My program uses Selenium to scrap information about airplane ticket prices from the website kiwki.com. I chose this website as the best prices posted on the website can be easily seen in the DOM current state in the **span** tag with the **class** being "length-4". I extracted the prices from the DOM current state HTML using BeautifulSoup. 

This was a project mostly born out of curiosity and it was my first attempt at a full web scrapping project. The dramatic fluctuation in the price of airplane tickets was interesting to see. You can change the start and end date, as well as the URL to get prices on different routes and at different times.
