from tkinter import *
from selenium import webdriver
from pyautogui import typewrite
from time import sleep

def login(client):
    window = Tk()
    window.title("Login Details")

    desc = Label(window, text="Enter your {} account details".format(client))
    desc.grid(row=0, columnspan=2)

    e = Label(window, text="Email")
    e.grid(row=1, column=0)
    
    email = Entry(window, width=32)
    email.grid(row=1, column=1)

    p = Label(window, text="Password")
    p.grid(row=2, column=0)
    
    passwd = Entry(window, width=32, show="*")
    passwd.grid(row=2, column=1)

    submit = Button(window, text="Submit", command= lambda:openc(client, email.get(), passwd.get()))
    submit.grid(columnspan=2)
    
    window.mainloop()

def logfb():
    login("Facebook")

def loggm():
    login("Gmail")

def openc(client, email, passwd):
    driver = webdriver.Firefox()
    driver.get("http://{}.com".format(client))
    if client == "Facebook":
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("pass").send_keys(passwd)
        driver.find_element_by_id("loginbutton").click()
    else:
        driver.find_element_by_id("identifierId").send_keys(email)
        driver.find_element_by_class_name("CwaK9").click()
        sleep(1)
        #Problem in finding password bar in gmail    
        typewrite(passwd)
        typewrite(['enter'])

def youtube():
    driver = webdriver.Firefox()
    driver.get("https://www.youtube.com/watch?v=kJjfle7CEwI&t=8s")
    sleep(5)
    typewrite(['space'])

root = Tk()
root.title("Automation!")

fb = Button(root, text="Open Facebook", command=logfb)
fb.grid(row=0, column=0)

gm = Button(root, text="Check Gmail", command=loggm)
gm.grid(row=0, column=1)

yg = Button(root, text="Morning Yoga", command=youtube)
yg.grid(row=0, column=2)

root.mainloop()
