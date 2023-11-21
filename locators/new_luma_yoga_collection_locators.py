from selenium.webdriver.common.by import By

class PriceTabLocators:
    PRICE_TAB = (By.XPATH,'//div[@class="filter-options-title" and text()="Price"]')
    PRICE_LIST = (By.XPATH,'//div[@style="display: block;"]/ol[@class="items"]/li')
    PRICE_LEVEL_LOCATOR = (By.XPATH, './/span')