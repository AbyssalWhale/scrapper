from playwright.sync_api import Playwright

from enums.framework.enums_framework_config_properties import EnumsFrameworkConfigProperties
from helpers.helper_run_config import HelperRunConfig


class HelperPlaywright:
    def __init__(self, playwright: Playwright, config: HelperRunConfig):
        self.__config = config
        self.playwright = playwright
        self.browser = self.playwright.chromium.launch(
            headless=self.__config.get_property_value(EnumsFrameworkConfigProperties.IS_HEADLESS)
        )
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()