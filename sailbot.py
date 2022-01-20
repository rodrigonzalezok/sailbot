from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.keys import Keys
import time
import json
from os import system
from time import sleep
import random

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------- NAVEGADOR WEB DONDE ESTARÁ CORRIENDO LA PÁGINA DONDE TRABAJAREMOS ---------------------------------------------------------

# Creamos la instancia del navegador
def browser_init():
    # Creamos las sesiones
    global browser
    browser = webdriver.Chrome(executable_path=".\driver\chromedriver.exe")
    # Abrimos las páginas y maximizamos las ventanas
    browser.get('https://web.whatsapp.com/')
    browser.maximize_window()
    # Qr
    print("Por favor, escanea los códigos QR")
    # Esperamos a que se cargue la pagina
    WebDriverWait(browser, 30000).until(expected_conditions.visibility_of_element_located((By.ID, 'side')))
    print("Whatsapp iniciado")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------- CÓDIGO QUE RECONOCE LOS MENSAJES Y OFRECE RESPUESTAS ACORDE A LAS MISMAS ---------------------------------------------------------

# Mensajes a enviar
def send_message(msj):

    # Utilizamos el diccionario json para elegir respuestas
    with open('./diccionario.json', encoding = "utf-8") as diccionario_mensajes:
        diccionario = json.load(diccionario_mensajes)
        
    # Hacemos click en el mensaje nuevo
    nombre_contacto = browser.find_element(locate_with(By.TAG_NAME, 'div').above(msj))
    nombre_contacto.click()
    time.sleep(0.5)

    # Si aparece un mensaje de un destinatario nuevo, damos click en 'Ok'
    try:
        if browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[2]/div/div[1]/div[1]/div/div[2]/div[3]/div/div/div').text == "OK":
            browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[2]/div/div[1]/div[1]/div/div[2]/div[3]/div/div/div').click()
    except:
        pass
    
    # Creamos variables
    mensaje_recibido = browser.find_elements(By.CSS_SELECTOR, 'div._22Msk div div._1Gy50')[-1].text
    mensaje_enviado = ""
    escribir_mensaje = browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    if len(browser.find_elements(By.CSS_SELECTOR, 'div._22Msk div div._1Gy50')) >= 2:
        mensaje_enviado = browser.find_elements(By.CSS_SELECTOR, 'div._22Msk div div._1Gy50')[-2].text
    mensaje_enviado_imagen = browser.find_elements(By.CSS_SELECTOR, 'div._22Msk div div._1Gy50')[-1].text
    
    # Verificamos qué mensaje nos llegó

    # Mensaje ABRIR CUENTA
    if mensaje_recibido.title() in diccionario.get('Abrir cuenta'):
        time.sleep(1)
        # Enviamos un mensaje
        try:
            escribir_mensaje.send_keys(diccionario.get('Respuesta a Abrir cuenta') + Keys.ENTER + Keys.ENTER)            
        except:
            print("No se pudo enviar el mensaje")

    """
    # Mensaje RECIBE NOMBRE DE USUARIO Y PIDE EMAIL
    if mensaje_enviado == diccionario.get('Respuesta a Abrir cuenta'):
        time.sleep(1)
        # Almacenamos el nombre del contacto que nos envia
        nombre_cliente = mensaje_recibido.title()
        # Enviamos un mensaje
        try:
            escribir_mensaje.send_keys("Muchas gracias *" + nombre_cliente + diccionario.get('Respuesta a Nombre') + Keys.ENTER)
        except:
            print("No se pudo enviar el mensaje")

    # Mensaje RECIBE EMAIL DE USUARIO Y PREGUNTA SI LA CUENTA ES PARA TITULAR O CON COTITULAR
    if mensaje_enviado == "Para comenzar te voy a pedir que me envies el email con el que querés abrir tu cuenta en Sailing Inversiones, dentro de poco vas a recibir la confirmación de la apertura en ese correo.":
        time.sleep(1)
        # Enviamos un mensaje
        try:
            escribir_mensaje.send_keys(diccionario.get('Respuesta a Email') + Keys.ENTER)
        except:
            print("No se pudo enviar el mensaje")

    # Mensaje ELIJE TITULAR Y RESPONDE PIDIENDO FOTO FRENTE DNI
    if mensaje_enviado == "Responde con la letra correspondiente a la opción que desees" and mensaje_recibido.title() in diccionario.get('Titular'):
        time.sleep(1)
        # Enviamos un mensaje
        try:
            escribir_mensaje.send_keys(diccionario.get('Respuesta a Titular') + Keys.ENTER)
        except:
            print("No se pudo enviar el mensaje") 

    # Mensaje RECIBE FOTO FRENTE DNI Y RESPONDE PIDIENDO FOTO DORSO DNI
    try:
        if browser.find_element(By.CSS_SELECTOR, 'div div._1bJJV div._3IfUe img').get_attribute('class') == 'jciay5ix tvf2evcx oq44ahr5 lb5m6g5c' and mensaje_enviado_imagen == "Por favor, verifica que se vean las 4 esquinas del DNI y que la imagen se vea lo más nítida posible.":
            time.sleep(1)
            # Enviamos un mensaje
            try:
                escribir_mensaje.send_keys(diccionario.get('Respuesta a Frente DNI') + Keys.ENTER)
            except:
                print("No se pudo enviar el mensaje") 
    except:
        pass

    # Mensaje RECIBE FOTO DORSO DNI Y RESPONDE PIDIENDO SELFIE CON DNI
    try:
        if browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/div[3]/div[17]/div/div[1]/div/div/div[1]/div[1]/div[2]/img').get_attribute('class') == "jciay5ix tvf2evcx oq44ahr5 lb5m6g5c" and mensaje_enviado_imagen == "¡Excelente! Ahora te voy a pedir que me mandes una foto del DORSO de tu DNI. Por favor, verifica que se vean las 4 esquinas del DNI y que la foto sea lo más nítida posible.":
            time.sleep(1)
            # Enviamos un mensaje
            try:
                escribir_mensaje.send_keys(diccionario.get('Respuesta a Dorso DNI') + Keys.ENTER)
            except:
                print("No se pudo enviar el mensaje")
    except:
        pass

    # Mensaje RECIBE SELFIE CON DNI Y RESPONDE PIDIENDO SELFIE CON GESTO
    try:
        if browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/div[3]/div[17]/div/div[1]/div/div/div[1]/div[1]/div[2]/img').get_attribute('class') == "jciay5ix tvf2evcx oq44ahr5 lb5m6g5c" and mensaje_enviado_imagen == "¡Sonríe!":
            time.sleep(1)
            # Enviamos un mensaje
            try:
                escribir_mensaje.send_keys(random.choice(diccionario.get('Respuesta a Selfie DNI')) + Keys.ENTER)
            except:
                print("No se pudo enviar el mensaje")
    except:
        pass

    # Mensaje RECIBE SELFIE CON GESTO Y RESPONDE PIDIENDO ESTADO CIVIL
    try:
        if browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/div[3]/div[17]/div/div[1]/div/div/div[1]/div[1]/div[2]/img').get_attribute('class') == "jciay5ix tvf2evcx oq44ahr5 lb5m6g5c" and mensaje_enviado_imagen == "¡WHISHY!":
            time.sleep(1)
            # Enviamos un mensaje
            try:
                escribir_mensaje.send_keys(diccionario.get('Respuesta a Selfie Aleatoria') + Keys.ENTER)
            except:
                print("No se pudo enviar el mensaje")
    except:
        pass

    # Mensaje RECIBE ESTADO CIVIL Y RESPONDE PIDIENDO RELACIÓN DE DEPENDENCIA
    if mensaje_enviado == "d. Viudo/a" and mensaje_recibido.title() in diccionario.get('a', 'b', 'c', 'd'):
        time.sleep(1)
        # Enviamos un mensaje
        try:
            escribir_mensaje.send_keys(diccionario.get('Respuesta a Estado Civil') + Keys.ENTER)
        except:
            print("No se pudo enviar el mensaje")

    # Mensaje RECIBE RELACIÓN DE DEPENDENCIA Y RESPONDE PIDIENDO ALCANCE EN ESTADOS OBLIGADOS
    if mensaje_enviado == "e. Estudiante" and mensaje_recibido.title() in diccionario.get('a', 'b', 'c', 'd', 'e'):
        time.sleep(1)
        # Enviamos un mensaje
        try:
            escribir_mensaje.send_keys(diccionario.get('Respuesta a Relacion de Dependencia') + Keys.ENTER)
        except:
            print("No se pudo enviar el mensaje")

    # Mensaje FINALIZACIÓN
    if mensaje_enviado == "g. Ninguno" and mensaje_recibido.title() in diccionario.get('a', 'b', 'c', 'd', 'e', 'f', 'g'):
        time.sleep(1)
        # Enviamos un mensaje
        try:
            escribir_mensaje.send_keys(diccionario.get('Respuesta a Relacion de Dependencia') + Keys.ENTER)
        except:
            print("No se pudo enviar el mensaje")
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------- CÓDIGO QUE VERIFICA QUE HAYA O NO NUEVOS MENSAJES Y EJECUTA LA FUNCIÓN SEND_MESSAGE() ---------------------------------------------------------

# Verificamos que haya un mensaje nuevo
def check_new_message(): 
    while True:
        system("cls")
        # Almacenamos los mensajes nuevos
        caja_mensajes = browser.find_elements(By.CSS_SELECTOR, 'div._1pJ9J span._23LrM')
        contador = 0
        # Si hay mensajes nuevos
        if len(caja_mensajes) > 0:
            # Recorremos todas las cajas de mensajes
            for mensaje in caja_mensajes:
                send_message(mensaje)
                contador += 1
                time.sleep(1)
                print("Quedan",contador,"mensajes nuevos")
        else:
            print("No hay mensajes nuevos")
        time.sleep(3)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------ INICIA EL SCRIPT -------------------------------------------------------------------------------------------

browser_init()
check_new_message()
time.sleep(100000)
