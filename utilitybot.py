"""MIT License

Copyright (c) 2020 utilitybot.co

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import sys
import discord
from discord.ext import commands
import asyncio
import asyncpg
import datetime
import aiohttp
import json
import logging


class Utilitybot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.launchtime = datetime.datetime.now(datetime.timezone.utc)
        self.db = asyncpg.pool.Pool = None
        self.started = False

        logging.basicConfig(filename='utilitybot.log', level=logging.INFO)
        self.logging = logging.getLogger('Utility')
        stdout = logging.StreamHandler(sys.stdout)
        stdout.setLevel(logging.INFO)
        self.logging.addHandler(stdout)
        gateway = logging.getLogger('discord.gateway')
        gateway.addHandler(stdout)
        
        
    async def load_commands(self):
        pass

    async def load_cogs(self):
        pass

    async def load_utils(self):
        pass

    async def load_events(self):
        pass

