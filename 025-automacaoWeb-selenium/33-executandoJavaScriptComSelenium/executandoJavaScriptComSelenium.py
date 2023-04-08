"""

### Executar Comandos Javascript (Scroll da tela)

- Você consegue, por meio do Selenium, executar comandos javascript no seu navegador

- Isso é essencial para dar scroll na tela, por exemplo, caso seja necessário, como no youtube

"""
# comando que dá scroll na janela em javascript é o window.scroll(x,y) onde x e y é o local para onde você quer ir na tela, exemplo:

# window.scroll(0, 100) onde x seria posicao zero e y posicao 100 (geralmente a posicao x sempre sera zero pois os sites nao costumam ter scroll lateral)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os, time

options=webdriver.ChromeOptions()
# chrome://version
options.add_argument(r'user-data-dir=C:\Users\Jorge\AppData\Local\Google\Chrome\User Data\Profile Selenium')
navegador=webdriver.Chrome(options=options)


# quero pegar uma lista de pelo menos 50 vídeos de Python do Youtube

navegador.get("https://www.youtube.com/results?search_query=python")

i=0
while len(navegador.find_elements(By.ID,'thumbnail'))<1:
    time.sleep(3)
    i+=1
    if i>30:
        break


# vou dar scroll na tela antes de pegar a lista de videos para que possam ser pegos um numero maior de videos
for i in range(5):
    numeroDeScroll=i*2000
    navegador.execute_script(f'window.scroll(0,{numeroDeScroll})')
    time.sleep(3)


listaVideos=navegador.find_elements(By.ID,'thumbnail')

listaLinksVideos=[video.get_attribute('href') for video in listaVideos if video.get_attribute('href')!=None]

for link in listaLinksVideos:
    print(link)

print(len(listaLinksVideos))



time.sleep(7)