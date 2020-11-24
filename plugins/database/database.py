import asyncio
import asyncpg
import json
import discord

from discord import User
from discord import Guild
from discord import Message


class Database(object):
    def __init__(self, bot, pool, loop=None, timeout: float = 60.0):
        self.bot = bot
        self.pool = pool
        self._loop = loop or asyncio
        self.timeout = timeout
        self._rate_limit = asyncio.Semaphore(value=self.pool._maxsize, loop=self._loop)

    @classmethod
    async def create_pool(cls, bot, uri=None, *, min_connections=None, max_connections=None,
        timeout=60.0, loop=None, **kwargs):
        pool = await asyncpg.create_pool(uri, min_size=min_connections, max_size=max_connections, **kwargs)
        self = cls(bot=bot, pool=pool, loop=loop, timeout=timeout)
        return self 

    async def fetchrow(self, query, *args):
        async with self._rate_limit:
            async with self.pool.acquire() as con:
                return await con.fetchrow(query, *args)
                
    async def fetch(self, query, *args):
        async with self._rate_limit:
            async with self.pool.acquire() as con:
                return await con.fetch(query, *args, timeout=self.timeout)

    """"Execute querys"""
    async def execute(self, query, *args):
        async with self._rate_limit:
            async with self.pool.acquire() as con:
                return await con.execute(query *args)
