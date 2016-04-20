from selenium import webdriver

class Twitter_Driver:
    def __init__(self):
        self.driver =webdriver.Firefox()
        self.driver.get("https://twitter.com/")
        self.islogIn = False

    def logIn(self, userName, password):
        self.driver.find_element_by_css_selector(".StreamsHero-buttonContainer .Button.StreamsLogin").click()
        user = self.driver.find_element_by_css_selector(".LoginForm input")
        user.send_keys(userName)

        contrasena = self.driver.find_element_by_name("session[password]")
        contrasena.send_keys(password)

        self.driver.find_element_by_class_name("js-submit").click()
        self.islogIn = True
    def twit(self, text):
        if self.islogIn:
            insertText = self.driver.find_element_by_name("tweet")
            insertText.send_keys(text)
            self.driver.find_element_by_css_selector(".tweet-form .tweet-btn").click()
        else:
            print "Logueate primero..."


if __name__ == "__main__":
    t1 = Twitter_Driver()
    t1.logIn("painEDU21@gmail.com", "verificacionMola")
    t1.twit("Hola gente de la interne")