from typing import List
from typing import Set

from fastapi import APIRouter

from blockchain import Blockchain
from cache import CacheManager

router: APIRouter = APIRouter(
    prefix='/nodes',
    tags=['nodes'],
)

@router.get(
    '',
    response_model=List[str],
    status_code=200,
)
def retrieve_nodes():
    blockchain: Blockchain = CacheManager.retrieve_blockchain()
    nodes: List[str] = list(blockchain.nodes)

    return nodes

@router.post(
    '/register',
    response_model=List[str],
    status_code=201,
)
def register_nodes(nodes_request: List[str]):
    incoming_nodes: Set[str] = set(nodes_request)

    blockchain: Blockchain = CacheManager.retrieve_blockchain()
    blockchain.registerNodes(incoming_nodes)
    CacheManager.update_blockchain(blockchain)

    new_nodes: List[str] = list(incoming_nodes)

    return new_nodes

@router.post(
    '/resolve',
    status_code=202,
)
def resolve_conflicts():
    blockchain: Blockchain = CacheManager.retrieve_blockchain()
    blockchain.resolveConflicts()
    CacheManager.update_blockchain(blockchain)