import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bookcart.azurewebsites.net/")
    page.get_by_role("button", name="Login").click()
    page.locator(".mat-mdc-form-field-infix").first.click()
    page.get_by_placeholder("Username").fill("siam495")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("siamim7139@@@A")
    page.locator("mat-card-actions").get_by_role("button", name="Login").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name=" GitHub").click()
    page1 = page1_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
