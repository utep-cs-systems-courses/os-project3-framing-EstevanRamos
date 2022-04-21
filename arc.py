import os

def archiver(path):
    flags = os.O_RDONLY
    
    #gets fd of the file
    try:
        fd = os.open(path , flags)
        print('file has been opened')
    except:
        print('file could not be opened')
    
    #encodes name of the file to bytes
    filename = str.encode(os.path.basename(path))
    
    #gets size of the file
    size = os.path.getsize(fd)
    
    #gets bytearry of the content of the file
    barr = os.read(fd, size)

    #archives name of file and length of name
    barr = len(filename).to_bytes(4, byteorder = 'big') + filename + barr
    return barr


def dearchiver(barr):
    flags = os.O_WRONLY|os.O_CREAT
    
    #get the len of the name of the file
    name_len = int.from_bytes(barr[:4] , 'big')

    #remove the length of the name from the array
    barr = barr[4:]

    #get name of file to string
    name = barr[:name_len].decode()
    print(name)

    #open the recieved file
    recieved = os.open( 'test_recieved.txt' , flags)

    #write the contents of the file
    os.write( recieved , barr[name_len:])