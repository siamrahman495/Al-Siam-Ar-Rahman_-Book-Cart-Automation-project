import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bookcart.azurewebsites.net/")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("siam")
    page.locator("mat-form-field:nth-child(2) > .mat-mdc-text-field-wrapper > .mat-mdc-form-field-flex > .mat-mdc-form-field-infix").click()
    page.get_by_placeholder("Password").fill("siamim7139@@@A")
    page.locator("mat-card-actions").get_by_role("button", name="Login").click()
    page.locator("mat-card-actions").get_by_role("button", name="Login").click()
    page.get_by_text("visibility_off").click()
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("siam495")
    page.locator("mat-card-actions").get_by_role("button", name="Login").click()
    page.get_by_text("account_circlearrow_drop_down").click()
    page.get_by_role("menuitem", name="My Orders").click()
    page.get_by_text("account_circlearrow_drop_down").click()
    page.get_by_role("menuitem", name="Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
