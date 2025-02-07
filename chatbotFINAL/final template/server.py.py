import asyncio
import websockets

# Store connected clients
connected_clients = set()

async def notify_users(message):
    """Send a notification to all connected clients."""
    if connected_clients:  # asyncio.wait doesn't accept an empty list
        await asyncio.wait([client.send(message) for client in connected_clients])

async def handle_client(websocket, path):
    """Handle an individual client connection."""
    # Register the new client
    connected_clients.add(websocket)
    await notify_users(f"A user has joined the chat. Total users: {len(connected_clients)}")
    try:
        async for message in websocket:
            # Broadcast the received message to all connected clients
            await asyncio.wait([client.send(message) for client in connected_clients])
    finally:
        # Unregister the client on disconnect
        connected_clients.remove(websocket)
        await notify_users(f"A user has left the chat. Total users: {len(connected_clients)}")

async def main():
    server = await websockets.serve(handle_client, "localhost", 8010)  # Update port here to 8010
    print("WebSocket server is running on ws://localhost:8010")
    await server.wait_closed()
    
if __name__ == "__main__":
    asyncio.run(main())
