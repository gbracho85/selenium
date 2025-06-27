from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("Café")

buscador.send_keys(Keys.RETURN)

# Esperar resultados
time.sleep(3)
# Validar que exista algún resultado
#resultados = driver.find_elements(By.CSS_SELECTOR,".result") 
resultados = driver.find_elements(By.XPATH, "//*[@id='rso']/div[3]/div/div/div/div[1]/div/div/span/a/h3")
assert len(resultados) > 0, "No se encontraronresultados."
print("✅ Prueba funcional completada con éxito")
driver.quit()