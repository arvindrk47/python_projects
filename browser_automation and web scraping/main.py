from selenium import webdriver
import time

def get_demo():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://www.codechef.com/login?destination=/")
  return driver


def main():
    driver= get_demo()
    time.sleep(10)
    driver.find_element(by="name", value="name").send_keys("arvindrk47@outlook.com")


print(main())