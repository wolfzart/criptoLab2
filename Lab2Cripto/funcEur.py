from apiCorreos import generateEmail, readMails, readMail
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

def registrarme(driver,mail,password,conta):
  #registrarme
  driver.get('https://www.boko.es/registro/?from=/')
  sleep(10)

  #saca anuncio y coockies
  if (conta == 0):
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/a").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/span").click()
  driver.save_screenshot('hito3-registro/fotopagina.png')
  sleep(10)

  #Comienzo de registro
  #ingresar email o usuario
  driver.find_element_by_xpath("/html/body/main/section/form/article/div[1]/input").send_keys(mail)
  driver.save_screenshot('hito3-registro/emailRegistro.png')    
  

  #Contraseña
  driver.find_element_by_xpath("/html/body/main/section/form/article/div[2]/input").send_keys(password)
  driver.save_screenshot('hito3-registro/passRegistro.png')

  #ticket termino y condiciones
  #https://stackoverflow.com/questions/55479227/select-checkbox-with-selenium-error-element-could-not-be-scrolled-into-view

  checkbox = driver.find_element_by_xpath("/html/body/main/section/form/article/div[4]/div/label")
  action = ActionChains(driver)
  action.move_to_element_with_offset(checkbox, 1, 1).click().perform()
  sleep(2)
  driver.save_screenshot('hito3-registro/teryconRegistro.png')

  #Click para registrarce
  driver.find_element_by_xpath("/html/body/main/section/form/article/button").click()
  sleep(5)
  driver.save_screenshot('hito3-registro/clickRegistro.png')

def inicioSesion(driver,mail,password,conta):
  #inicio de sesion
  #Entrar pagina española
  driver.get('https://www.boko.es/login/')
  driver.save_screenshot('hito3-inicioSesion/fotopagina.png')
  sleep(5)
  
  #saca anuncio y coockies
  if conta==0:
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/a").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/span").click()

  #correo
  #/html/body/main/section/form/div/div[1]/input
  driver.find_element_by_xpath("/html/body/main/section/form/div/div[1]/input").send_keys(mail)
  sleep(5)
  driver.save_screenshot('hito3-inicioSesion/correopagina.png')

  #contraseña
  driver.find_element_by_xpath("/html/body/main/section/form/div/div[2]/input").send_keys(password)
  sleep(5)
  driver.save_screenshot('hito3-inicioSesion/contraseña.png')

  #click
  driver.find_element_by_xpath("/html/body/main/section/form/button").click()
  sleep(5)
  driver.save_screenshot('hito3-inicioSesion/click.png')

def restablecerPassInicioSesion(driver,passActual,newPass):
  driver.get('https://www.boko.es/mi-contrasena/')
  driver.save_screenshot('hito3-restPass/fotopagina.png')
  sleep(5)

  #contraseña Actual
  driver.find_element_by_xpath("/html/body/div[4]/div/main/section/form/div/div/div[1]/input").send_keys(passActual)
  sleep(3)
  driver.save_screenshot('hito3-restPass/passActual.png')

  #nueva contraseña
  driver.find_element_by_xpath("/html/body/div[4]/div/main/section/form/div/div/div[2]/input").send_keys(newPass)
  sleep(3)
  driver.save_screenshot('hito3-restPass/newPass.png')

  #click para el cambio
  driver.find_element_by_xpath("/html/body/div[4]/div/main/section/form/button").click()
  sleep(3)
  driver.save_screenshot('hito3-restPass/cambioContraseña.png')


def contraPass(email):
  Mails=readMails(email)
  print(Mails[1]['id'])
  cuerpoMail=readMail(email,Mails[1]['id'])

  mensaje=cuerpoMail['body']
  bs = BeautifulSoup(mensaje, 'html.parser')

  newcontraseña = bs.find("td",{'align':'center','align':'center', 'valign':'middle','style':'color: #ECECEB; font-family: Arial, \'Helvetica Neue\', Helvetica, sans-serif; font-size: 23px; font-weight: bold; line-height: 150%; vertical-align: middle; mso-table-lspace: 0pt; mso-table-rspace: 0pt; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;'})
  return newcontraseña

def olvideMiPass(driver,mail):
  driver.get('https://www.boko.es/recordar-contrasena/')
  sleep (5)
  driver.save_screenshot('hito3-olvidoPass/fotopagina.png')
  sleep(5)
  
  driver.find_element_by_xpath("/html/body/div[8]/div[1]/a").click()
  driver.find_element_by_xpath("/html/body/div[1]/div/span").click()
  
  #email
  sleep(5)
  driver.find_element_by_xpath("/html/body/div[4]/div/section[1]/form/div[1]/div[1]/input").send_keys(mail)
  sleep(5)
  driver.save_screenshot('hito3-olvidoPass/email.png')
  
  #click
  driver.find_element_by_xpath("/html/body/div[4]/div/section[1]/form/div[2]/button").click()
  sleep(5)
  driver.save_screenshot('hito3-olvidoPass/clik.png')
