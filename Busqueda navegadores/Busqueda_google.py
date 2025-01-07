from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def realizar_busqueda():
    # Configurar el controlador de Selenium usando webdriver-manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Navegar a Google
        driver.get("https://www.google.com")

        # Esperar un momento para asegurarse de que la página cargue completamente
        time.sleep(1)

        # Aceptar cookies si aparece el cuadro de diálogo
        try:
            aceptar_cookies = driver.find_element(By.XPATH, "//button[contains(text(), 'Acepto') or contains(text(), 'Aceptar todo')]")
            aceptar_cookies.click()
            time.sleep(1)  # Esperar a que se cierre el cuadro
        except:
            pass  # Ignorar si no aparece el cuadro de cookies

        # Encontrar la barra de búsqueda
        barra_busqueda = driver.find_element(By.NAME, "q")

        # Escribir la frase clave
        frase_clave = "¿Es Google hoy en día, despues de la aparición de chatGPT, las nuevas páginas amarillas?"
        barra_busqueda.send_keys(frase_clave)

        # Enviar la búsqueda
        barra_busqueda.send_keys(Keys.RETURN)

        #ventana maximizada
        driver.maximize_window()

        # Esperar unos segundos para que se carguen los resultados
        time.sleep(5)

    finally:
        # Cerrar el navegador
        driver.quit()

if __name__ == "__main__":
    realizar_busqueda()
