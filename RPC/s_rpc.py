from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Buat server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    info = [] #NoPenerbangan,asal,tujuan,transit,boarding
    penerbangan1 = ['1','bandung', 'tokyo', 'singapura', '23.30 - 23.55']
    info.append(penerbangan1)
    penerbangan2 = ['2','jakarta', 'inggris', 'turki', '20.00 - 20.55']
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
                return(info)
    server.register_function(insert_penerbangan,'updatePenerbangan')  


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
        
    server.register_function(informasi_transit, 'tujuan')

    def informasi_asal(no):
        for i in range(0,len(info)):
            if(info[i][0]==no):
                return info[i][1]
        
    server.register_function(informasi_boarding, 'asal')
    


    # Run the server's main loop
    server.serve_forever()