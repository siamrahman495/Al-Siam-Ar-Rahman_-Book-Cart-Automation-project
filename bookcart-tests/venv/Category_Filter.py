from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://bookcart.azurewebsites.net/")
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Username").fill("siam495")
    page.get_by_placeholder("Password").fill("siamim7139@@@A")
    page.get_by_role("button", name="Login").click()

    page.get_by_text("Biography").click()
    page.get_by_role("slider").click()
    for _ in range(10):
        page.keyboard.press("ArrowRight")

    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_text("account_circlearrow_drop_down").click()
    page.get_by_role("menuitem", name="Logout").click()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
