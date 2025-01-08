from fastapi import FastAPI

import settings

from api.chain import router as chain_router
from api.mine import router as mine_router
from api.nodes import router as nodes_router
from api.transactions import router as transactions_router

from blockchain import Blockchain
from cache import CacheManager

CacheManager.save_blockchain(Blockchain())

app = FastAPI(
    debug=settings.debug,
    title='Blockchain API',
)

app.include_router(chain_router)
app.include_router(mine_router)
app.include_router(nodes_router)
app.include_router(transactions_router)