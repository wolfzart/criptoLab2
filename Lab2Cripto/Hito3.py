from funcEur import registrarme,inicioSesion,restablecerPassInicioSesion,olvideMiPass
from funcCL import registrarme2,inicioSesion2,restablecerPassInicioSesion2,olvideMiPass2
from apiCorreos import generateEmail, readMails, readMail

import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--window-size=1000x1000")
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
from selenium.webdriver.common.action_chains import ActionChains
#PAGINA EUROPEA

#crear correo
email=generateEmail()
#registrarce
registrarme(driver,email,"12345",0)
#cierrosesion
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
#iniciar sesion
inicioSesion(driver,email,"12345",0)
#restablerPassInicioSesion
restablecerPassInicioSesion(driver,"12345","123456")
#cerrar sesion
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
#olvide mi contraeña
olvideMiPass(driver,email)



#PAGINA CHILENA

correo=generateEmail()
print(correo)
contraseña="P123.sdrt)23"
newContraseña="P123.sdrt)24"
#registrarme
registrarme2(driver,correo,contraseña,0)

#resta
restablecerPassInicioSesion2(driver,contraseña,newContraseña)

#cierraSesion
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

#inicioSesion con nueva contraseña
inicioSesion2(driver,correo,newContraseña,0)

#cierra sesion
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

#olvide mi contraseña
#correo="doqzeh@wwjmp.com"
olvideMiPass2(driver,correo,contraseña)