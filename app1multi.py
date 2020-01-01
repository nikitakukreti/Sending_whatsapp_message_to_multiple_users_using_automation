from selenium import webdriver

driver=webdriver.Chrome(executable_path='C:\\Users/Nikita/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('http://web.whatsapp.com')
y="y"
while y=="y":
    name=[input("Enter the name of the user or group : ")]
    msg=input("Enter the message to be sent : ")
    count=int(input("Enter the count : "))

    #Scan the code before processing
    input("Enter anything after scanning QR code")

    user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()
    msg_box=driver.find_element_by_class_name('_2S1VP')
    for x in name:
        user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        for i in range(count):
            msg_box.send_keys(msg)
            driver.find_element_by_class_name('_35EW6').click()
        y=input("Enter y to re run the script")


