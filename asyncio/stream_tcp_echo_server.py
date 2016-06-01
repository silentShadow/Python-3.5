#!/Users/Jonman/anaconda/bin/python3
import asyncio as snc


@snc.coroutine
def handle_echo( reader, writer):
    data = yield from reader.read( 100)
    msg = data.decode()
    peer = writer.get_extra_info( 'peername' )
    print( "Received {} from {}".format( msg, peer))
    
    print( "Send: {}".format( msg))
    writer.write( data)
    yield from writer.drain()
    
    print( "Close the client socket")
    writer.close()
    
    
loop = snc.get_event_loop()
coro = snc.start_server( handle_echo, '127.0.0.1', 4545, loop=loop)
srvr = loop.run_until_complete( coro)

print('Serving on {}'.format(srvr.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
srvr.close()
loop.run_until_complete(srvr.wait_closed())
loop.close()
