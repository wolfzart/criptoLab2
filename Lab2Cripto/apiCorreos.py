import requests
import json

def generateEmail():
    url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
    response = requests.get(url)
    data = json.loads(response.text)
    return data[0]

def readMails(mail):
    user = mail.split('@')[0]
    domain = mail.split('@')[1]
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def readMail(mail,id):
    user = mail.split('@')[0]
    domain = mail.split('@')[1]
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={domain}&id={id}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data