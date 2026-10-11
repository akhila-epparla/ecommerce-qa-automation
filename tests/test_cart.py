

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def login(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID, "login-button"
    ).click()

    # Wait until the inventory page is fully loaded
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    # Verify that the expected page loaded
    assert "/inventory.html" in driver.current_url

def test_add_product_to_cart(driver):
    """Verify that a product can be added to the cart."""
    login(driver)

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    wait = WebDriverWait(driver, 10)

    cart_badge = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert cart_badge.text == "1"



def test_remove_product_from_cart(driver):
    login(driver)

    wait = WebDriverWait(driver, 10)

    # Add a product
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()

    # Open the cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )
    ).click()

    # Wait for the product to appear
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    # Click Remove
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "remove-sauce-labs-backpack")
        )
    ).click()

    # Wait until no cart items remain
    wait.until(
        lambda d: len(
            d.find_elements(By.CLASS_NAME, "cart_item")
        ) == 0
    )

    # Verify that the cart is empty
    assert len(
        driver.find_elements(By.CLASS_NAME, "cart_item")
    ) == 0
