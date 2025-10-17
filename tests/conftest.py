import os
import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from appium import webdriver
import config as app_config
from utils.attachments import add_screenshot, add_xml, add_video


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Выбор окружения для запуска теста: local emulator (локальный эмулятор) или bstack (BrowserStack)"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"
    load_dotenv(dotenv_path=env_file_path)
    load_dotenv('.env.credentials')


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = app_config.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    session_id = browser.driver.session_id

    yield

    add_screenshot(browser)
    add_xml(browser)

    with allure.step("Закрытие браузера"):
        browser.quit()

    if context == 'bstack':
        add_video(session_id, os.getenv('BS_USER_NAME'), os.getenv('BS_ACCESS_KEY'))