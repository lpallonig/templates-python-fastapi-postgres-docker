from fastapi import APIRouter

from src.api.v1 import rota_home
from src.api.v1 import rota_exemplo


router = APIRouter()
router.include_router(rota_home.router,prefix="",tags=["general_pages"])
router.include_router(rota_exemplo.router,prefix="/exemplo",tags=["exemplo"])