
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout_with_valid_details(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.get("https://www.saucedemo.com/")

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Add product to cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    # Open cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Proceed to checkout
    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # Enter customer details
    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Akhila")

    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "postal-code").send_keys("560001")
    driver.find_element(By.ID, "continue").click()

    # Verify checkout overview
    wait.until(EC.url_contains("/checkout-step-two.html"))

    assert "/checkout-step-two.html" in driver.current_url
    assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 1


def test_checkout_with_empty_first_name(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.get("https://www.saucedemo.com/")

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Add product and open cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Open checkout
    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # Leave first name empty
    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )

    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "postal-code").send_keys("560001")
    driver.find_element(By.ID, "continue").click()

    # Verify the validation error
    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "First Name is required" in error.text

def test_checkout_with_empty_last_name(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.get("https://www.saucedemo.com/")

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Add product and open cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Open checkout
    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # Enter first name and postal code, leaving last name empty
    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Akhila")

    driver.find_element(By.ID, "postal-code").send_keys("560001")
    driver.find_element(By.ID, "continue").click()

    # Verify validation error
    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "Last Name is required" in error.text

def test_checkout_with_empty_postal_code(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.get("https://www.saucedemo.com/")

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Add product and open cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Open checkout
    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # Enter first and last names, leaving postal code empty
    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Akhila")

    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "continue").click()

    # Verify validation error
    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "Postal Code is required" in error.text

def test_checkout_with_empty_postal_code(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    # Login
    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Add product and open cart
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Start checkout
    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # Enter first and last names, leaving postal code empty
    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Akhila")

    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "continue").click()

    # Verify the validation message
    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "Postal Code is required" in error.text


