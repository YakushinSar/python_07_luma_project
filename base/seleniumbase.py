from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from locators.base_page_locators import BasePageLocators


class BasePage():
    """
    Базовый класс для страниц веб-приложения, использующий Selenium для взаимодействия с элементами на странице.

    Args:
        driver: WebDriver, экземпляр Selenium WebDriver для управления браузером.
        url (str): URL страницы, которую необходимо открыть при инициализации объекта.

    Methods:
        open(): Открывает URL страницы в браузере, связанном с данным объектом.
        
        is_visible(locator: tuple, timeout: int = 10) -> WebElement: Ожидает видимость элемента, заданного локатором, в течение указанного времени. Возвращает WebElement, если элемент видим, или вызывает исключение TimeoutException, если элемент не появился.
        
        is_clickable(locator, timeout: int = 10): Ожидает, что элемент, заданный локатором, станет кликабельным в течение указанного времени. Если элемент становится кликабельным, функция возвращает элемент, иначе вызывает исключение TimeoutException.

    Note:
        Для использования этого класса необходимо импортировать соответствующие модули и создать экземпляр WebDriver перед его инициализацией.
    """
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """
        Открывает URL страницы в браузере.
        """
        self.driver.get(self.url)

    def is_visible(self, locator: tuple, timeout: int = 10) -> WebElement:
        """
        Ожидает видимость элемента, заданного локатором, в течение указанного времени.

        Args:
            locator (tuple): Локатор элемента, который необходимо найти (например, 'id', 'name', 'css selector', 'xpath', и т.д.).
            timeout (int): Максимальное время ожидания в секундах (по умолчанию 10).

        Returns:
            WebElement: Элемент, если он видим.

        Raises:
            TimeoutException: Если элемент не появился в течение указанного времени.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator:tuple, timeout: int = 10) -> WebElement:
        """
        Ожидает, что элемент, заданный локатором, станет кликабельным в течение указанного времени.

        Args:
            locator: Локатор элемента, который необходимо найти (например, 'id', 'name', 'css selector', 'xpath', и т.д.).
            timeout (int): Максимальное время ожидания в секундах (по умолчанию 10).

        Returns:
            WebElement: Элемент, если он становится кликабельным.

        Raises:
            TimeoutException: Если элемент не становится кликабельным в течение указанного времени.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def header(self) -> WebElement:
        return self.is_visible(BasePageLocators.HEADER)

    def hold_mouse_on_element(self, locator):
        ActionChains(self.driver).move_to_element(self.is_visible(locator)).perform()

    def is_invisible(self, locator: tuple, timeout: int = 10) -> WebElement:
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))