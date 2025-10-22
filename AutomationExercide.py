from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time

# Initialize the driver (Chrome in this example)
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to the website
driver.get("https://automationexercise.com/")
time.sleep(2)  # Let the homepage load

# Verify that home page is visible successfully
assert "Automation Exercise" in driver.title
print("Homepage loaded successfully.")
# Scroll down the page to make sure page loads further products/elements if necessary
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)


# Click on 'Category' -> 'Men'
men_category = driver.find_element(By.XPATH, "//a[normalize-space()='Men']")
men_category.click()
time.sleep(2)

# Click on 'Tshirts' under 'Men' category
tshirts_link = driver.find_element(By.XPATH, "//a[normalize-space()='Tshirts']")
tshirts_link.click()
time.sleep(2)

# Verify Men - Tshirts Products is visible
products_header = driver.find_element(By.XPATH, "//h2[contains(text(), 'Men - Tshirts Products')]")
assert products_header.is_displayed()
print("'Men - Tshirts Products' is visible.")

# Find the first product's 'Add to cart' button and click it
add_to_cart_btn = driver.find_element(By.XPATH, "(//a[contains(@class,'add-to-cart')])[1]")
add_to_cart_btn.click()
time.sleep(5)

# Click on the Contiinue Shopping Button
continue_shopping_btn = driver.find_element(By.XPATH, "//button[@class='btn btn-success close-modal btn-block']")
continue_shopping_btn.click()
time.sleep(2)

# Click on View Cart:
view_cart_btn = driver.find_element(By.XPATH, "//a[@href='/view_cart']")
view_cart_btn.click()
time.sleep(2)

# Wait until the cart items table is visible (this means items are loaded)
cart_table_locator = (By.XPATH, "//section[@id='cart_items']//table")
try:
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(cart_table_locator))
    print("Cart items are displayed.")
except Exception as e:
    print(f"Cart items did not load: {e}")


# Verify the Item, Description, Price, Quantity & Total data is not empty
# Locate the cart items table row (assuming only one product in the cart for this test)
cart_row = driver.find_element(By.XPATH, "//section[@id='cart_items']//table//tbody/tr")

# Get Item (image container/title)
item = cart_row.find_element(By.XPATH, "./td[@class='cart_product']/a/img")
description = cart_row.find_element(By.XPATH, "./td[@class='cart_description']")
price = cart_row.find_element(By.XPATH, "./td[@class='cart_price']")
quantity = cart_row.find_element(By.XPATH, "./td[@class='cart_quantity']")
total = cart_row.find_element(By.XPATH, "./td[@class='cart_total']")

# Check all the relevant fields are not empty
assert item.get_attribute("src"), "Item image src is empty"
assert description.text.strip() != "", "Description is empty"
assert price.text.strip() != "", "Price is empty"
assert quantity.text.strip() != "", "Quantity is empty"
assert total.text.strip() != "", "Total is empty"

print("Items added Perfectly")


#Click Proceed To Checkout
proceed_to_checkout_btn = driver.find_element(By.XPATH, "//a[@class='btn btn-default check_out']")
proceed_to_checkout_btn.click()
time.sleep(2)


# Click Register / Login button
register_login_btn = driver.find_element(By.XPATH, "//u[normalize-space()='Register / Login']")
register_login_btn.click()
time.sleep(2)


# Wait for the registration/login page to load by checking for a known element
try:
    reg_login_header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='login-form']//h2 | //div[@class='signup-form']//h2"))
    )
    print("Register/Login page loaded successfully.")
except Exception as e:
    print(f"Register/Login page did not load as expected: {e}")


#New User Signup!
#Random mail generator
random_email = random.choice(string.ascii_letters) + ''.join(random.choices(string.ascii_letters + string.digits, k=4)) + "@example.com"

#Name
driver.find_element(By.XPATH, "//input[@data-qa='signup-name']").send_keys("Test User")
time.sleep(1)

#Email
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(random_email)
time.sleep(1)

#Click the button Signup. XPATH: //button[normalize-space()='Signup']
driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()
time.sleep(2)


# Wait for the "ENTER ACCOUNT INFORMATION" text to be visible and verify its presence
enter_account_info = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//b[normalize-space()='Enter Account Information']"))
)
assert enter_account_info.is_displayed(), "'ENTER ACCOUNT INFORMATION' text is not visible"
time.sleep(2)

#Title
# Click the radio button for 'Mr.' Title
driver.find_element(By.XPATH, "//input[@id='id_gender1']").click()
time.sleep(1)

#password
# Generate a random password
random_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))

# Input the generated password in the Password field
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(random_password)
time.sleep(1)

#Date Of Birth
driver.find_element(By.XPATH, "//select[@id='days']/option[@value='5']").click()
time.sleep(1)
# Click and select the Month dropdown and then a specific month (e.g., May)
driver.find_element(By.XPATH, "//select[@id='months']/option[@value='5']").click()
time.sleep(1)
# Click and select the Year dropdown
driver.find_element(By.XPATH, "//select[@id='years']").click()
time.sleep(1)
# Click the "Sign up for our newsletter!" radio button
driver.find_element(By.XPATH, "//input[@id='newsletter']").click()
time.sleep(1)
# Click the "Receive special offers from our partners!" radio button
driver.find_element(By.XPATH, "//input[@id='optin']").click()
time.sleep(1)


# Fill First name field (required)
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("TestFirstName")
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("TestLastName")
driver.find_element(By.XPATH, "//input[@id='company']").send_keys("TestCompany")
driver.find_element(By.XPATH, "//input[@id='address1']").send_keys("123 Demo Street, TestDistrict")
driver.find_element(By.XPATH, "//input[@id='address2']").send_keys("Apartment 101, Demo Complex")
driver.find_element(By.XPATH, "//select[@id='country']/option[normalize-space()='Australia']").click()
driver.find_element(By.XPATH, "//input[@id='state']").send_keys("New South Wales")
driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Sydney")
driver.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("2000")
driver.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys("0412345678")
time.sleep(1)
driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']").click()
time.sleep(2)



#Wait for the next page to load
WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH, "//b[normalize-space()='Account Created!']"))
)

#Click the Continue button
driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
time.sleep(1)


# Wait until the homepage is loaded by checking the presence of a homepage element
WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Home')]"))
)

# Assert the website's title to confirm homepage
assert "Automation Exercise" in driver.title

print("Test Automation Completed.")
time.sleep(2)




# End the browser session for this demo
driver.quit()
