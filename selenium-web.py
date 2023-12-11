from selenium import webdriver

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe")

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/")
assist=infow()
assist.get_infow
