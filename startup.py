def tables( start, default=10 ):

    for i in range(1, (default + 1) ):
        print( start * i)
            

if __name__ == "__main__":
    
    tables( 2, 20 )
    
    