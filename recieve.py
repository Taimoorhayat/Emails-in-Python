
##Overview of Received Emails
##Now that we understand how to send emails progammatically with Python, 
##let's explore how we can read and search recieved emails. To do we will use the built-in imaplib library. We will also use the built in email 
##library for parsing through the recieved emails.

import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
import getpass
user = input("Enter your email: ")

# Remember , you may need an app password if you are a gmail user
# 
password = getpass.getpass("Enter your password: ")

M.login(user,password)

M.list()


# Connect to your inbox
M.select("inbox")


##You can also use the logical operators AND and OR to combine the above statements. Check out the full list of search keys 
##here: http://www.4d.com/docs/CMU/CMU88864.HTM.

##Please note that some IMAP server providers for different email services will have slightly different syntax. You may need to experiment to get the 
##results you want.

