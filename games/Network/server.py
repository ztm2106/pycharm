import pickle
import socket
from _thread import *
from player import Player
import pickle
from game import Game

#server must be running on this machine with IP
server = "10.143.246.224"
# port = 80 (HTTP Connection) but port = 5555 is typically open for use
port = 5555

#setting up a socket
#socket.AF_INET is a type of connection to IPV4 and socket.SOCK_STREAM is how the server string comes in
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind server and port to socket
try:
    s.bind((server, port))
except socket.error as e:
    str(e)
#opens up the port to start connecting
#leaving blank has umlimited connections
s.listen()
print("Waiting for connection, Server Started")

connected = set()
games = {}
idCount = 0

#def read_pos(str):
    #str = str.split(",")
    #return int(str[0]), int(str[1])

#def make_pos(tup):
    #return str(tup[0]) + "," + str(tup[1])

#pos = [(0,0),(100,100)]
#players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50, 50, (0,0,255))]


# threaded function #thread is another process running in the background
def threaded_client(conn, p, gameId):
    #conn.send(pickle.dumps(players[player]))
    #reply = ""
    #continue running while client is connected
    #while True:
    #    try:
            #add bits which is the amount of info we are trying to receive
    #       data = pickle.loads(conn.recv(2048))
    #       players[player] = data

    #       #we have in encode the info when sending info
            #reply = data.decode("utf-8")
    #       if not data:
    #           print("Disconnected")
    #            break
    #       else:
    #           if player == 1:
    #               reply = players[0]
    #           else:
    #               reply = players[1]
    #           print("Received: ", data)
    #           print("Sending: ", reply)

     #       conn.sendall(pickle.dumps(reply))
      #  except:
       #     break
    #print("Lost Connection")
    #conn.close()

#check how many players are connected
#currentPlayer = 0
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("lost Connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    #s.accept() is going to accept any incoming connections
    #store connection and address(IP)
    conn, addr = s.accept()
    print("Connected to:", addr)

    #keep track # of ppl connected to server
    idCount += 1
    p = 0
    # 10 ppl 5 games but 9 games need another game because need even # of players
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a New Game")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))
    #currentPlayer += 1