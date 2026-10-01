from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

FAKE_USER = {"username": "ana", "password": "miclave123"}

LOGIN_FORM = """
<!doctype html>
<html>
<body style="font-family: sans-serif; max-width: 320px; margin: 80px auto;">
  <h2>Ingresar</h2>
  <form method="post" action="login">
    <input name="username" placeholder="Usuario" /><br><br>
    <input name="password" type="password" placeholder="Contraseña" /><br><br>
    <button type="submit">Entrar</button>
  </form>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def login_form():
    return LOGIN_FORM


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == FAKE_USER["username"] and password == FAKE_USER["password"]:
        return {"status": "ok", "mensaje": f"Bienvenido, {username}"}
    return {"status": "error", "mensaje": "Credenciales inválidas"}
