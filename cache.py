import pickle

import redis

import settings

from blockchain import Blockchain

class CacheManager:
    blockchain_key: str = 'blockchain'
    client: redis.Redis = redis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        db=settings.redis_db,
    )
    
    @staticmethod
    def save_blockchain(blockchain: Blockchain) -> None:
        encoded_blockchain: bytes = pickle.dumps(blockchain)

        CacheManager.client.set(
            name=CacheManager.blockchain_key,
            value=encoded_blockchain,
        )

    @staticmethod
    def update_blockchain(blockchain: Blockchain) -> None:
        CacheManager.save_blockchain(blockchain)

    @staticmethod
    def retrieve_blockchain() -> Blockchain:
        encoded_blockchain: bytes = CacheManager.client.get(
            name=CacheManager.blockchain_key,
        )

        blockchain: Blockchain = pickle.loads(encoded_blockchain)

        return blockchain