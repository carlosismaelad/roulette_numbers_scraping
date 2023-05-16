import dotenv
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

env = dotenv.dotenv_values(".env")

class LoginEstrelabet:
    def __init__(self):      
      self.user = env["user"]
      self.password = env["password"]

      service = Service('./chromedriver')
      self.driver = webdriver.Chrome(service=service)

    
    def AccessEstrela(self):
      try:
        # Abre o site e efetua o login
        self.driver.get("https://estrelabet.com/ptb/bet/main")
        input_user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='username']")))
        actions = ActionChains(self.driver)
        actions.move_to_element(input_user).perform()
        input_user.click()
        input_user.send_keys(self.user)
        
        input_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='password-login']")))
        input_password.click()
        input_password.send_keys(self.password)
       
        button_login = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='hdr-login-btn sign-in-btn']")))
        button_login.click()
        
        # Navega no site a procura da sessão desejada       
        button_live_casino = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@routerlinkactive='active' and @href='/ptb/games/livecasino']")))
        button_live_casino.click()
        
        button_vendor = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'vendor-title flex-item') and contains(text(), 'Fornecedor')]")))
        button_vendor.click()
        
        button_pragmatic_play = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'type truncate') and contains(text(), 'Pragmatic Play')]")))
        button_pragmatic_play.click()
       
        button_roulette = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'text flex-item') and contains(text(), 'Roleta')]")))
        button_roulette.click()
        

        # Localiza um card de roleta
        auto_roulette = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@class='gm-img']")))
        # move o mouse sobre ele para que apareça o elemento oculto
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.move_to_element(auto_roulette).perform()
        hidden_element = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.XPATH, "//a[@class='btn real' and contains(text(), 'Jogar agora')]")))        
        hidden_element.click()               
        time.sleep(20)

        # Seleciona o botão que estiver visível antes do botão "Todos os jogos"
        try:            
            btn_ok = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary promo-optbtn okbtn']")))
            btn_ok.click()        
        except NoSuchElementException:
            try:            
                btn_no_thanks = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//button[@class='pp_desktopBTN2']")))
                btn_no_thanks.click()
            except NoSuchElementException:
               print("Nenhum borão de fechamento de popup encontrado")
               
            
        try:
            all_games = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "homeId")))
            all_games.click()
        except NoSuchElementException:
           print("Botão 'Todos os jogos' não localizado")

            
        
        

      finally:
        self.driver.quit()



access = LoginEstrelabet()
access.AccessEstrela()