from playwright.sync_api import Playwright, sync_playwright


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
    page.locator("mat-card").filter(has_text="favorite Harry Potter and the Prisoner of Azkaban₹213.00shopping_cart Add to").get_by_label("Book title").click()
    page.get_by_role("button", name="Remove from Wishlist").click()
    page.get_by_text("account_circlearrow_drop_down").click()
    page.get_by_role("menuitem", name="Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
