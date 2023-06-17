from fastapi import APIRouter
from psycopg2.extras import DictCursor

from src.database import database

router = APIRouter()


@router.get("/")
def show_exemplos():
    conn = database.connect()
    cur = conn.cursor(cursor_factory=DictCursor)
    cur.execute("SELECT * FROM teste")
    resultados = cur.fetchall()
    retorno = []
    for resultado in resultados:
        retorno.append({"id": resultado['id'],
                        "valor": resultado['valor']})
    cur.close()
    conn.close()
    return retorno 

@router.post("/")
def create_exemplo(id: int, valor: int):
    conn = database.connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO teste (id, valor) VALUES (%s, %s)", (id, valor))
    conn.commit()
    print("adicionado com sucesso")
    cur.close()
    conn.close()