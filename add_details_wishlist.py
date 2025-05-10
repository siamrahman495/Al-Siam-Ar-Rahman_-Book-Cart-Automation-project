from playwright.sync_api import Playwright, sync_playwright




def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bookcart.azurewebsites.net/")
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("siam495")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("siamim7139@@@A")
    page.locator("mat-card-content").click()
    page.locator("mat-card-actions").get_by_role("button", name="Login").click()
    page.locator("mat-card").filter(has_text="favorite Rot & Ruin₹123.").get_by_label("Book title").click()
    page.get_by_role("button", name="Add to Wishlist").click()
    page.locator("button").filter(has_text="favorite6").click()
    page.get_by_role("button", name="Clear Wishlist").click()
    page.get_by_role("button", name="Continue shopping").click()
    page.get_by_text("account_circlearrow_drop_down").click()
    page.get_by_role("menuitem", name="Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
