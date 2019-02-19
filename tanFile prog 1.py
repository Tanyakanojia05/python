'''
To create a file of N records and create f1 and f2 2 files in blocks of BS
'''
import pickle, os
import random

N = 1000
BS = 4

class Record :
    '''
    DESCRIPTON : To create an object of class 'obj' with key and other value pairs
    ATTRIBUTES : key, other
    '''

    def __init__(self, key, other):
        '''
        OBJECTIVE : To initialize an object of class 'Obj'
        INPUT PARAMETERS :
                self : Implicit
                key : key value of the object 
                other : value corresponding to that key
        OUTPUT :
                None
        '''

        #Appoach: Assign key and other
        
        self.key = key 
        self.other = other

    def get_key(self):

        '''
        OBJECTIVE: To get key value of the object
        INPUT PARAMETERS:
                 self: Implicit
        OUTPUT :
                 Return key
        '''

        return self.key


    def __str__(self):
        '''
        OBJECTIVE: To return a string of the values of the object 
        INPUT PARAMETERS :
                self : Implicit
        OUTPUT : 
                a string of object
        '''

        return "Key: "+str(self.key) #+ "\nOther: " + str(self.other)

'''
def write():

    
    OBJECTIVE :  To write objects in file.txt
                                key=random(1000000,2000000)
                                value=key*100
    INPUT PARAMETERS :
            None
    OUTPUT :
            None
    

    #Approach: Dump Record object in file.txt 

    f = open("file.txt", "wb")
    keyList = []
    i=0;
    while i<N:
        key = random.randint(1000000, 2000000)

        #if dupicate ignore

        if key not in keyList:
            keyList.append(key)
            val = str(key) * 100
            ob = Obj(key, val)
            pickle.dump(ob, f)
            i=i+1
            
    f.close()
'''


def write(fname):

    '''
    OBJECTIVE :  To write objects in file.txt
                                key=random(1000000,2000000)
                                value=key*100
    INPUT PARAMETERS :
            None
    OUTPUT :
            None
    '''

    #Approach: Dump Record object in file.txt 

    f = open(fname, "wb")

    keyList = []
    L=random.sample(range(10000000,20000000),N)
    #print('type(L): ', type(L))
    for i in range(0,N):
        key=L[i]
        val = str(key) * 100
        ob = Record(key, val)
        pickle.dump(ob, f)
        
        if i%100000==0:
            print(i)    
    f.close()

def createF1F2(file1,f1,f2):
    '''
    OBJECTIVE :  To sort records of file.txt block by block and store them in f1.txt and f2.txt
    INPUT PARAMETERS :
            Global variable BS(blocksize) is used
    OUTPUT :
            None
    '''
    #APPROACH: To sort the records in file.txt and store them in f1.txt and f2.txt sorted by blocksize
    #                        :Call merge and combine blocks of f1 and f2 by calling function merge()

    global BS

    f = open(file1, "rb")
    f1 = open(f1, "wb")
    f2 = open(f2, "wb")
    dump_to=True
    Loop=True
    
    #loop false when records finished in f1 or f2
    #dump_to=True then f1 , False then f2

    while Loop:
        f1List = []
        try:
            for i in range (0, BS):
                ob = pickle.load(f)
                f1List.append(ob)
        except EOFError :
            Loop=False
            
        f1List.sort(key = lambda Obj : Obj.get_key())
            
        if dump_to:
            fdump=f1
        else:
            fdump=f2
                
        for el in f1List:
            pickle.dump(el, fdump)
                
        dump_to = not dump_to
    f.close()
    f1.close()
    f2.close()


def display(file1):
    '''
    OBJECTIVE :  To display records in file1
    INPUT PARAMETERS :
            None
    OUTPUT :
            None
    '''
    f = open(file1, "rb")
    for i in range(1,N+1):
        ob = pickle.load(f)
        print(str(i) + " file")
        print(ob)        
    f.close()
    
def displayFx(fx,L,R=-1):
    '''
    OBJECTIVE: To display records in file f1.txt or f2.txt from record number L to R or a specific record number(R=0)
    INPUT PARAMETERS:
                fx = 0 print from f1.txt, 1 print from f2.txt
                L = start printing from
                R = print till
    '''
    '''
    Approach: To print from f1 if fx=0 and f2 if fx=1, Move to (L-1)*size record
        where
        size: size of the node/record
    '''
    f=open(fx,"rb")
    pickle.load(f)
    size=f.tell()
    f.seek(0)
    f.seek((L-1)*size)
    if R==-1:
        try:
            print(pickle.load(f))
        except:
            pass
    else:
        while R>=L:
            
            try:
                print(str(L)+" ::",end="")
                L+=1
                print(pickle.load(f))
            except:
                break
            

    
def displayF1F2(f1,f2) :
    '''
    OBJECTIVE :  To display records of f1 and f2 files
    INPUT PARAMETERS :
            None
    OUTPUT :
            None
    '''
    f1 = open(f1, "rb")
    f2 = open(f2, "rb")
    i=1
    while True:
        try:
            ob = pickle.load(f1)
            print(str(i) + " f1")
            print(ob)
            i+=1
        except:
            break
    i=1
    while True:
        try:
            ob = pickle.load(f2)
            print(str(i) + " f2")
            print(ob)
            i+=1
        except:
            break

    f1.close()
    f2.close()
    
def main() :
    file1=input("Enter file name to create random records")
    write(file1)
    f1=input("Enter file name F1 to sort records")
    f2=input("Enter file name F2 to sort records")
    createF1F2(file1,f1,f2)
    while True:
        print("\nMENU")
        print("1. Print main random records file")
        print("2. Print a number of records from ",f1)
        print("3. Print one record from ",f1)
        print("4. Print a number of records from ",f2)
        print("5. Print one record from ",f2)
        print("\n")
        n=input("Enter your choice")
        if n!='':
            n=int(n)
        if n==1:
            display(file1)
        elif n==2:
            L=int(input("Print record from"))
            R=int(input("Print record till"))
            displayFx(f1,L,R)
        elif n==3:
            L=int(input("Print record number"))
            displayFx(f1,L)
        elif n==4:
            L=int(input("Print record from"))
            R=int(input("Print record till"))
            displayFx(f2,L,R)
        elif n==5:
            L=int(input("Print record number"))
            displayFx(f2,L)    
        else:
            print("Please enter a choice")
if __name__=='__main__':
    main()
