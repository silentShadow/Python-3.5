#!/Users/Jonman/anaconda/bin/python3
import asyncio as sync


class EchoServer( sync.Protocol ):
    def connection_made( self, transport ):
        peer = transport.get_extra_info( 'peername' )
        print( "[+] Connection from {}".format( peer))
        self.transport = transport


    def data_received( self, data ):
        msg = data.decode()
        print( "Data received: {!r}".format( msg))
        
        print( "Send: {!r}".format( msg))
        self.transport.write( data)
        
        

loop = sync.get_event_loop()
coro = loop.create_server( EchoServer, '127.0.0.1', 4545)
srvr = loop.run_until_complete( coro)

# Keep serving requests until Ctrl+C is pressed
print( "Serving on {}".format( srvr.sockets[0].getsockname() ) )
try:
    loop.run_forever()
except:
    pass
    
# Close server
srvr.close()
loop.run_until_complete( srvr.wait_closed())
loop.close()