from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)
print(driver.capabilities)
driver.quit()
