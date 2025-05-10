from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bookcart.azurewebsites.net/")
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Username").fill("sumi8997")
    page.get_by_placeholder("Password").fill("siamim7139@@@A")
    page.get_by_role("button", name="Login").click()

    try:
        expect(page.get_by_text("Book Cart")).to_be_visible(timeout=5000)
        print("✅ Login successful!")
    except:
        print("❌ Login failed. Check username or password.")

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
