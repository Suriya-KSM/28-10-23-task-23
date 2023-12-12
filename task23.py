from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

class KSM:

    def __init__(self):
        self.url = "https://jqueryui.com/droppable/"
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def Drag_and_Drop(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

            #Switching to iframe
            Frame = self.driver.find_element(by=By.CSS_SELECTOR, value='iframe.demo-frame')
            self.driver.switch_to.frame(Frame)

            #Drag and Drop using ActionChains
            Do = ActionChains(self.driver)
            Source = self.driver.find_element(by=By.CSS_SELECTOR, value='div#draggable.ui-widget-content.ui-draggable.ui-draggable-handle')
            Target = self.driver.find_element(by=By.CSS_SELECTOR, value='div#droppable.ui-widget-header.ui-droppable')
            Do.drag_and_drop(source=Source, target=Target).perform()
            sleep(3)
        except NoSuchElementException as selenium_error:
            print(selenium_error)

    def Shutdown(self):
        sleep(2)
        self.driver.close()

Obj=KSM()
Obj.Drag_and_Drop()
Obj.Shutdown()