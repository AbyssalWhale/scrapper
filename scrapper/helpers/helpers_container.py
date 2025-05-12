from playwright.sync_api import Playwright

from helpers.helper_run_config import HelperRunConfig
from helpers.helper_system import HelperSystem


class HelpersContainer:
    def __init__(self, playwright: Playwright):
        self.system = HelperSystem()
        self.config = HelperRunConfig(self.system)