from fastapi import FastAPI
from routes.chat_route import chat_route

app = FastAPI()

app.include_router(chat_route)





































# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# #from fastapi.responses import HTMLResponse

# app = FastAPI()

# # Store active users
# active_users = []

# html = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Chat Room</title>
#     <style>
#         #chat {
#             border: 1px solid black;
#             height: 250px;
#             width: 300px;
#             overflow-y: scroll;
#             padding: 5px;
#         }
#     </style>
# </head>
# <body>

# <h3>Chat Room</h3>

# <div id="chat"></div><br>

# <input id="name" placeholder="Your name"><br><br>
# <input id="msg" placeholder="Type message">
# <button onclick="sendMessage()">Send</button>

# <script>
#     var socket = new WebSocket("ws://127.0.0.1:8000/ws");

#     socket.onmessage = function(event) {
#         var chat = document.getElementById("chat");
#         chat.innerHTML += "<p>" + event.data + "</p>";
#     };

#     function sendMessage() {
#         var name = document.getElementById("name").value;
#         var msg = document.getElementById("msg").value;

#         socket.send(name + ": " + msg);
#         document.getElementById("msg").value = "";
#     }
# </script>

# </body>
# </html>
# """

# @app.get("/")
# def home():
#     return HTMLResponse(html)

# @app.websocket("/ws")
# async def chat_room(websocket: WebSocket):
#     await websocket.accept()
#     active_users.append(websocket)
#     print("New user joined. Active users:", len(active_users))

#     try:
#         while True:
#             message = await websocket.receive_text()
#             print("Message received:", message)

#             # Send message to ALL active users
#             for user in active_users:
#                 await user.send_text(message)

#     except WebSocketDisconnect:
#         active_users.remove(websocket)
#         print("User left. Active users:", len(active_users))
