from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bookcart.azurewebsites.net/")
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Username").fill("siam495")
    page.get_by_placeholder("Password").fill("siamim7139@@@A")
    page.get_by_role("button", name="Login").nth(1).click()
    expect(page.get_by_text("BookCart")).to_be_visible()
    page.get_by_role("button", name="Book Cart").click()
    expect(page.get_by_text("Your cart is empty")).to_be_visible()
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
