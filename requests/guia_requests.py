# # No llamar al archivo requests.py
import requests


# r = requests.get('https://api.github.com/events')
# print(r)              # >>> <Response [200]>
# print(dir(r))         # muestra todos los metodos que pueden usarse. 
# print(help(r))        # muestra descripciones de lo que hacen los metodos. 
# print(r.text)         # imprime toda la estructura del contenido en html 
# print(r.json())       # imprime la estructura en formato json
# print(r.status_code)  # devuelve el estado de la peticion. 200, 300, 404, 500
# print(r.headers)      # detalles de la pagina. 
# print(r.url)          # Imprime tal cual el url al que consulta


# Descargar una imagen: pueed ser cualquier imagen mientras tenga su urlç
r = requests.get("https://wallpapercave.com/wp/wp4097158.jpg")

with open("cosmos_27_03_21.png", "wb") as f:
    f.write(r.content)


# ----------Get-----------
payload = {"page": 2, "count": 25}
r = requests.get("https://httpbin.org/get", params = payload)
print(r.text)
print(r.url)                  # >>> https://httpbin.org/get?page=2&count=25


# ----------Post-----------
payload = {"username": "charles", "password": "testing"}
r = requests.post("https://httpbin.org/post", data = payload)
print(r.text)

r_json = r.json()
print(r_json["form"])       # >>> {'password': 'testing', 'username': 'charles'}


# ----------login-----------: enviamos con auth el user y password
r = requests.get("https://httpbin.org/basic-auth/antoine/testing", auth=("antoine", "testing"))
print(r.text)               # >>> {"authenticated": true, "user": "antoine"}
print(r)                    # >>> <Response [200]>


r = requests.get("https://httpbin.org/basic-auth/antoine/testing", auth=("inexistente", "testing"))
print(r.text)               # no devuelve nada 
print(r)                    # >>> <Response [401]>

