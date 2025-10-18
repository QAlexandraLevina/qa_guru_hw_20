import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from selene.core.exceptions import TimeoutException


def test_getting_started():
        with allure.step("Проверка первого экрана"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("The Free Encyclopedia"))
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

        with allure.step("Проверка главного экрана"):
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark')).should(be.visible)