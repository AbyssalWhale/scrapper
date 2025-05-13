import pytest
from playwright.sync_api import Playwright, Locator, Page
from pytest_playwright.pytest_playwright import playwright, browser

from enums.framework.enums_framework_config_properties import EnumsFrameworkConfigProperties
from helpers.helpers_container import HelpersContainer


@pytest.fixture(scope="session")
def onetime_set_up(playwright: Playwright):
    helpers = HelpersContainer(playwright)
    proj_dir = helpers.system.get_project_dir()
    data_dir = helpers.config.get_property_value(EnumsFrameworkConfigProperties.DIR_DATA)

    yield helpers

    helpers.playwright.close()

@pytest.fixture(scope="function")
def set_up(onetime_set_up):
    yield onetime_set_up.playwright

def test_simple(set_up):
    page = set_up.page
    page.goto("")
    clickWhileExists(page.locator("//span[text()='Load More']"))

def clickWhileExists(element: Locator):
    is_visible = True
    while is_visible:
        try:
            if element.is_visible():
                element.click()
                element.wait_for(timeout=2000, state="visible")
        except:
            is_visible = False




