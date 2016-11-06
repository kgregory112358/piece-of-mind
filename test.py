from websocket_server import WebsocketServer, WebSocketHandler
import thread
import types

client_queue = []
client_connections = {}

def create_connection():
    client1 = client_queue.pop(0)
    client2 = client_queue.pop(0)
    client_connections[client1['id']] = client2
    client_connections[client2['id']] = client1

def message_received(client, server, message):
    partner = client_connections.get(client['id'], None)
    if partner is not None:
        server.send_message(partner, message)

def new_client(client, server):
    client_queue.append(client)
    if len(client_queue) >= 2:
        create_connection()


server = WebsocketServer(13254, host='127.0.0.1')
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()
