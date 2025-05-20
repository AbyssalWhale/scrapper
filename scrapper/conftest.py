import pytest
from playwright.sync_api import Playwright, Locator
from pytest_playwright.pytest_playwright import playwright

from enums.enum_scrapping_sources import EnumScrappingSources
from helpers.helpers_container import HelpersContainer
from models.model_source import ModelSource


@pytest.fixture(scope="session")
def onetime_set_up(playwright: Playwright):
    helpers = HelpersContainer(playwright)

    yield helpers

    helpers.playwright.close()

@pytest.fixture(scope="function")
def set_up(onetime_set_up):
    yield onetime_set_up

def test_simple(set_up):
    page = set_up.playwright.page
    source: ModelSource = set_up.config.get_source(EnumScrappingSources.HEINZ)
    page.goto(source.url)
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




