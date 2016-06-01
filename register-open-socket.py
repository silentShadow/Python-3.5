#!/Users/Jonman/anaconda/bin/python3
import asyncio
from socket import socketpair


rsock, wsock = socketpair()             # Create a pair of connected sockets
loop = asyncio.get_event_loop()         # Create the event loop


class MyProto(asyncio.Protocol):
    transport = None
    
    def connection_made( self, transport):
        peer = transport.get_extra_info( 'peername' )
        print( "[+] Connection from {}".format( peer))
        self.transport = transport
        
    def data_received( self, data):
        print( "Data received: {}".format( data.decode()))
        
    def connection_lost( self, exc):
        print( "[!] Lost connection")
        loop.stop()
        
        
cnt_coro = loop.create_connection( MyProto, sock=rsock)
transport, protocol = loop.run_until_complete( cnt_coro)

loop.call_soon( wsock.send, 'abc'.encode())

loop.run_forever()

rsock.close()
wsock.close()
loop.close()
