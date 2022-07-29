from email import message
import smtplib
# secured mail transfer protocol library

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# module in order to add a subject
def SendEmail():

    user = "automationtempproject@gmail.com"
    msg = """From:
    To:
    Subject: Item Added to Cart!
    This email is to notify you that you have ran out of bananas
    and they have been added to your Amazon cart for you to buy at
    the best of your convenience.
    Best,

    Your Smart Fridge
    """
    
    # make sure to include 3 lines with from, to, subject and then have another line in between subject and body
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.starttls()
    
    #will go through security
    mail.login("automationtempproject@gmail.com", "qikbyeevrmhboall")
    
    #use generated password for python from gmail
    mail.sendmail(user, user, msg)
    
    # user, receiver, message
    mail.quit()