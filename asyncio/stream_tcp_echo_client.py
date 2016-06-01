#!/Users/Jonman/anaconda/bin/python3
import asyncio as snc


@snc.coroutine
def tcp_echo_client( msg, loop):
    reader, writer = yield from snc.open_connection( '127.0.0.1', 4545, loop=loop)
    
    print( "Send: {}".format( msg))
    writer.write( msg.encode())
    
    data = yield from reader.read( 100)
    print( "Received: {}".format( data.decode()))
    
    print( "Close the socket")
    writer.close()
    
    
msg = "Hello, world!"
loop = snc.get_event_loop()
loop.run_until_complete( tcp_echo_client( msg, loop))
loop.close()