from EmailSender import EmailSender
import pandas

# Read Emails
contact_emails = pandas.read_csv("./Recipients_list.csv")
Emails = contact_emails["Email"].to_list()

# text- This is a list, 1st element will be in normal font, 2nd element will be in bold, 3rd element will in normal font ....
# For Line gaps and all used """ """ comment and define the element
text = ["normal text", "Bold text"]

# Send Emails
mailer = EmailSender(sender_email=" ", sender_password=" ",
                     mail_subject=" ", mail_body=text)
mailer.send_mails(driver_path="./chromedriver.exe", emails=Emails)
