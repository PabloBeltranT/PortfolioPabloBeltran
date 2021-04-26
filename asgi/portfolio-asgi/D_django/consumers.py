from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep
import json
from D_django.static.real_time_viewer import information

class Consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        while True:
            await self.send(json.dumps({'message':information()}))
            await sleep(1)