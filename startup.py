def tables( start, default=10 ):
    table = []
    for i in range(1, (default + 1) ):
        table.append( start * i )
    return table
            

if __name__ == "__main__":
    
    print( tables(2, 16) )
    