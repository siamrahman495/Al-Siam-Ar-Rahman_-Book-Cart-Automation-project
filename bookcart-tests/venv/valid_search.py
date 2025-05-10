from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bookcart.azurewebsites.net/")
    page.click("button:has-text('Login')")
    page.fill("input[placeholder='Username']", "siam495")
    page.fill("input[placeholder='Password']", "siamim7139@@@A")
    page.click("button:has-text('Login')")
    page.fill("input[placeholder='Search books or authors']", "harr")
    page.press("input[placeholder='Search books or authors']", "Enter")
    page.click("text=Harry Potter and the Prisoner")
    page.click("button:has-text('Add to Cart')")
    page.click("button:has-text('shopping_cart')")
    page.click("text=account_circle")
    page.click("text=Logout")
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
