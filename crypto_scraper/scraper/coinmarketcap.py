import time,re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
class CoinMarketCap:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--log-level=3")  
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-infobars")
        
        prefs = {"profile.managed_default_content_settings.images": 2,
                 "profile.managed_default_content_settings.cookies": 2,
                 "profile.managed_default_content_settings.javascript": 1}
        chrome_options.add_experimental_option("prefs", prefs)

        chrome_service = Service("D:\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def fetch_coin_data(self, coin):
        url = f"https://coinmarketcap.com/currencies/{coin}/"
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        output = {
            'price': self._get_price(soup),
            'price_change': self._get_price_change(soup),
            'market_cap': self._get_market_cap(soup),
            'market_cap_rank': self._get_market_cap_rank(soup),
            'volume': self._get_volume(soup),
            'volume_rank': self._get_volume_rank(soup),
            'volume_change': self._get_volume_change(soup),
            'circulating_supply': self._get_circulating_supply(soup),
            'total_supply': self._get_total_supply(soup),
            'diluted_market_cap': self._get_diluted_market_cap(soup),
            'contracts': self._get_contracts(soup),
            'official_links': self._get_official_links(soup),
            'socials': self._get_social_links(soup),
        }
        
        return output
    
    def _get_price(self, soup):
        try:
            price_element = soup.find("div", class_="sc-d1ede7e3-0 eaAjIS coin-stats-header") \
                                .find("span", class_="sc-d1ede7e3-0 fsQm base-text")
            price = price_element.text.strip()
            return float(price.replace('$', '').replace(',', ''))
        except Exception:
            return None

    def _get_price_change(self, soup):
        try:
            percentage_change_element = soup.find("div", class_="sc-d1ede7e3-0 kzFEmO") \
                                .find("div", class_="sc-4c05d6ef-0 sc-58c82cf9-0 dlQYLv dTczEt") \
                                .find("p", class_="sc-71024e3e-0 sc-58c82cf9-1 ihXFUo iPawMI")

            percentage_change = re.search(r'(\d+\.\d+)%', percentage_change_element.text)
            return (percentage_change.group(1))
        except Exception as e:
            return e

    def _get_market_cap(self, soup):
        try:
            dl_element = soup.find("dl", class_="sc-d1ede7e3-0 bwRagp coin-metrics-table")
            value_element = dl_element.find_all("div", class_="sc-d1ede7e3-0 bwRagp")[0] \
                                            .find("dd", class_="sc-d1ede7e3-0 hPHvUM base-text")
            value_cap_text = value_element.contents[-1].strip()
            return int(value_cap_text.replace('$', '').replace(',', ''))
        except Exception:
            return None

    def _get_market_cap_rank(self, soup):
        try:
            ranklist = soup.find("dl", class_="sc-d1ede7e3-0 bwRagp coin-metrics-table")
            rank_element = ranklist.find_all("div", class_="sc-d1ede7e3-0 bwRagp")[0] \
                            .find("div", class_="sc-d1ede7e3-0 sc-cd4f73ae-3 bwRagp iElHRj BasePopover_base__tgkdS") \
                            .find("span", class_="text slider-value rank-value")
            rank_text = rank_element.text.strip()
            return int(rank_text.replace('#', ''))
        except Exception:
            return None

    def _get_volume(self, soup):
        try:
            dl_element = soup.find("dl", class_="sc-d1ede7e3-0 bwRagp coin-metrics-table")
            value_element = dl_element.find_all("div", class_="sc-d1ede7e3-0 bwRagp")[1] \
                                            .find("dd", class_="sc-d1ede7e3-0 hPHvUM base-text")
            value_cap_text = value_element.contents[-1].strip()
            return int(value_cap_text.replace('$', '').replace(',', ''))
        except Exception:
            return None

    def _get_volume_rank(self, soup):
        try:
            ranklist = soup.find("dl", class_="sc-d1ede7e3-0 bwRagp coin-metrics-table")
            rank_element = ranklist.find_all("div", class_="sc-d1ede7e3-0 bwRagp")[1] \
                            .find("div", class_="sc-d1ede7e3-0 sc-cd4f73ae-3 bwRagp iElHRj BasePopover_base__tgkdS") \
                            .find("span", class_="text slider-value rank-value")
            rank_text = rank_element.text.strip()
            return int(rank_text.replace('#', ''))
        except Exception:
            return None
    
    def _get_volume_change(self, soup):
        try:
            dl_element = soup.find("dl", class_="sc-d1ede7e3-0 bwRagp coin-metrics-table")
            value_element = dl_element.find_all("div", class_="sc-d1ede7e3-0 bwRagp")[2] \
                                            .find("dd", class_="sc-d1ede7e3-0 hPHvUM base-text")
            value_cap_text = value_element.contents[-1].strip()
            return float(value_cap_text.split('%')[0].replace(',', ''))
        except Exception:
            return None
        
    def _get_circulating_supply(self, soup):
        try:
            dl_element = soup.find("dl", class_="sc-d1ede7e3-0 bwRagp coin-metrics-table")
            value_element = dl_element.find_all("div", class_="sc-d1ede7e3-0 bwRagp")[3] \
                                            .find("dd", class_="sc-d1ede7e3-0 hPHvUM base-text")
            value_cap_text = value_element.contents[-1].strip()
            numeric_value = value_cap_text.split()[0]  
            return int(numeric_value.replace(',', ''))
        except Exception:
            return None

    def _get_total_supply(self, soup):
        try:
            dl_element = soup.find("dl", class_="sc-d1ede7e3-0 bwRagp coin-metrics-table")
            value_element = dl_element.find_all("div", class_="sc-d1ede7e3-0 bwRagp")[4] \
                                            .find("dd", class_="sc-d1ede7e3-0 hPHvUM base-text")
            value_cap_text = value_element.contents[-1].strip()
            numeric_value = value_cap_text.split()[0] 
            return int(numeric_value.replace(',', ''))
        except Exception:
            return None

    def _get_diluted_market_cap(self, soup):
        try:
            dl_element = soup.find("dl", class_="sc-d1ede7e3-0 bwRagp coin-metrics-table")
            value_element = dl_element.find_all("div", class_="sc-d1ede7e3-0 bwRagp")[6] \
                                            .find("dd", class_="sc-d1ede7e3-0 hPHvUM base-text")
            value_cap_text = value_element.contents[-1].strip()
            return int(value_cap_text.replace('$', '').replace(',', ''))
        except Exception:
            return None

    def _get_contracts(self, soup):
        try:
            contract_div = soup.find("div", class_="sc-d1ede7e3-0 cvkYMS coin-info-links") \
                            .find_all("div", class_="sc-d1ede7e3-0 jTYLCR")[0] 
            span_name = contract_div.find("a", class_="chain-name") \
                            .find("span", class_="sc-71024e3e-0 dEZnuB")
            span_address = contract_div.find("a", class_="chain-name") \
                            .find("span", class_="sc-71024e3e-0 eESYbg address")
            contract_name = span_name.get_text(strip=True).replace(":", "").strip()
            contract_address = span_address.get_text(strip=True).strip()

            return {"name": contract_name, "address": contract_address}
        except Exception:
            return None

    def _get_official_links(self, soup):
        try:
            websites = []
            links_div = soup.find("div", class_="sc-d1ede7e3-0 cvkYMS coin-info-links")
            website_divs = links_div.find_all("div", class_="sc-d1ede7e3-0 jTYLCR")[1]
            for website_div in website_divs:
                website_name_tag = website_div.find("a", rel="nofollow noopener")
                if website_name_tag:
                    website_address = website_name_tag['href']
                    website_name = website_name_tag.get_text(strip=True)
                    websites.append({"name": website_name, "address": website_address})
            return websites
        except Exception:
            return None

    def _get_social_links(self, soup):
        try:
            socials = []
            links_div = soup.find("div", class_="sc-d1ede7e3-0 cvkYMS coin-info-links")
            socials_div = links_div.find_all("div", class_="sc-d1ede7e3-0 jTYLCR")[2]
            social_links = socials_div.find_all("div", class_="sc-d1ede7e3-0 sc-7f0f401-0 gRSwoF gQoblf")
            for social_link in social_links:
                social_tag = social_link.find("a", rel="nofollow noopener")
                if social_tag:
                    social_url = social_tag['href']
                    social_name = social_tag.get_text(strip=True).split()[-1] 
                    socials.append({"name": social_name.lower(), "url": social_url})
            return socials
        except Exception:
            return None

    def close(self):
        self.driver.quit()
