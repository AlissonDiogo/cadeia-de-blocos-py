import time

from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from blockchain import Blockchain
from cache import CacheManager

router: APIRouter = APIRouter(
    prefix='/transactions',
    tags=['transactions'],
)

class TransactionRequest(BaseModel):
    sender: str
    recipient: str
    amount: float
    priv_wif_key: str

    @property
    def timestamp(self) -> int:
        timestamp: int = int(time.time())

        return timestamp
    
class Transaction(BaseModel):
    sender: str
    recipient: str
    amount: float
    timestamp: int
    signature: str

@router.post(
    '/create',
    response_model=Transaction,
)
def create_transaction(transaction_request: TransactionRequest):
    blockchain: Blockchain = CacheManager.retrieve_blockchain()

    transaction: Transaction = blockchain.createTransaction(
        sender=transaction_request.sender,
        recipient=transaction_request.recipient,
        amount=transaction_request.amount,
        timestamp=transaction_request.timestamp,
        privWifKey=transaction_request.priv_wif_key,
    )

    CacheManager.update_blockchain(blockchain)

    return transaction

@router.get(
    '/mempool',
    response_model=List[Transaction]
)
def retrieve_memory_pool():
    blockchain: Blockchain = CacheManager.retrieve_blockchain()

    memory_pool: List[Transaction] = blockchain.memPool

    return memory_pool