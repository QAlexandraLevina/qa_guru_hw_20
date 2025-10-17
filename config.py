import os
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv


load_dotenv('.env.credentials')

def to_driver_options(context):
    options = UiAutomator2Options()
    if context == 'local_emulator':
        options.set_capability('remote_url', os.getenv('LOCAL_REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))

    if context == 'bstack':
        options.set_capability('fullReset', 'true')
        options.set_capability('noReset', 'false')
        options.set_capability('autoGrantPermissions', 'true')
        options.set_capability('remote_url', os.getenv('BS_REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))
        options.set_capability(
        'bstack:options',{
                    "projectName": "Wikipedia project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack test",
                    "userName": os.getenv('BS_USER_NAME'),
                    "accessKey": os.getenv('BS_ACCESS_KEY'),
        },
        )
    return options