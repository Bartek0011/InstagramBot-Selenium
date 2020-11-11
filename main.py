from selenium import webdriver
import time
from sec import passd


class IgBot:
    def __init__(self, username):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        time.sleep(0.2)
        self.driver.find_element_by_xpath('//button[contains(text(), "Akceptuję")]').click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(passd)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        try:
            code = int(input('Input:'))
            self.driver.find_element_by_xpath("//input[@name=\"verificationCode\"]").send_keys(code)
        except ValueError:
            print('not a number')
        time.sleep(0.3)
        self.driver.find_element_by_xpath('//button[contains(text(), "Potwierdź")]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//button[contains(text(), "Nie teraz")]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//button[contains(text(), "Nie teraz")]').click()
        time.sleep(2)

    def not_follow_back(self):  # who is not follow you back
        following = self._get_following()
        followers = self._get_followers()
        # following = self._get_following()
        names = [name for name in following if name not in followers]
        print(names)

    def _get_names(self):
        scroll_area = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        height, last_height = 1, 0
        while height != last_height:
            last_height = height
            time.sleep(0.6)
            height = self.driver.execute_script('''arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;''', scroll_area)
        links = scroll_area.find_elements_by_tag_name('a')
        print(links)
        names = [name.text for name in links if name.text != '']
        time.sleep(0.2)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
        time.sleep(0.2)
        return names

    def _get_followers(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[2]').click()
        time.sleep(0.2)
        return self._get_names()

    def _get_following(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[3]').click()
        time.sleep(0.2)
        return self._get_names()


bot = IgBot('')  # type your username or email here

