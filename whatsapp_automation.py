from selenium import webdriver

driver = webdriver.Chrome ()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("Enter name or group Name:")
msg = input("Enter message:")
count= int(input("Enter the counts:"))

input("Enter done after scanning the QR")

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for index in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
        button.click()

print("Success")