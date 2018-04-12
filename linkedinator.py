from selenium import webdriver

linksArray = []

driver = webdriver.Chrome("webdriver/chromedriver.exe")

#login process
driver.get("https://www.linkedin.com/")

#typing email
## coloque o email do seu LinkedIn
loginEmail = driver.find_element_by_id("login-email")
loginEmail.click()
loginEmail.send_keys('SEU_EMAIL')

#typing password
## coloque a senha do seu LinkedIn
loginPass = driver.find_element_by_id("login-password")
loginPass.click()
loginPass.send_keys('SUA_SENHA')

#submitting
loginButton = driver.find_element_by_id("login-submit")
loginButton.click()

#visiting links
for link in linksArray:
    try:
        # go to url
        driver.get(link)
        driver.implicitly_wait(3)
        # finding connect button
        connectButton = driver.find_element_by_class_name("pv-s-profile-actions--connect")
        connectButton.click()
        # finding Add a note button
        addNote = driver.find_element_by_css_selector(".button-secondary-large.mr1")
        addNote.click()
        # have no idea why it's here
        div = driver.find_element_by_class_name("send-invite__actions")
        # finding text area to write into
        textArea = driver.find_element_by_id("custom-message")
        textArea.click()
        ## COLOQUE AQUI A SUA MENSAGEM!
        textArea.send_keys("Ola, eu sou do CodeXP!")
        sendButton = driver.find_element_by_css_selector(".button-primary-large.ml1")
        sendButton.click()
        driver.implicitly_wait(3)
    except Exception :
        ## Loga os enderecos que, por algum motivo, deram problema
        print(link)
        continue
    print("O programa terminou")

driver.quit()
