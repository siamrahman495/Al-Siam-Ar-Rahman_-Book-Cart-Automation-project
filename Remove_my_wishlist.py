from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Login
    page.goto("https://bookcart.azurewebsites.net/")
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Username").fill("siam495")
    page.get_by_placeholder("Password").fill("siamim7139@@@A")
    page.locator("mat-card-actions").get_by_role("button", name="Login").click()

    # Add 3 books to wishlist
    time.sleep(2)
    page.locator("mat-card-content").filter(
        has_text="Harry Potter and the Chamber of Secrets"
    ).locator("span").first.click()

    page.locator("mat-card-content").filter(
        has_text="Harry Potter and the Prisoner of Azkaban"
    ).locator("span").first.click()

    page.locator("mat-card-content").filter(
        has_text="Harry Potter and the Goblet of Fire"
    ).locator("span").first.click()

    # Open wishlist
    page.locator("button").filter(has_text="favorite3").click()

    # Logout
    page.get_by_text("account_circlearrow_drop_down").click()
    page.get_by_role("menuitem", name="Logout").click()

    # Re-login
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Username").fill("siam495")
    page.get_by_placeholder("Password").fill("siamim7139@@@A")
    page.locator("mat-card-actions").get_by_role("button", name="Login").click()

    # Re-open wishlist and remove items
    page.locator("button").filter(has_text="favorite3").click()
    time.sleep(2)
    remove_buttons = page.get_by_role("button", name="Remove from Wishlist")
    if remove_buttons.count() >= 2:
        remove_buttons.nth(0).click()
        time.sleep(1)
        remove_buttons.nth(1).click()

    # Final logout
    page.get_by_text("account_circlearrow_drop_down").click()
    page.get_by_role("menuitem", name="Logout").click()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
