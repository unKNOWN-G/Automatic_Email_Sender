from selenium import webdriver
from time import sleep


def bolder(driver: webdriver):
    driver.find_element_by_css_selector('.aaA.eN').click()


def login(driver: webdriver, sender_email: str, sender_password: str) -> None:
    # Open Gmail Page
    driver.get("http://www.gmail.com")
    sleep(2)

    # Logging in
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(sender_email)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(sender_password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
    sleep(7)


def send_single_mail(driver: webdriver, email: str, email_subject: str, email_body: list) -> None:
    # Compose button
    try:
        driver.find_element_by_css_selector('.z0>.L3').click()
    except IndexError:
        driver.find_element_by_css_selector('.z0>.L3::before').click()
    sleep(1)

    # Input Recipient
    driver.find_element_by_css_selector(".oj div textarea").send_keys(email)
    sleep(0.5)

    # Input Subject
    driver.find_element_by_css_selector(".aoD.az6 input").send_keys(email_subject)
    sleep(0.5)

    # Input Text
    if(len(email_body)>1):
        for i in range(len(email_body)):
            driver.find_element_by_css_selector(".Ar.Au div").send_keys(email_body[i])
            bolder(driver)
    else:
        driver.find_element_by_css_selector(".Ar.Au div").send_keys(email_body[0])
    sleep(0.5)

    # Send Button
    driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.T-I-atl.L3").click()
    sleep(0.5)

    print("Email Sent to " + email)


class EmailSender:
    def __init__(self, sender_email: str, sender_password: str, mail_subject: str, mail_body: list):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.subject = mail_subject
        self.body = mail_body

    def send_mails(self, driver_path: str, emails: list) -> None:
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()
        login(driver, self.sender_email, self.sender_password)
        for i in range(len(emails)):
            send_single_mail(driver, emails[i], self.subject, self.body)

        sleep(2)
        # Close Browser
        driver.close()
