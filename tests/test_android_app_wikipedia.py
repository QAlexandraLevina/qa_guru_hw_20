import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from selenium.common import NoSuchElementException


def test_getting_started():
    """Поиск Onboarding"""
    with allure.step("Проверяем наличие модального окна"):
        try:
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Ok")).click()

        except NoSuchElementException:
            pass

    try:
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).should(be.visible)

        with allure.step("Проверка первого экрана"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.exact_text("The Free Encyclopedia"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/addLanguageButton")).should(have.text("Add or edit languages"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

        with allure.step("Проверка второго экрана"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("New ways to explore"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

        with allure.step("Проверка третьего экрана"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("Reading lists with sync"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

        with allure.step("Проверка четвёртого экрана"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("Data & Privacy"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()

    except NoSuchElementException:
        with allure.step("Проверка главного экрана"):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark')).should(be.visible)