import time
from colorama import Fore, Back, Style
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup

# account_sid = #
# auth_token = #
# client = Client(account_sid, auth_token)


def newDriver():
    randomW, randomH = random.randint(600, 1080), random.randint(600, 1000)
    randomPX, randomPY = random.randint(0, 100), random.randint(0, 200)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    # chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--start-maximized")
    main = webdriver.Chrome('####REPLACE WITH YOUR CHROMEDRIVER PATH#####', chrome_options=chrome_options)
    main.delete_all_cookies()
    main.set_window_size(randomW, randomH)
    main.set_window_position(randomPX, randomPY)
    return main


def checkWalmart(item, store, url):
    page = requests.get(url)
    try:
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all('span', class_='price-characteristic')
        try:
            addCart = soup.find_all('span', class_='price-characteristic')
        except:
            addCart = soup.find_all('span', class_='spin-button-children')

        if "Add" in addCart.text:
            inStock = True
        elif "This item is" in addCart.text:
            inStock = False
        else:
            inStock = False
        if int(price.text[1:]) > 500:
            thirdParty = True
        else:
            thirdParty = False
    except:
        thirdParty = False
        inStock = False
    return availability(item, store, inStock, thirdParty, url)


def checkbestBuyTarget(item, store, url):
    randomSleep()
    driver.get(url)
    thirdParty = False
    try:
        addCart = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']")))
        if 'Sold' in addCart.text:
            inStock = False
        else:
            inStock = True
    except:
        inStock = False
    return availability(item, store, inStock, thirdParty, url)


def checkTarget(item, store, url):
    randomSleep()
    driver.get(url)
    thirdParty = False
    addCart =''
    try:
        try:
            addCart = (WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='h-text-orangeDark']")))).text
        except:
            addCart = "In stock"
        if 'Sold out' in addCart:
            inStock = False
        elif 'Sold out' not in addCart and '' not in addCart:
            inStock = True
        else:
            inStock = False
    except:
        inStock = False
        print("")
    return availability(item, store, inStock, thirdParty, url)


def checkGameStop(item, store, url):
    randomSleep()
    driver.get(url)
    thirdParty = False
    try:
        addCart = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@id='add-to-cart']")))
        if 'NOT AVAILABLE' in addCart.text:
            inStock = False
        else:
            inStock = True
    except:
        inStock = False
        print("Error")
    return availability(item, store, inStock, thirdParty, url)


def checkAmazon(item, store, url):
    randomSleep()
    driver.get(url)
    thirdParty = False
    try:
        addCart = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[@class='a-size-base a-color-price']")))
        if 'unavailable' in addCart.text:
            inStock = False
        else:
            inStock = True
            dollar_dec = float(addCart.text[1:])
            if float(dollar_dec) > 500:
                thirdParty = True
            else:
                thirdParty = False
    except:
        print("Error")
    return availability(item, store, inStock, thirdParty, url)


def availability(item, store, inStock, thirdParty, url):
    t = time.strftime("%I:%M:%S %p")
    date = time.strftime("%x")
    time_string = date + ' ' + t
    print(f"{Fore.WHITE}{time_string} :: ", end='')
    if inStock:
        if thirdParty:
            return f"{Fore.WHITE}INFO{Fore.RESET} :: " \
                   f"{Fore.YELLOW}{item} :: " \
                   f"{Fore.BLUE}{store}{Fore.RESET} :: " \
                   f"{Fore.GREEN}IN STOCK{Fore.RESET} :: " \
                   f"{Fore.LIGHTRED_EX}THIRD PARTY{Fore.RESET}:: " \
                   f"{Fore.CYAN}{url}{Fore.RESET}"
        else:
            sendSMS = f'{item} is IN STOCK at {store}, click on LINK:{url}'
            returnMSG = f"{Fore.WHITE}INFO{Fore.RESET} :: " \
                      f"{Fore.YELLOW}{item} :: " \
                      f"{Fore.BLUE}{store}{Fore.RESET} :: " \
                      f"{Fore.GREEN}IN STOCK{Fore.RESET} :: " \
                      f"{Fore.CYAN}{url}{Fore.RESET}"
            message = client.messages \
                .create(
                body=sendSMS,
                from_='#',
                to='#')
            return returnMSG
    if not inStock:
        return f"{Fore.WHITE}INFO{Fore.RESET} :: " \
               f"{Fore.YELLOW}{item} :: " \
               f"{Fore.BLUE}{store}{Fore.RESET} :: " \
               f"{Fore.RED}OUT OF STOCK{Fore.RESET} :: " \
               f"{Fore.CYAN}{url}{Fore.RESET}"


def randomSleep():
    time.sleep(random.randint(0, 2))
    return


def startScript(driver):
    driver = driver
    print(checkWalmart('PLAYSTATION 5 DISC', 'WALMART',
                       'https://www.walmart.com/ip/PlayStation-5-Console/363472942?irgwc=1&sourceid=imp_Tc1WnfWe0xyLUZRwUx0Mo36bUkBzWFyFQWKY000&veh=aff&wmlspartner=imp_1943169&clickid=Tc1WnfWe0xyLUZRwUx0Mo36bUkBzWFyFQWKY000&sharedid=&affiliates_ad_id=565706&campaign_id=9383'))
    print(checkbestBuyTarget('PLAYSTATION 5 DISC', 'BESTBUY',
                             'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'))
    print(checkTarget('PLAYSTATION 5 DISC', 'TARGET',
                      'https://www.target.com/p/-/A-81114596?clkid=e23d720fNad6211eb8c4942010a246ff3&lnm=81938&afid=CNET%20Media%20Inc.&ref=tgt_adv_xasd0002'))
    print(checkGameStop('PLAYSTATION 5 DISC', 'GAMESTOP',
                        'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html'))
    print(checkAmazon('PLAYSTATION 5 DISC', 'AMAZON',
                      'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG?ref_=ast_sto_dp'))

    print(checkWalmart('PLAYSTATION 5 DIGITAL', 'WALMART',
                       'https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815?irgwc=1&sourceid=imp_Tc1WnfWe0xyLUZRwUx0Mo36bUkBzR9RJQWKY000&veh=aff&wmlspartner=imp_159047&clickid=Tc1WnfWe0xyLUZRwUx0Mo36bUkBzR9RJQWKY000&sharedid=cnet&affiliates_ad_id=565706&campaign_id=9383'))
    print(checkbestBuyTarget('PLAYSTATION 5 DIGITAL', 'BESTBUY',
                             'https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161'))
    print(checkTarget('PLAYSTATION 5 DIGITAL', 'TARGET',
                      'https://www.target.com/p/playstation-5-digital-edition-console/-/A-81114596?clkid=e23d720fNad6211eb8c4942010a246ff3&lnm=81938&afid=Future%20PLC.&ref=tgt_adv_xasd0002'))
    print(checkGameStop('PLAYSTATION 5 DIGITAL', 'GAMESTOP',
                        'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-digital-edition/11108141.html'))
    print(
        checkAmazon('PLAYSTATION 5 DIGITAL', 'AMAZON',
                    'https://arcus-www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62'))
 
driver = newDriver()
while 'yes' == 'yes':
    startScript(driver)
