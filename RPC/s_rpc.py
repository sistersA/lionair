from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Buat server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    info = [] #asal,tujuan,transit,boarding
    penerbangan1 = ['bandung', 'tokyo', 'singapura', '23.30 - 23.55']
    info.append(penerbangan1)
    penerbangan2 = ['jakarta', 'inggris', 'turki', '20.00 - 20.55']
    info.append(penerbangan2)
    
    # Operasi hitung
    def informasi_transit(asal, tujuan):
        for i in range(0,len(info)):
            if(info[i][0]==asal and info[i][1]==tujuan):
                return info[i][2]
        
    server.register_function(informasi_transit, 'insit')

    def informasi_boarding(asal, tujuan):
        for i in range(0,len(info)):
            if(info[i][0]==asal and info[i][1]==tujuan):
                return info[i][3]
        
    server.register_function(informasi_boarding, 'inboard')
    


    # Run the server's main loop
    server.serve_forever()