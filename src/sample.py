# sample.py
import sys
import os

def process_data(  data,options = {}  ):
    target = data["value"]
    
    if target == None:
        return []

    if options.get("verbose") == True:
        print( f"Processing..." ) 

    result_list = [ 'apple', "banana",'orange',"grape",
                   'peach',"melon" ]
    
    unused_var = 100
    
    x = 1
    x = 2

    return result_list