import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from explicity_wait import ExplicitWaitType





class Automation:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.baseUrl = "https://tienda.bigauto.solutionslion.com/mx/"
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(0.7)
        self.wait = ExplicitWaitType(self.driver)
        self.lista_numeros = []
        self.nuevo_titulo = ""
        self.abecedario = [""]


    def buscar(self, titulo):
        element = self.wait.waitForElement(locator="#newsletter_block_popup > div > button > i", locatorType="css")
        self.wait.elementClick(element)
        element_buscador = self.wait.waitForElement(locator="search-input")
        self.wait.sendKeys(titulo,element_buscador)
        self.wait.enter(element_buscador)
        element_resultado = self.wait.waitForElement(locator='//*[@id="js-product-list-top"]/div[1]/p', locatorType='xpath')
        texto_resultado = self.wait.get_text(element_resultado)
        element_inicio = self.wait.waitForElement(locator='//*[@id="header"]/div[3]/div/div/div[1]/a', locatorType='xpath')
        self.wait.elementClick(element_inicio)
        return texto_resultado

    def generar_palabra(self):
        self.nuevo_titulo = ""
        for _ in range(1):
            self.nuevo_titulo += random.choice(self.abecedario)
            # self.nuevo_titulo += ""
        print(self.nuevo_titulo)
        return self.nuevo_titulo

    def cerrar(self):
        self.driver.close()

