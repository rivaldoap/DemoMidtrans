from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver

    # untuk handle iframe
    def switch_to_snap(self):
        WebDriverWait(self.driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "snap-midtrans"))
        )
    def wait_snap_iframe(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "snap-midtrans"))
        )
    
    # untuk menghapus default input
    def clear_and_type(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(value)
        
    def select_all_without_delete(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(value)
    
    #Membuka website
    def load(self):
        self.driver.get("https://demo.midtrans.com/")
    
    def Button_BuyNow(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='BUY NOW']"))
        ).click()
    
    def switch_to_snap(self):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "snap-midtrans"))
        )

    FIELD_MIDTRANSPILLOW               = (By.XPATH, "(//input[@type='number' and contains(@class,'text-right')])[1]")
    FIELD_NAME                         = (By.XPATH, "(//input[@type='text'])[1]")
    FIELD_EMAIL                        = (By.XPATH, "//input[@type='email']")
    FIELD_PHONE                        = (By.XPATH, "(//input[@type='text'])[2]")
    FIELD_CITY                         = (By.XPATH, "(//input[@type='text'])[3]")
    FIELD_ADDRESS                      = (By.XPATH, "(//textarea)[1]")
    FIELD_POSTAL                       = (By.XPATH, "(//input[@type='text'])[4]")

    def Field_ShoppingCart(self, midtranspillow, name, email, phone, city, address, postal):
        self.select_all_without_delete(self.FIELD_MIDTRANSPILLOW, midtranspillow)
        self.clear_and_type(self.FIELD_NAME, name)
        self.clear_and_type(self.FIELD_EMAIL, email)
        self.clear_and_type(self.FIELD_PHONE, phone)
        self.clear_and_type(self.FIELD_CITY, city)
        self.clear_and_type(self.FIELD_ADDRESS, address)
        self.clear_and_type(self.FIELD_POSTAL, postal)

    def Button_CheckOut(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='cart-checkout']"))
        ).click()
    
    def PaymentMethod(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='bank_transfer']//div[@class='collapsible-payment--multiple__title']"))
        ).click()
    def VA_BRI(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='#/bank-transfer/bri-va']//div[@class='payment-page-text horizontal']//div[@class='bank-list-content']//div[@class='bank-logo-wrapper horizontal']//*[name()='svg']"))
        ).click()

    def Button_CheckStatus(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='button']"))
        ).click()
    def Button_CloseX(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='header']/div[1]/div[2]"))
        ).click()