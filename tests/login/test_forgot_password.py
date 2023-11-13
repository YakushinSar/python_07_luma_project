from pages.account.sign_in import ForgotPage
from pages.login.forgot_password_page import ForgotPasswordPage
# from pages.login.forgot_password_page import ForgotPasswordPage
from locators.login_page_locators import ResetPageLocators, LoginPageLocators, ForgotPasswordPageLocators
import pytest


def test_link_forgot_password(driver):
    page = ForgotPasswordPage(driver, url=LoginPageLocators.URL)
    page.open()
    page.button_forgot_password().click()
    text = page.verify_text_forgot_password()
    assert text == ForgotPasswordPageLocators.TEXT, f'Expected result: {ForgotPasswordPageLocators.TEXT}, but got: {text}'


@pytest.mark.parametrize('test_email', ["test@com", "test@tescom", "test.com", 'test@'])
def test_email_not_valid_format(driver, test_email):
    page = ForgotPasswordPage(driver, url=LoginPageLocators.URL)
    page.open()
    page.button_forgot_password().click()
    email = page.email_fild_with_not_valid_format()
    email.clear()
    email.send_keys(test_email)
    page.button_reset_password().click()
    error_text = page.error_email_text()
    assert error_text == ForgotPasswordPageLocators.TEXT_WRONG_EMAIL, f'Expected result: {ForgotPasswordPageLocators.TEXT_WRONG_EMAIL}, but got: {error_text}'

@pytest.mark.parametrize('test_email', ["test@test.com", "test123@tes.com"])
def test_email_valid_format(driver, test_email):
    page = ForgotPasswordPage(driver, url=LoginPageLocators.URL)
    page.open()
    page.button_forgot_password().click()
    email = page.email_fild_with_not_valid_format()
    email.clear()
    email.send_keys(test_email)
    page.button_reset_password().click()
    message = page.text_after_reset_email()
    assert message == ForgotPage.SUCCESS % test_email, (f'Expected result: {ForgotPage.SUCCESS % test_email}, '
                                                        f'but got: {message}')
    # assert message == LoginPageLocators.RESET_PASS_MESS, f'Expected result: {LoginPageLocators.RESET_PASS_MESS}, but got: {message}'

