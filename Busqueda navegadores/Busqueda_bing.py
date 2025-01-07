from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def buscar_en_bing():
    # Configurar el controlador del navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Navegar hacia Bing
        driver.get("https://www.bing.com")

        # Esperar un momento para que cargue la página
        time.sleep(2)

        # Localizar la barra de búsqueda
        barra_busqueda = driver.find_element(By.NAME, "q")

        # Palabras clave a buscar
        palabras_clave = (
            "¿Es Google hoy en día, despues de la aparición de chatGPT, las nuevas páginas amarillas?"
        )

        # Escribir las palabras clave y presionar Enter
        barra_busqueda.send_keys(palabras_clave)
        barra_busqueda.send_keys(Keys.RETURN)

        # Esperar unos segundos para que los resultados se carguen
        time.sleep(5)

        # Maximizar la ventana
        driver.maximize_window()

    finally:
        # Cerrar el navegador
        driver.quit()

if __name__ == "__main__":
    buscar_en_bing()
