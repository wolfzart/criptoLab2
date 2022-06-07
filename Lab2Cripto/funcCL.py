from apiCorreos import generateEmail, readMails, readMail
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

def registrarme2(driver,mail,password,conta):
  #registrarme
  driver.get('https://jasaltec.cl/mi-cuenta/')
  sleep(3)
  #debido a ciberday click en cerrar una cosa x que sale
  driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/button").click()
  sleep(3)
  driver.save_screenshot('hito3-CH-registro/paginaRegistro.png')

  #click registro
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div[2]/div/div[3]/a").click()
  sleep(3)
  driver.save_screenshot('hito3-CH-registro/clickRegistro.png')
  
  #ingresar email o usuario
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div[2]/div/div[2]/form/p[1]/input").send_keys(mail)
  sleep(3)
  driver.save_screenshot('hito3-CH-registro/emailRegistro.png')    

  #Contraseña
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div[2]/div/div[2]/form/p[2]/span/input").send_keys(password)
  sleep(3)
  driver.save_screenshot('hito3-CH-registro/passRegistro.png')
  
  
  #Contraseña
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div[2]/div/div[2]/form/p[3]/button").click()
  sleep(3)
  driver.save_screenshot('hito3-CH-registro/resgistrado.png')

def restablecerPassInicioSesion2(driver,passActual,newPass):
  driver.get('https://jasaltec.cl/mi-cuenta/edit-account/')
  driver.save_screenshot('hito3-CH-restPass/fotopagina.png')
  sleep(5)

  #nombre
  driver.find_element_by_xpath("//*[@id='account_first_name']").send_keys("pedro")
  sleep(3)
  driver.save_screenshot('hito3-CH-restPass/nombre.png')

  #apellido
  driver.find_element_by_xpath("//*[@id='account_last_name']").send_keys("altamrino")
  sleep(3)
  driver.save_screenshot('hito3-CH-restPass/apellido.png')

  #contraseña Actual
  driver.find_element_by_xpath("//*[@id='password_current']").send_keys(passActual)
  sleep(3)
  driver.save_screenshot('hito3-CH-restPass/passActual.png')

  #nueva contraseña
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div/div[2]/form/fieldset/p[2]/span/input").send_keys(newPass)
  sleep(3)
  driver.save_screenshot('hito3-CH-restPass/newPass.png')
  
  #nueva contraseña X2
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div/div[2]/form/fieldset/p[3]/span/input").send_keys(newPass)
  sleep(3)
  driver.save_screenshot('hito3-CH-restPass/newPass2.png')

  #click para el cambio
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div/div[2]/form/p[5]/button").click()
  sleep(3)
  driver.save_screenshot('hito3-CH-restPass/cambioContraseña.png')

def inicioSesion2(driver,mail,password,conta):
  #inicio de sesion
  #Entrar pagina española
  driver.get('https://jasaltec.cl/mi-cuenta/')
  driver.save_screenshot('hito3-inicioSesion/fotopagina.png')

  sleep(3)
  #debido a ciberday click en cerrar una cosa x que sale
  driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/button").click()
  sleep(3)
  driver.save_screenshot('hito3-CH-registro/paginaRegistro.png')

  #correo
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div[2]/div/div[1]/form/p[1]/input").send_keys(mail)
  sleep(5)
  driver.save_screenshot('hito3-CH-inicioSesion/correopagina.png')

  #contraseña
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div[2]/div/div[1]/form/p[2]/span/input").send_keys(password)
  sleep(5)
  driver.save_screenshot('hito3-CH-inicioSesion/contraseña.png')

  #click
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/div[2]/div/div[1]/form/p[3]/button").click()
  sleep(5)
  driver.save_screenshot('hito3-CH-inicioSesion/click.png')


def link(email):
  data=readMails(email)
  id=data[0]['id']
  data2=readMail(email,id)
  mensaje=data2['body']
  bs = BeautifulSoup(mensaje, 'html.parser')
  conta = 0
  for href in bs.find_all('a',href=True):
    if (conta==0):
      link = href.get('href')
    conta=conta+1
  return link
def olvideMiPass2(driver,mail,newPass):
  driver.get('https://jasaltec.cl/mi-cuenta/lost-password/')
  sleep (3)
  driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/button").click()
  sleep(3)

  driver.save_screenshot('hito3-CH-olvidoPass/pagina.png')

  driver.save_screenshot('hito3-CH-olvidoPass/fotopagina.png')
  #email
  driver.find_element_by_xpath("//*[@id='user_login']").send_keys(mail)
  sleep(5)
  driver.save_screenshot('hito3-CH-olvidoPass/email.png')
  #click
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/form/p[3]/button").click()
  sleep(10)
  driver.save_screenshot('hito3-CH-olvidoPass/clik.png')
  #link enviado 
  url = link(mail)
  
  driver.get(url)
  driver.save_screenshot('hito3-CH-olvidoPass/fotopagina2.png')
  sleep(10)
  #contraseña nueva
  driver.find_element_by_xpath("//*[@id='password_1']").send_keys(newPass)
  sleep(5)
  driver.save_screenshot('hito3-CH-olvidoPass/contraseña1.png')

  #contraseña nueva2
  driver.find_element_by_xpath("//*[@id='password_2']").send_keys(newPass)
  sleep(5)
  driver.save_screenshot('hito3-CH-olvidoPass/contraseña2.png')
  #click
  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/article/div/div/form/p[4]/button").click()
  sleep(5)
  driver.save_screenshot('hito3-CH-olvidoPass/click2.png')