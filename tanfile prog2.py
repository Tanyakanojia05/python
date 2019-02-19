import os
import Fileprogram1
from Fileprogram1 import *

'''
Run program Fileprogram1.py
'''


def merge(fname1,fname2):
    '''
    OBJECTIVE: To merge files f1 and f2 block by block and placing the sorted twice size block to files f3 and f4 respectively
            by increasing the blocksize to twice its length until file f2 is empty and all records are in f1 sorted
            Replacing the files f3 and f4 by f1 and f2 repeatedly
    INPUT PARAMETERS: global variable(BS): blocksize
                      get_key function imported
                      class Obj imported and used

    OUTPUT: sorted file f1 
    '''
    '''
    APPROACH: To sort BS records from f1 and BS from f2 and place in f3 and f4 till file f2 is empty

    VARIABLES:
            Loop: Loop is true initially, False if one of the files is left with records less than blocksize
            dump_to: True then dump in file f3 else file f4
            fx: f3 or f4
            Loadob1: if True load object from file f1
            Loadob2: if True load object from file f2
            LI: To keep track of loaded object from file f1 when while loop is finished
            LJ: To keep track of loaded object from file f2 when while loop is finished
            i: Number of records from file f1 dumped
            j: Number of records from file f2 dumped
    '''
    global BS

    while True:
        f1=open(fname1,"rb")
        f2=open(fname2,"rb")
        f3=open("f3","wb")
        f4=open("f4","wb")
        Loop=True
        dump_to=True
        
        while Loop:
            if dump_to:
                fx=f3
            else:
                fx=f4
            dump_to = not dump_to
            #Alternative f3 anf f4 file
            
            i,j=0,0
            Loadob1,LI=True,False
            Loadob2,LJ=True,False

            #Load till Blocksize number of records are read from any f1 or f2 file
            while i<BS and j<BS:
                if Loadob1==True:
                    try:
                        ob1=pickle.load(f1)
                        LI=True
                        Loadob1=False
                    except:
                        Loop=False
                        break
                if Loadob2==True:
                    try:
                        ob2=pickle.load(f2)
                        LJ=True
                        Loadob2=False
                    except:
                        Loop=False
                        break

                if ob1.get_key()<ob2.get_key():
                    pickle.dump(ob1,fx)
                    i=i+1
                    Loadob1=True
                    LI=False
                else:
                    pickle.dump(ob2,fx)
                    j=j+1
                    Loadob2=True
                    LJ=False
                    
            #dump the last loaded record either of f1 or f2
                    
            if LI:                        #if object from file f1 is loaded dump it
                pickle.dump(ob1,fx)
                i+=1
            elif LJ:                      #if object from file f2 is loaded dump it
                pickle.dump(ob2,fx)
                j+=1
            
            #Number of dumped objects from file f1 or f2 not equal to blocksize
            #dump the remaining
                
            while i<BS:
                try:
                    ob1=pickle.load(f1)
                    pickle.dump(ob1,fx)
                    i=i+1
                except:
                    Loop=False
                    break
            while j<BS:
                try:
                    ob2=pickle.load(f2)
                    pickle.dump(ob2,fx)
                    j=j+1
                except:
                    Loop=False
                    break

        
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        try:
            os.remove(fname1)
            os.remove(fname2)
            os.rename("f3",fname1)
            os.rename("f4",fname2)
        except:
            print("error")
        if os.path.getsize(fname2) == 0:
            break
        BS*=2

def displayFname(fname,L,R=-1):
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
    f=open(fname,"rb")
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
                print("EMPTY")
                break
            

def main():

    print("Enter file names to merge")
    fname1=input("File 1 name:")
    fname2=input("File 2 name:")
    merge(fname1,fname2)
    while True:
        print("Print a number of records from",fname1)
        print("\n")
        L=int(input("Enter lower limit\n"))
        R=int(input("Enter upper limit\n"))
        #Imported function from Fileprogram1.py
        #Fx=0 display file f1
        displayFname(fname1,L,R)

if __name__=='__main__':
    main()
