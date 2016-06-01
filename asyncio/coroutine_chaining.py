#!/Users/Jonman/anaconda/bin/python3
import asyncio as snc


async def compute(x, y):
    print( "Compute {} + {}...".format( x, y))
    await snc.sleep( 10)
    return x + y
    
    
async def print_sum(x, y):
    result = await compute( x, y)
    print( "{} + {} = {}".format( x, y, result))
    
    
loop = snc.get_event_loop()                         # Get the event loop of the current context
loop.run_until_complete( print_sum( 2, 4))          # Blocking call that returns what the print_sum() coroutine is done
loop.close()
