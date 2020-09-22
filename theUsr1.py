#-------------------------------------------------------------------------------
# Name:        Bot
# Purpose:
#
# Author:      t3fox
#
# Created:     06/09/2020
# Copyright:   (c) t3fox 2020
# Licence:     GNU.V3
#-------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
import subprocess


driver = webdriver.PhantomJS()


def Usrlog():

    theemail = "username@mail.com"
    psswrd = "x=6XGnpCVJ"
    driver.get('https://m.facebook.com/')


    print("\n\n-----    Search  OK  -----\n")
    print("--- STATUS BLUE.USERS --\n\n")


    email = driver.find_element_by_xpath('//*[@id="m_login_email"]')
    email.send_keys(theemail)
    print("\t>>> Email    -   OK ")

    password = driver.find_element_by_name('pass')
    password.send_keys(psswrd)
    print("\t>>> Password -   OK")


    button = driver.find_element_by_xpath('//*[@id="u_0_4"]/button')
    button.click()
    print("\n\n-----LOGIN-----")

    time.sleep(3)
    skip = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/div/a')
    skip.click()

    print("\n\n-----ESTAS EN LA INTERFA<> PRINCIPAL-----")
    time.sleep(3)




#EXPERIMENTAL 1.0
def likethat():

    try:
        thelike = driver.find_element_by_css_selector('a[aria-label=Like]')
        #thelike = driver.find_element_by_class_name(' _6a-y _3l2t  _18vj')

    #thelike = driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div/form/div[2]/div/div[2]/div/span[1]/div/div/div/div/div/div/div[1]/span[1]')
        print(">>> ",thelike)
        thelike.click()
        print("\n\n-----    LIKED   OK  -----")

    except:
        print("No encontrado")

def lovethat():
    pass

def enjoythat():
    pass

def angrythat():
    pass

#END TO EXPERIMENTAL


def Repany():
    somepe = str(input(">>> User Mobile: "))
    driver.get(somepe)
    time.sleep(3)
    some_rep = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div/div[1]/div/div[3]/div/div[4]/a')
    some_rep.click()
    time.sleep(2)
    reportsome = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[2]/a[1]')
    reportsome.click()
    time.sleep(3)
    print("\n\t\t...:::TIPO DE PROBLEMA:::... ")
    print("""\n
   >>> Cuenta Falsa                                             --         1
   >>> Nombre Falso                                             --         2
   >>> Contenido Inapropiado                                    --         3
   >>> Acoso o Bullying                                         --         4

   """)
    selrep = int(input('>>> : '))
    subprocess.call("cls",shell=True)

    if selrep == 1:
        time.sleep(2)
        check = driver.find_element_by_xpath('//*[@id="tag_profile_fake_account"]')
        check.click()
        time.sleep(2)
        submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/form/div[4]/button')
        submit.click()
        time.sleep(4)
        donefkaccount = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button')
        donefkaccount.click()
        print("\n\t...:::REPORTANDO:::...")
        driver.close()


    elif selrep == 2:
        time.sleep(2)
        check = driver.find_element_by_xpath('//*[@id="tag_profile_fake_name"]')
        check.click()
        time.sleep(2)
        submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/form/div[4]/button')
        submit.click()
        time.sleep(4)
        donefkaccount = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button')
        donefkaccount.click()
        print("\n\t...:::REPORTANDO:::...")
        driver.close()

    elif selrep == 3:
        time.sleep(2)
        check = driver.find_element_by_xpath('//*[@id="tag_profile_posting_inappropriate_things"]')
        check.click()
        time.sleep(2)
        submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/form/div[4]/button')
        submit.click()
        time.sleep(4)
        donefkaccount = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button')
        donefkaccount.click()
        print("\n\t...:::REPORTANDO:::...")
        driver.close()

    elif selrep == 4:
        time.sleep(2)
        check = driver.find_element_by_xpath('//*[@id="tag_profile_posting_inappropriate_things"]')
        check.click()
        time.sleep(2)
        submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/form/div[4]/button')
        submit.click()
        time.sleep(4)
        donefkaccount = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button')
        donefkaccount.click()
        print("\n\t...:::REPORTANDO:::...")
        driver.close()






def RepPublish():
   time.sleep(2)
   theurl = str(input('\n\n--- URL PUBLICACION ---'))
   driver.get(theurl)
   print("\n----- ESTAS EN LA PUBLICACION -----")

   report = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[1]/header/div[2]/div/div/div[3]/div/a')
   report.click()
   time.sleep(2)
   startrep = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[4]/div/div/div[2]/a[2]')
   startrep.click()

   print("\n\t\t...:::TIPO DE PROBLEMA:::... ")
   print("""\n
   >>> Acoso                -       1
   >>> Noticia Falsa        -       2
   >>> Incitacion al odio   -       3

   """)
   selrep = int(input('>>> : '))
   subprocess.call("cls",shell=True)

   if selrep == 1:
        time.sleep(2)
        check = driver.find_element_by_xpath('//*[@id="tag_harassment"]')
        check.click()
        time.sleep(2)
        tpcheck = driver.find_element_by_xpath('//*[@id="tag_harassment_me"]')
        tpcheck.click()
        time.sleep(2)
        submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/form/div[4]/button')
        submit.click()
        time.sleep(4)
        doneharass = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button')
        doneharass.click()
        print("\n\n... Reportando Acoso ...")

   elif selrep == 2:
        time.sleep(2)
        check = driver.find_element_by_xpath('//*[@id="tag_false_news"]')
        check.click()
        time.sleep(2)
        submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/form/div[4]/button')
        submit.click()
        time.sleep(4)
        donefknew = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button')
        donefknew.click()
        print("\n\n... Reportando Fake New ...")

   elif selrep == 3:
        time.sleep(2)
        check = driver.find_element_by_xpath('//*[@id="tag_hate_speech"]')
        check.click()
        time.sleep(2)
        tpcheck = driver.find_element_by_xpath('//*[@id="tag_hate_speech_social_caste"]')
        tpcheck.click()
        time.sleep(2)
        submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/form/div[4]/button')
        submit.click()
        time.sleep(4)
        doneharass = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button')
        doneharass.click()
        print("\n\n... Reportando Incitacion ...")


def commit():
    comentando = driver.find_element_by_xpath('//*[@id="feedback_inline_192772562283843"]/div[2]/div[2]/a')
    comentando.click()
    print("\n\n--Entrando a comentarios---")

    time.sleep(3)

    textarea = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div/div/div[6]/div[2]/form/div[1]/div[2]/div[1]/div/textarea')

    #commit = str(input("Comentario: "))
    #textarea.send_keys(commit)


Usrlog()
time.sleep(3)
#commit()

#RepPublish()
Repany()

