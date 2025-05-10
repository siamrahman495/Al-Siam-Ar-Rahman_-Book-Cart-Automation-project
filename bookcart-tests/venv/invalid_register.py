from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to site and register
    page.goto("https://bookcart.azurewebsites.net/")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Register").click()
    page.get_by_placeholder("First name").fill("Al Siam")
    page.get_by_placeholder("Last Name").fill("Rahman")
    page.get_by_placeholder("User name").fill("siam495")
    page.get_by_placeholder("Password", exact=True).fill("siamim7139@@@A")
    page.get_by_placeholder("Confirm Password").fill("siamim7139@@@A")
    page.get_by_label("Male", exact=True).check()
    page.get_by_role("button", name="Register").click()

    # Login
    page.get_by_placeholder("Username").fill("siam495")
    page.get_by_placeholder("Password").fill("siamim7139@@@A")
    page.get_by_role("button", name="Login").click()

    # Search and filter
    page.get_by_text("Biography", exact=True).click()
    page.get_by_text("Fiction").click()
    page.get_by_text("Mystery").click()
    page.get_by_text("Fantasy").click()
    page.get_by_text("Romance").click()

    # Search a book and add to cart + wishlist
    page.get_by_placeholder("Search books or authors").fill("The Hookup")
    page.get_by_role("option", name="The Hookup").click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("button", name="Add to Wishlist").click()

    # View wishlist and cart, then clear both
    page.get_by_role("button", name="Clear Wishlist").click()
    page.get_by_role("button", name="shopping_cart2").click()
    page.get_by_role("button", name="Clear cart").click()

    # Add other books to cart
    page.get_by_role("button", name="Book Cart").click()
    page.locator("mat-card-content").filter(has_text="Harry Potter").nth(0).get_by_role("button").click()
    page.locator("mat-card-content").filter(has_text="Slayer").nth(0).get_by_role("button").click()

    # My Orders and Logout
    page.get_by_text("account_circlearrow_drop_down").click()
    page.get_by_role("menuitem", name="My Orders").click()
    page.get_by_text("account_circlearrow_drop_down").click()
    page.get_by_role("menuitem", name="Logout").click()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
