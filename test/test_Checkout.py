import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from pages.checkout_Page import ShoppingCart

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")             #membuka chrome dalam mode incognito
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--log-level=3")  # 0=INFO, 1=WARNING, 2=ERROR, 3=FATAL
    driver = webdriver.Chrome(options=options)
    driver.maximize_window() #maximize ukuran windows
    yield driver
    driver.quit()

# contoh implementasi field input dengan DDT sederhana
test_data = [
    ("3", "Jhon Doe", "mail@mail.co", "08888", "Konoha", "Jakarta Selatan", "12345", "success")
]

class TestCheckout:
    @pytest.mark.parametrize("MidTransPillow, Name, Email, PhoneNo, City, Address, PostalCode, expected", test_data)
    def test_checkout(self, driver, MidTransPillow, Name, Email, PhoneNo, City, Address, PostalCode, expected):
        checkout_Page = ShoppingCart(driver)
        checkout_Page.load()
        checkout_Page.Button_BuyNow()
        # input field
        checkout_Page.Field_ShoppingCart(
        MidTransPillow,
        Name,
        Email,
        PhoneNo,
        City,
        Address,
        PostalCode
    )
        time.sleep(3)
        
        checkout_Page.Button_CheckOut()
        checkout_Page.switch_to_snap()

        checkout_Page.PaymentMethod()
        # payment method dengan VA BRI
        checkout_Page.VA_BRI()
        checkout_Page.Button_CheckStatus()
        time.sleep(3)
        checkout_Page.Button_CloseX()
        # assertion untuk memastikan pesanan sudah dibuat
        assert "We've booked your payment." in driver.page_source
        print ("\nberhasil assert")