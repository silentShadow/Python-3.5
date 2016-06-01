#!/Users/Jonman/anaconda/bin/python3
import asyncio as snc
import datetime


async def display_date( loop):
    print( "\nThis program will display the date every second for 5 seconds")
    end_time = loop.time() + 5.0                        # The time to stop is 5 seconds from current time
    
    while True:                                         # Endless loop
        print( datetime.datetime.now())                 # Print the current datetime
        if (loop.time() + 1.0) >= end_time:             # If the current datetime + 1 becomes >= the set end_time:
            break                                       #+ break the loop
        await snc.sleep( 1)                             # Sleep for 1 second between each iteration
        
    print()
    
        
loop = snc.get_event_loop()                             # Get the event loop for the current context
loop.run_until_complete( display_date( loop))           # Blocking call that returns when the display_date() coroutine is done
loop.close()
