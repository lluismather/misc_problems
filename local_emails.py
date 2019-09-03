import os
import unicodedata
import pandas as pd
import win32com.client as win32
from bs4 import BeautifulSoup as soup

# create outlook class
outlook = win32.Dispatch("Outlook.Application")
mail_folder = outlook.GetNameSpace("MAPI")

# container for all mailing objects
mailings = []

# find subfolder
def find_folder(root, folder):
    for file in root.Folders:
        if file.Name == folder:
            return file
    return False

# get rid of uneccessary strings
def drop_string(text, string):
    temp = unicodedata.normalize("NFKD", text)
    temp = temp.replace("\n", "").replace("\r", "")
    if string in temp:
        temp = temp.split(string, 1)[1]
        temp = temp.replace(string, "")
    temp = temp.split(" <theteam> wrote:", 1)[0]
    return temp

# find all mailing items
def file_recurse(root):
    for item in root.Items:
        mailings.append(item)
    for file in root.Folders:
        file_recurse(file)

# root folder and subfolders
the_team_folder = find_folder(mail_folder, "theteam")
theteam = find_folder(the_team_folder, "Inbox")
file_recurse(theteam)


# main pandas df
pd_mail =  pd.DataFrame({"sender":[], "sent_dt":[], "subject":[], "text":[], "text_obj":[]})

# get mailings data and append to the dataframe
for item in mailings:
    sender_email = item.SenderEmailAddress
    if "EXCHANGELABS/OU=EXCHANGE ADMINISTRATIVE GROUP " not in sender_email:
        sent_time = str(item.ReceivedTime).replace("+00:00", "")
        mail_subject = item.Subject
        try:
            mail_html_raw = soup(item.HTMLBody, "html.parser")
            mail_html = drop_string(mail_html_raw.text)
            mail_text = drop_string(item.Body)
        except:
            mail_html = "NA"
            mail_text = "NA"
        
        # append data
        print(sender_email, sent_time, mail_subject, mail_html, mail_text)
        pd_mail = pd_mail.append(pd.DataFrame({"sender":[sender_email], "sent_dt":[sent_time], 
                                           "subject":[mail_subject], "text":[mail_html], "text_obj":[mail_text]}))

# save pandas dataframe
os.chdir("C:/Users/lmather/Desktop/")
export_csv = pd_mail.to_csv("export_dataframe.csv", index = None, header=True)
print(">>> export of emails complete...")

