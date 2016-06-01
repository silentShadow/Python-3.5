#!/Users/Jonman/anaconda/bin/python3
import asyncio as snc


def hello_world( loop ):
    print( 'hello, world!' )
    loop.stop()                         # Once the hello_world function is called stop the loop
    

loop = snc.get_event_loop()             # 
loop.call_soon( hello_world, loop )     # Schedule a call to the specified function passing the loop as an arg
loop.run_forever()                      # Run forever until stop() method is called
loop.close()                            # Shut it down