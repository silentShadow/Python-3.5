#!/Users/Jonman/anaconda/bin/python3
import asyncio as snc


class ListeningConnections( snc.Protocol ):
    def connection_made( self, transport):
        peer = transport.get_extra_info( 'peername')
        print( "[+] Connection from {}".format( peer))
        self.transport = transport

    def data_recevied( self, data):
        command = input( "Shell> ")
        print( "Data received: {!r}".format( data.decode()))
        
        self.transport.write( command)
        



loop = snc.get_event_loop()                                             # Get the event loop for the current context
                                                                        #+ returns an event loop object implementing the BaseEventLoop interface
coro = loop.create_server( ListeningConnections, '127.0.0.1', 4545)     # Create the TCP server bound to host and port
srvr = loop.run_until_complete( coro)

# Keep serving requests until Ctrl+C is pressed
print( "Serving on {}".format( srvr.sockets[0].getsockname() ) )
try:
    loop.run_forever()
except:
    pass