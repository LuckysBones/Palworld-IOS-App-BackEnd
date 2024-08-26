import asyncio
import websockets

async def players():
    uri = "ws://localhost:8001/ws/players/"  # Replace with your WebSocket server URI
    async with websockets.connect(uri) as websocket:
            await websocket.send('')
            message = await websocket.recv()
            print(message)
            await websocket.close()


async def info():
    uri = "ws://localhost:8001/ws/info/"  # Replace with your WebSocket server URI
    async with websockets.connect(uri) as websocket:
            await websocket.send('')
            message = await websocket.recv()
            print(message)
            await websocket.close()


async def metric():
    uri = "ws://localhost:8001/ws/metric/"  # Replace with your WebSocket server URI
    async with websockets.connect(uri) as websocket:
            await websocket.send('')
            message = await websocket.recv()
            print(message)
            await websocket.close()


async def message():
    uri = "ws://localhost:8001/ws/message/"  # Replace with your WebSocket server URI
    async with websockets.connect(uri) as websocket:
            await websocket.send("message")
            await websocket.close()


async def save():
    uri = "ws://localhost:8001/ws/save/"  # Replace with your WebSocket server URI
    async with websockets.connect(uri) as websocket:
            await websocket.send("")
            await websocket.close()


async def shutdown():
    uri = "ws://localhost:8001/ws/shutdown/"  # Replace with your WebSocket server URI
    async with websockets.connect(uri) as websocket:
            await websocket.send("message")
            await websocket.close()


if __name__ == '__main__':
      asyncio.run(players())
      print("\n")
      asyncio.run(info())
      print("\n")
      asyncio.run(metric())
      print("\n")
      asyncio.run(message())
      print("\n")
      asyncio.run(save())
      # asyncio.run(shutdown())