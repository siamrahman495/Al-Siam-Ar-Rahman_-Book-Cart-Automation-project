import time
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://bookcart.azurewebsites.net/")
    time.sleep(1)

    page.get_by_role("button", name="Login").click()
    time.sleep(1)

    page.get_by_placeholder("Username").fill("siam495")
    time.sleep(1)

    page.get_by_placeholder("Password").fill("siamim7139@@@A")
    time.sleep(1)

    page.locator("mat-card-actions").get_by_role("button", name="Login").click()
    time.sleep(2)

    page.locator("mat-card-content").filter(has_text="Curuk ve Harabe").get_by_role("button").click()
    time.sleep(1)

    page.locator("mat-card-content").filter(has_text="Roomies").get_by_role("button").click()
    time.sleep(1)

    page.locator("mat-card-content").filter(has_text="A Princess in Theory").get_by_role("button").click()
    time.sleep(1)

    page.locator("mat-card-content").filter(has_text="Wicked and the").get_by_role("button").click()
    time.sleep(1)

    page.locator("mat-card-content").filter(has_text="Dr. Strange Beard").get_by_role("button").click()
    time.sleep(1)

    page.locator("button").filter(has_text="shopping_cart13").click()
    time.sleep(1)

    page.get_by_text("account_circlearrow_drop_down").click()
    time.sleep(1)

    page.get_by_role("menuitem", name="Logout").click()
    time.sleep(1)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
