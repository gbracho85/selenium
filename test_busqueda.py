from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Bogotá")

buscador.send_keys(Keys.RETURN)

# Esperar resultados
time.sleep(2)
# Validar que exista algún resultado
#resultados = driver.find_elements(By.CSS_SELECTOR,".result") 
resultados = driver.find_elements(By.XPATH, "//*[@id='r1-0']/div[3]/h2/a/span")
# Esperar un tiempo para cerrar
time.sleep(4)
assert len(resultados) > 0, "No se encontraronresultados."
print("✅ Prueba funcional completada con éxito")
driver.quit()