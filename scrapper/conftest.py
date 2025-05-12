import pandas as pd
import pytest
from bs4 import BeautifulSoup
from playwright.sync_api import Playwright, Locator, Page
from pytest_playwright.pytest_playwright import playwright, browser

from helpers.helpers_container import HelpersContainer


@pytest.fixture(scope="session")
def onetime_set_up(playwright: Playwright):
    helpers = HelpersContainer(playwright)
    proj_dir = helpers.system.get_project_dir()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    yield page

    page.close()
    context.close()
    browser.close()

def test_simple(onetime_set_up):
    page = onetime_set_up
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




