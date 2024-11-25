import asyncio

import game.Instance

instance = game.Instance()
asyncio.run(instance.loop())

