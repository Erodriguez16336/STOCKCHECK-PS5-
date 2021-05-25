import selenium
import time
from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

def checkWalmart(item, store, url):
    page = requests.get(url)
    try:
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find_all('span', class_='price-characteristic')
        print(price)
        try:
            addCart = soup.find_all('span', class_='price-characteristic')
        except:
            addCart = soup.find_all('span', class_='spin-button-children')
        print(addCart)
        if "Add" in addCart.text:
            inStock = True
        elif "This item is" in addCart.text:
            inStock = False
        else:
            inStock = False
        if int(price.text) > 500:
            thirdParty = True
        else:
            thirdParty = False
    except:
        thirdParty = False
        inStock = False
    return availability(item, store, inStock, thirdParty, url)


def availability(item, store, inStock, thirdParty, url):
    if inStock:
        if thirdParty:
            return f"{Fore.WHITE}INFO{Fore.RESET} :: " \
                   f"{Fore.YELLOW}{item} :: " \
                   f"{Fore.BLUE}{store}{Fore.RESET} :: " \
                   f"{Fore.GREEN}IN STOCK{Fore.RESET} :: " \
                   f"{Fore.LIGHTRED_EX}THIRD PARTY{Fore.RESET}:: " \
                   f"{Fore.CYAN}{url}{Fore.RESET}"
        else:
            return f"{Fore.WHITE}INFO{Fore.RESET} :: " \
                   f"{Fore.YELLOW}{item} :: " \
                   f"{Fore.BLUE}{store}{Fore.RESET} :: " \
                   f"{Fore.GREEN}IN STOCK{Fore.RESET} :: " \
                   f"{Fore.CYAN}{url}{Fore.RESET}"
    if not inStock:
        return f"{Fore.WHITE}INFO{Fore.RESET} :: " \
               f"{Fore.YELLOW}{item} :: " \
               f"{Fore.BLUE}{store}{Fore.RESET} :: " \
               f"{Fore.RED}OUT OF STOCK{Fore.RESET} :: " \
               f"{Fore.CYAN}{url}{Fore.RESET}"


checkWalmart('Tracfone Wireless', 'WALMART',
                     'https://www.walmart.com/ip/Tracfone-Wireless-LG-Classic-Flip-8GB-Black-Prepaid-Phone/679025506?wpa_bd=&wpa_pg_seller_id=F55CDC31AB754BB68FE0B39041159D63&wpa_ref_id=wpaqs:n3jB8EXWl6-46QQOqeiBRRP1wtC6518zS4r7S7L5rcKdR3a1pUd32HLHulnPGEyAgQSJ6odAn4kKNkJmVifRIBhqcBFDGNpBMks48bUQpCVUERbF6qIPi7JsVBY6kEr-bUvtk-yc-Ltvd0rG0eFEvakSLIUzzY3qLVJr0wJZupeDzHMqqhtpph_n-Gbvy_bQazQ7YJ2H_msZ5PEsKTt0sn8oVOT4_r2DIumn-vW-MVKVLVVEMhSWWTg38lLN_op8&wpa_tag=&wpa_aux_info=&wpa_pos=2&wpa_plmt=1145x1145_T-C-IG_TI_1-6_HL-INGRID-GRID-NY&wpa_aduid=6a7a8128-fbae-4006-a4ce-4b74a7a12682&wpa_pg=search&wpa_pg_id=phone&wpa_st=phone&wpa_tax=1105910_4527935_1072335_8991975&wpa_bucket=__bkt__')