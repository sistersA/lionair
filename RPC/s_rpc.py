from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Buat server
with SimpleXMLRPCServer(('192.168.43.109', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    info = [] #NoPenerbangan,asal,tujuan,transit,boarding
    penerbangan1 = ['1','bandung', 'tokyo', 'singapura', '23.30 - 23.55', 'update']
    info.append(penerbangan1)
    penerbangan2 = ['2','jakarta', 'inggris', 'turki', '20.00 - 20.55', 'update']
    info.append(penerbangan2)
    

    def list_informasi_penerbangan():
        return info
    server.register_function(list_informasi_penerbangan,'DaftarPenerbangan')  

    def insert_penerbangan(no,asal,tujuan,transit,boarding):
        penerbangan=[no,asal,tujuan,transit,boarding]
        info.append(penerbangan)
        return penerbangan
    server.register_function(insert_penerbangan,'insert')  

    def update_penerbangan(no,asal,tujuan,transit,boarding):
        for i in range(0,len(info)):
            if(info[i][0]==no):
                info[i][1]=asal
                info[i][2]=tujuan
                info[i][3]=transit
                info[i][4]=boarding
                info[i][5]=datetime.now()
                return(info)
    server.register_function(update_penerbangan,'updatePenerbangan')  


    def informasi_transit(no):
        for i in range(0,len(info)):
            if(info[i][0]==no):
                return info[i][3]
        
    server.register_function(informasi_transit, 'insit')

    def informasi_boarding(no):
        for i in range(0,len(info)):
            if(info[i][0]==no):
                return info[i][4]
        
    server.register_function(informasi_boarding, 'inboard')

    def informasi_tujuan(no):
        for i in range(0,len(info)):
            if(info[i][0]==no):
                return info[i][2]
        
    server.register_function(informasi_tujuan, 'tujuan')

    def informasi_asal(no):
        for i in range(0,len(info)):
            if(info[i][0]==no):
                return info[i][1]
        
    server.register_function(informasi_asal, 'asal')
    
    def informasi_waktuUpdate(no):
        for i in range(0,len(info)):
            if(info[i][0]==no):
                return info[i][5]
        
    server.register_function(informasi_waktuUpdate, 'wup')

    # Run the server's main loop
    server.serve_forever()
