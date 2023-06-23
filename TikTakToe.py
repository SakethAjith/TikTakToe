import random
from random import choice
import requests
import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Game:

    def __init__(self):
        self.lim=3
        self.board=[]
        self.playerO='O'
        self.playerX='X'

        for i in range(self.lim):
            k=[]
            for j in range(self.lim):
                k.append('')
            self.board.append(k)

    def reset(self):
        self.board = [[''*(self.lim)]*self.lim]

    def play(self,s,pi,pj):
        self.board[pi][pj] = s

    def win(self,s):
        if s == 'O'*self.lim:
            print('Winner O')
            return True
        if s == 'X'*self.lim:
            print('Winner X')
            return True
        return False

    def check(self):
        res = False
        b=self.board
        for i in range(self.lim):
            res = res or self.win(''.join(b[i]))

        s=''
        for i in range(self.lim):
            s=''
            for j in range(self.lim):
                s+=b[j][i]
            res = res or self.win(s)


        s=''
        for i in list(range(self.lim)):
            s+=b[i][i]
        res = res or self.win(s)

        s=''
        for i in list(range(self.lim)):
            s+=b[i][self.lim-1-i]
        res = res or self.win(s)

        return res

    def freespc(self):
        res=[]

        for i in range(self.lim):
            for j in range(self.lim):
                if self.board[i][j]=='':
                    res.append([i,j])
        return res

def AgentRandom(spcs):
    return random.choice(spcs)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        tk = Game()
        # url = "http://localhost:3000/board"
        cnt = 0
        o=True

        while cnt<= pow(tk.lim,3) and (not tk.check()):
            spcs = tk.freespc()
            if tk.check():
                break
            if len(spcs)==0:
                if not tk.check():
                    print('Draw!')
                print(*tk.board, sep='\n')
                print()
                break
            if o:
                po=AgentRandom(spcs)
                tk.play(tk.playerO,po[0],po[1])
                cnt+=1
            else:
                px = AgentRandom(spcs)
                tk.play(tk.playerX, px[0], px[1])
                cnt+=1

            if o:
                o=False
            else:
                o=True
            print(*tk.board,sep='\n')
            print()

        boardrequest = {'board':tk.board}
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(boardrequest),"utf-8"))
        self.wfile.close()


myServer = HTTPServer(('',30),MyServer)

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()

# tk = Game()
# url = "http://localhost:3000/board"
# cnt = 0
# o=True

# while cnt<= pow(tk.lim,3) and (not tk.check()):
#     spcs = tk.freespc()
#     if len(spcs)==0:
#         if not tk.check():
#             print('Draw!')
#         print(*tk.board, sep='\n')
#         print()
#         break
#     if o:
#         po=AgentRandom(spcs)
#         tk.play(tk.playerO,po[0],po[1])
#         cnt+=1
#     else:
#         px = AgentRandom(spcs)
#         tk.play(tk.playerX, px[0], px[1])
#         cnt+=1

#     if o:
#         o=False
#     else:
#         o=True
#     print(*tk.board,sep='\n')
#     print()

#     boardrequest = {'board':tk.board}
#     response = requests(url,json=boardrequest)



# # tk.play(tk.playerO,0,2)
# # tk.play(tk.playerO,1,2)
# # tk.play(tk.playerO,2,2)
# print(tk.freespc())
# print(tk.check())
# print(tk.board)

