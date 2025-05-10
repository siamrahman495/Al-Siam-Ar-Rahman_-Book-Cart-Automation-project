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

    page.locator("mat-card").filter(has_text="Harry Potter and the Goblet of Fire").get_by_role("button", name="Add to Cart").click()
    page.locator("mat-card").filter(has_text="Harry Potter and the Deathly Hallows").get_by_role("button", name="Add to Cart").click()
    page.locator("mat-card").filter(has_text="Slayer").get_by_role("button", name="Add to Cart").click()
    page.locator("mat-card").filter(has_text="A Princess in Theory").get_by_role("button", name="Add to Cart").click()

    page.get_by_role("button", name="shopping_cart4").click()
    page.get_by_role("button", name="CheckOut").click()

    page.get_by_placeholder("Name").fill("abm")
    page.get_by_placeholder("Address Line 1").fill("Dhaka")
    page.get_by_placeholder("Address Line 2").fill("Sewrapara")
    page.get_by_placeholder("Pincode").fill("788996")
    page.get_by_placeholder("State").fill("Bangla")
    page.get_by_role("button", name="Place Order").click()

    page.get_by_text("account_circlearrow_drop_down").click()
    page.get_by_role("menuitem", name="Logout").click()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
