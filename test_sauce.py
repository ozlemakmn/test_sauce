from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class Test_Login:
    def setup_method(self):#her testen önce çağrılır.
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
    def teardown_method(self):
        self.driver.quit() 
        
    
 

    @pytest.mark.parametrize("username, password", [("1","1"),("abc","123"),("standard_user","secret_sauce")])    
    def test_giris(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"user-name")))
        usernameInput= self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,'password')
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginbuton=self.driver.find_element(By.ID,"login-button")
        loginbuton.click()
        errormessage=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errormessage.text == "Epic sadface: Username is required" 
        
    def test_bosgecis(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = self.driver.find_element(By.ID,'user-name')
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,'password')
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"pair5")
        actions.send_keys_to_element(passwordInput,"")
        loginButton = self.driver.find_element(By.ID,'login-button')
        loginButton.click()
        errormessage=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errormessage.text == "Epic sadface: Password is required" 
        
    
    
    def test_gecis(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"user-name")))
        usernameInput= self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,'password')
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"locked_out_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginbuton=self.driver.find_element(By.ID,"login-button")
        loginbuton.click()
        errormessage=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errormessage.text == "Epic sadface: Sorry, this user has been locked out."    
    
    def test_gecis1(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"user-name")))
        usernameInput= self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,'password')
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginbuton=self.driver.find_element(By.ID,"login-button")
        loginbuton.click()
        products=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_item_description")))
        print(f"{len(products)} adet ürün vardır")