user: dict = {
    "usuario_id": None,
    "pessoa_id": None,
    "email": None,
    "tipo_usuario": None,
    "acusador_id": None
}

def set_user(data: dict) -> None:
    global user
    user.update(data)