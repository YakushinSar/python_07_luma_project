from tests.new_luma_yoga_collection.conftest import new_luma_yoga_collection_page_precondition_for_test_data
import pytest
from pages.new_luma_yoga_collection_page.new_luma_yoga_collection_page import NewLumaYogaCollectionPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from locators.new_luma_yoga_collection_locators import PRICE_TAB,PRICE_LIST,PRICE_LEVEL_LOCATOR



PRICE_LEVELS = [
    "$10.00-$19.99",
    "$20.00-$29.99",
    "$30.00-$39.99",
    "$40.00-$49.99",
    "$50.00-$59.99",
    "$60.00-$69.99",
    "$70.00-$79.99",
    "$80.00-$89.99",
    "$90.00 and above"
]
UPDATABLE_PRICE_LEVEL_LIST=PRICE_LEVELS

class TestPriceLevelsVisibleClickable:
    PARAMETERS = [
        "visibility",
        "clickability",
    ]  

    def collect_test_data():
        test_data = []
        collection_page = new_luma_yoga_collection_page_precondition_for_test_data()
        collection_page.find_price_tab_and_click
        time.sleep(3)
        price_levels = collection_page.find_elements(locator=PRICE_LIST)
        for idx,price_level in enumerate(price_levels):
            price_level_link = price_level.find_element(By.XPATH,PRICE_LIST[1]+"/a").get_attribute("href")
            link_locator = (By.XPATH,PRICE_LIST[1]+f"/a[@href='{price_level_link}']")
            # separator_locator = (By.XPATH, '//span/following-sibling::text()')
            
            # separator = price_level.find_element(separator_locator).strip()
            
            # pytest.fail(f"{separator}")
            titles = price_level.find_elements(*PRICE_LEVEL_LOCATOR)
            combined_titles = []
            separator = '-'

            if idx == len(price_levels):
                separator=' and above'
                combined_titles_text = f'{titles[0].text}{separator}'
            elif idx < len(price_levels)-1:
                for title in titles:
                    combined_titles.append(title.text)
                    combined_titles_text = f'{separator}'.join(combined_titles[:2]) 
            assert combined_titles_text == PRICE_LEVELS[idx]
            UPDATABLE_PRICE_LEVEL_LIST.remove(PRICE_LEVELS[idx])
            test_data.append([link_locator, PRICE_LEVELS[idx]])

        assert not UPDATABLE_PRICE_LEVEL_LIST 
        return test_data


    # @pytest.mark.parametrize("param", PARAMETERS)
    # @pytest.mark.parametrize("price_level_locator,expected_price_level", collect_test_data())
    # def test_check_visibility_or_clickability_of_the_title_write_for_us(
    #     self, param, price_level_locator,expected_price_level,driver
    # ):
    #     """
    #     """

    #     collection_page = NewLumaYogaCollectionPage(driver=driver)
    #     collection_page.open()
    #     collection_page.is_clickable(locator=PRICE_TAB).click()

    #     collection_page.verify_visability_or_clickability_of_the_element_in_location(
    #         param=param,
    #         element_value=f"The Price Level({expected_price_level})'",
    #         element_locator=price_level_locator,
    #         location="price table",
    #     )