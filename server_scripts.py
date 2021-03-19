import socket
import asyncio


logs = []
def log_msg(msg):
    logs.append(msg)


async def handle_client(reader, writer):
    while True:
        if len(logs) > 0:
            writer.write(logs[0])
            logs = logs[1:]


async def run_server():
    server = await asyncio.start_server(handle_client, 'localhost', 1234)
    async with server:
        await server.serve_forever()


asyncio.run(run_server())     
    
