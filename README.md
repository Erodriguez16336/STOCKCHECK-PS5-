# STOCKCHECK-PS5-

## Requirements:
1. Run the pipInstall.py file to install all the required packages.
1. Replace the chromedriver file path
1. Run the program.


## Why a StockCheck?
I created this stockchecker for PS5's because I was in need of a little extra cash flow so I had to resort to reselling. 
Because the PlayStation 5 was in such high demand there was no way I'd be able to continuosly manually check the current stock
of the console. Therefore, I went ahead and programmed a stock checker.

## What does it do?
It scrapes the website using a combination of BeautifulSoup4 and ChromeDriver.
It's able to identify the stock availability by using HTML and CSS elements
as guides. Once it find an item in stock and sold for retail price
it will send a text message using Twiliio's API.

## Can it only do the PlayStation 5 Console ?
No! All you need to do is alter the links at the bottom of the code
and add the links to the product you would like a stock check on!
![Alt Text](https://i.imgur.com/gMGxX3E.gif)

