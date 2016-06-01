#!/Users/Jonman/anaconda/bin/python3
import asyncio as snc

async def hello_world():
    print( "Hello, World!")
    
    
loop = snc.get_event_loop()                 # Get the event loop for the current context
loop.run_until_complete( hello_world())     # Blocking call that returns when the hello_world() coroutine is done
loop.close()