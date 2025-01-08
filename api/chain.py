from fastapi import APIRouter

from blockchain import Blockchain
from cache import CacheManager

router: APIRouter = APIRouter(
    prefix='/chain',
    tags=['chain'],
)

@router.get('')
def retrieve_chain():
    blockchain: Blockchain = CacheManager.retrieve_blockchain()
    
    return blockchain.chain