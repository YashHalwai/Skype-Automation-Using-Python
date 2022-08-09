# Skype Automation Using Python

from skpy import Skype
import os.path #to send images

slogin = Skype("","") #mail #password

contact = slogin.contacts
ch = slogin.contacts[""] #id
with open("") as f: #location #name "/"
    contact.chat.sendFile(f,"",image=True) # "image name"


#group = slogin.chats.create(["",""]) #id

# contact = slogin.contacts
# contact = slogin.contacts[""] #id
# contact.chat.sendMsg("Welcome") #any message

# for i in contact:
#     print(i)
