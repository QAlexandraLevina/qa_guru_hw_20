import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_getting_started():
    """Поиск Onboarding"""
    with allure.step("Проверяем наличие модального окна"):
        try:
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Ok")).click()
        except:
            pass
    try:
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).should(be.visible)
        with allure.step("Проверка onboarding экранов"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.exact_text("The Free Encyclopedia"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/addLanguageButton")).should(have.text("Add or edit languages"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("New ways to explore"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("Reading lists with sync"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("Data & Privacy"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()
    except:
        with allure.step("Проверка поиска на главном экране"):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Java")