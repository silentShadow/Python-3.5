#!/Users/Jonman/anaconda/bin/python3
import asyncio as snc

props = dir( snc)

print( "Printing each item in the asyncio library")
for i in props:
    print( i)
    

print( "Printing subitems from everything in the asyncio library")
for i in props:
    print( dir( i))
    
    
snc.sleep
snc.create_subprocess_exec( program, *args, 
                            stdout=PIPE, 
                            stderr=PIPE, 
                            limit=streams._DEFAULT_LIMIT,
                            **kwds )
                            
