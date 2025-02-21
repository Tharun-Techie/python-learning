import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.get_by_role("heading", name=":00 am").click()

    # ---------------------
    context.close()
    browser.close()
    
    


with sync_playwright() as playwright:
    run(playwright.chromium)
