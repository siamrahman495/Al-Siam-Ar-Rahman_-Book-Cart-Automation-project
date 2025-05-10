from playwright.sync_api import Playwright, sync_playwright, expect
import time
import random

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

   
    unique_username = f"fakeid{random.randint(1000, 9999)}"

  
    page.goto("https://bookcart.azurewebsites.net/")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Register").click()
    time.sleep(1)  

    
    page.get_by_placeholder("First name").fill("Fake")
    page.get_by_placeholder("Last Name").fill("User")
    page.get_by_placeholder("User name").fill(unique_username)
    page.get_by_placeholder("Password", exact=True).fill("Fakeid12345@A")
    page.get_by_placeholder("Confirm Password").fill("Fakeid12345@A")
    page.get_by_label("Female").check()

    
    page.get_by_role("button", name="Register").click()
    page.wait_for_url("**/login", timeout=5000) 

    
    page.get_by_placeholder("Username").fill(unique_username)
    page.get_by_placeholder("Password").fill("Fakeid12345@A")
    page.get_by_role("button", name="Login").nth(1).click()


    time.sleep(3)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
