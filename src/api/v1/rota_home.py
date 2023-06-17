from fastapi import APIRouter, Request, Response
from fastapi import Request

router = APIRouter()

@router.get("/")
async def home(request: Request):
	return Response(content="Olá Mundo")