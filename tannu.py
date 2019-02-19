import pickle,  random, os

class Record:
    '''
    A class to represent a Record.
    '''
    def __init__(self,   key,  nonKey):
        '''
        Objective : To initialize the object of class Record.
        Input         :
             self : (Implicit Parameter) An object of class record.
        Return    : None
        '''

        self.keyAttr = key
        self.nonKeyAttr = nonKey

    def __str__(self):
        return 'KEY : '+str(self.keyAttr)

def recordKey(record):
    '''
    Objective : To return the key of the given node.
    Input          :
         node : An object of class Record.
    RETURN     : Key of the given node.
    '''
    return record.keyAttr

def saveRecords():
    '''
    Objective : To save records in a file and create an index file.
    Input          : None
    Return   : None
    '''
    
    start,  end,  min1,  max1,  min2,  max2 = 1, 100000, 3000000, 5000000, 50, 250

    fout = open('records.bin','wb')

    allKeys = []

    for i in range(start, end):

        key = random.randint(min1, max1)

        while key in allKeys : key = random.randint(min1, max1)

        allKeys.append(key)

        nonKey = str(i)*random.randint(min2, max2)

        pickle.dump(Record(key, nonKey),  fout)

    fout.close()
    
    
    '''
    fout = open('records.bin','wb')
    pickle.dump(Record(12,'1'), fout)
    pickle.dump(Record(72,'1'), fout)
    pickle.dump(Record(54,'1'), fout)
    pickle.dump(Record(35,'1'), fout)
    pickle.dump(Record(36,'1'), fout)
    pickle.dump(Record(67,'1'), fout)
    pickle.dump(Record(84,'1'), fout)
    pickle.dump(Record(21,'1'), fout)
    pickle.dump(Record(70,'1'), fout)
    pickle.dump(Record(40,'1'), fout)
    pickle.dump(Record(30,'1'), fout)
    pickle.dump(Record(19,'1'), fout)
    pickle.dump(Record(40,'1'), fout)
    pickle.dump(Record(16,'1'), fout)
    pickle.dump(Record(28,'1'), fout)
    pickle.dump(Record(14,'1'), fout)
    pickle.dump(Record(30,'1'), fout)
    '''
    
def getFileEnd(file):

    endOfFile =  file.seek(0,  os.SEEK_END)

    file.seek(0)

    return endOfFile

def merge(list1,  list2):
    '''
    Objective : To merge the given two lists.
    Input        :
        list1 : A list of objects of Record class.
        list2 : A list of objects of Record class.
    Return    : Merged list.
    '''
    mergedList = [ ]

    while list1 and list2:

        mergedList.append(list1.pop(0) if (recordKey (list1[0]) <= recordKey(list2[0])) else list2.pop(0))

    mergedList.extend( list1+ list2 )

    return mergedList
                
def mergeSortFiles( ):
    '''
    Objective : To merge sort the records on the basis of key values.
    Input     : None
    Return    : None
    '''
    inputFile, f1, f2 = open('records.bin','rb'), open('f1.bin','wb'), open('f2.bin','wb')
     
    blockSize = 4

    endOfFile = getFileEnd(inputFile)

    while inputFile.tell() < endOfFile:

        list1, list2 = [[pickle.load(inputFile) for _ in range(blockSize) if  inputFile.tell() < endOfFile] for _ in range(2)]

        list1.sort(key = recordKey), list2.sort(key = recordKey)

        for x in list1: pickle.dump(x,f1)

        for y in list2: pickle.dump(y,f2)

    inputFile.close(), f1.close(), f2.close()

    inputFile = open('records.bin','rb')
    print('UNSORTED:')
    i = 0
    while True:
        i += 1
        try:
            print(str(i)+' '+str(pickle.load(inputFile)))
        except EOFError:
            break

    while True:
        f1, f2, f3, f4 = open('f1.bin','rb'), open('f2.bin','rb'), open('f3.bin','wb'), open('f4.bin','wb')
        
        '''
        print('f1')
        while True:
            try:
                print(pickle.load(f1))
            except EOFError:
                break
        print('f2')
        while True:
            try:
                print(pickle.load(f2))
            except EOFError:
                break
    '''
        
        endOfFilef1,   endOfFilef2 = getFileEnd(f1),   getFileEnd(f2)

        if f2.tell() == endOfFilef2 : break

        while f1.tell() < endOfFilef1 or f2.tell() < endOfFilef2: 

            list1, list3 = [[pickle.load(f1) for _ in range(blockSize) if  f1.tell() < endOfFilef1] for _ in range(2)]

            list2, list4 = [[pickle.load(f2) for _ in range(blockSize) if  f2.tell() < endOfFilef2] for _ in range(2)]

            for x in merge(list1,list2): pickle.dump(x,f3)

            for y in merge(list3,list4): pickle.dump(y,f4)

        f1.close(), f2.close(), f3.close(), f4.close()
        
        os.remove('f1.bin'),os.remove('f2.bin')

        os.rename('f3.bin', 'f1.bin'), os.rename('f4.bin','f2.bin')

        blockSize *= 2

    f1 = open('f1.bin','rb')
    print('\n\nSORTED:')
    i = 0
    while True:
        i += 1
        try:
            print(str(i)+' '+str(pickle.load(f1)))
        except EOFError:
            break
        
if __name__ == '__main__':
    '''
    list1 = [Record(1,'1'),Record(4,'1'),Record(6,'1'),Record(7,'1'),Record(10,'1')]
    list2 = [Record(4,'1'),Record(5,'1'),Record(8,'1')]
    result = merge(list1,list2)
    for x in result: print(x)
    '''
    saveRecords()
    mergeSortFiles()
