from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to site and click login
    page.goto("https://bookcart.azurewebsites.net/")
    page.get_by_role("button", name="Login").click()

    # Fill login credentials
    page.get_by_placeholder("Username").fill("siam495")
    page.get_by_placeholder("Password").fill("siamim7139@@@A")  # ✅ Correct password
    page.get_by_role("button", name="Login").click()

    # Optional: Wait or assert something to verify login succeeded
    page.wait_for_timeout(3000)  # Wait 3 seconds to see result

    # Close browser
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
