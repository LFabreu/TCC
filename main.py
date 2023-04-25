import PySimpleGUI as psg
import requests
from PIL import Image
import cloudscraper
import io


def convert_img():
  url = imagens()
  
  jpg_data = (
      cloudscraper.create_scraper(
          browser={"browser": "firefox", "platform": "windows", "mobile": False}
        )
      .get(url)
      .content
  )
  
  pil_image = Image.open(io.BytesIO(jpg_data))
  png_bio = io.BytesIO()
  pil_image.save(png_bio, format="PNG")
  png_data = png_bio.getvalue()

  return png_data

def imagens():
  url = "https://dog.ceo/api/breeds/image/random"
  pegar = requests.get(url)
  get = pegar.json()
  imagem = get['message']
  
  return imagem

def nova_janela():
  psg.theme('Reddit')
  layout = [

  [psg.Image(data=convert_img(), size=(500, 500))],
  [psg.Button('Gerar Doguinho', key='GERAR')],
  ]

  return psg.Window('Gerador de doguinhos', layout)

janela = nova_janela()

while True:
  event, values = janela.read()
  if event == psg.WINDOW_CLOSED:
    break
  elif event == 'GERAR':
    janela.close()
    janela = nova_janela()
    

  