from fastapi import APIRouter

from app.modules.repositories.api import router as repos_router
from app.modules.scoring.api import router as scoring_router
from app.modules.search.api import router as search_router

api_router = APIRouter()

api_router.include_router(repos_router)
api_router.include_router(scoring_router)
api_router.include_router(search_router)
