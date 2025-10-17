import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_getting_started():
    """Поиск Onboarding"""
    try:
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).should(be.visible)
        with allure.step("Проверка заголовка и кнопки добавления языка на первой странице и переход на следующую"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.exact_text("The Free Encyclopedia"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/addLanguageButton")).should(have.text("Add or edit languages"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
        with allure.step("Проверка заголовка второй страницы и переход на следующую"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("New ways to explore"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
        with allure.step("Проверка заголовка третьей страницы и переход на следующую"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("Reading lists with sync"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()
        with allure.step("Проверка заголовка четвёртой страницы и нажатие на кнопку 'Get Started'"):
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("Data & Privacy"))
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()
    except:
        with allure.step("Проверка поиска на главном экране"):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Java")