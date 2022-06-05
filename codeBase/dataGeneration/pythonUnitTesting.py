#from __future__ import print_function
import os

from webPageCrawler import writeToTxtFile, httpStatusOfAllLinks

# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

sender_email_id = "4466vijay@gmail.com"
sender_email_id_password = "*******"
receiver_email_id = "contactvijay777@gmail.com"

# Authentication
s.login(sender_email_id, sender_email_id_password) # smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted.

# message to be sent
message = "Its a test msg."

# sending the mail
s.sendmail("sender_email_id", receiver_email_id, message)

# terminating the session
s.quit()













#def getAllLinkStatus():  #WIP need to chk hoe to iterate over each url and chk for none urls
print(os.getcwd())
with open("aLinks.csv") as f:
    url_lst = f.read().split()
    writeToTxtFile("urlsToList_WIP.csv", str(url_lst))
    print(url_lst)
    httpStatusOfAllLinks(url_lst)

import re

# COde to get all website urls from a string
def Find(string):
    # findall() has been used  with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]
# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))