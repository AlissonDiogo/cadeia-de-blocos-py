from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from api.transactions import Transaction

from blockchain import Blockchain
from cache import CacheManager

router: APIRouter = APIRouter(
    prefix='/mine',
    tags=['mine'],
)

class Block(BaseModel):
    index: int
    timestamp: int
    transactions: List[Transaction]
    merkleRoot: str
    nonce: int
    previousHash: str

@router.post(
    '',
    response_model=Block,
    status_code=201,
)
def mine_block():
    blockchain: Blockchain = CacheManager.retrieve_blockchain()

    newBlock: Block = blockchain.createBlock()
    blockchain.mineProofOfWork(blockchain.prevBlock)
    CacheManager.update_blockchain(blockchain)

    return newBlock