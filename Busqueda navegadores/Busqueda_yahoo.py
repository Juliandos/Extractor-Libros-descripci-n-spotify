from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar opciones para ignorar errores SSL
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')  # Ignorar errores SSL
chrome_options.add_argument('--ignore-ssl-errors')  # Ignorar errores SSL adicionales

# Configurar WebDriver con opciones
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Abrir Yahoo
    driver.get("https://www.yahoo.com/")
    time.sleep(2)

    # Hacer clic en el cuadro de búsqueda (Yahoo a veces tiene una estructura dinámica)
    search_box = driver.find_element(By.NAME, "p")  # Nombre del campo de búsqueda en Yahoo
    search_box.send_keys("¿Es Google hoy en día, después de la aparición de chatGPT, las nuevas páginas amarillas?")
    search_box.send_keys(Keys.RETURN)  # Realizar la búsqueda
    time.sleep(3)

finally:
    # Cerrar el navegador
    driver.quit()
