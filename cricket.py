
#----------------------cricket score card game ---------------------

#----instruction for run --------
try:
    print('''
    0,1,2,3,4,6------   run
    wkt -----for wicket              
    nb  -----for no ball
    wd  -----for wide ball
    lb  -----for leg bye''')
    print('\n'*3)
    


    boll=input('enter the runs (leave a space between runs) :-  ')   # enter runs and give a space between two ball 
    run=boll.split()


    
    order=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th']
    players=[f'{x} player' for x in order]    #create a list of playing XI

    #intial score board
    total=0
    extra=0
    wkt=0
    over=0

    p1=players[0]
    p2=players[1]
    recode={}         #recode of players
    a,b,c=0,0,0
    pp=0
    li=[]


    for j in range(len(run)):
        i=run[j]
        
        if i in '012345678':   #add simple run and count ball
            ii=int(i)
            total+=ii
            over+=1
        else:
            if 'wkt' in i:
                wkt+=1              #count wicket
                ii=int(i[0])
                total+=ii
                over+=1
            
                    
                if c==0 :
                    # print(p1,'out',a)
                    li.append([p1,'out',a])
                    a=0
                    p1=players[wkt+1]
                elif c==1:
                    # print(p2,'out',b)
                    s=[p2,'out',b]
                    li.append(s)
                    b=0
                    p2=players[wkt+1]
                    
            elif 'lb' in i:
                ii=int(i[0])   #lb run   mean addin extra runs
                total+=ii
                extra+=ii
                ii=0
                over+=1
                
            elif 'nb' in i:
                ii=int(i[0])
                total+=ii
                extra+=1
                ii=ii-1
                
                
            elif 'wd' in i:
                ii=int(i[0])
                total+=ii
                extra+=ii
                ii=0
                
        if j==0:    #this for plarer rotation after over completed 
            a+=ii     # or wicket fallen 
            recode[p1]=a
            c=a
            
        else:
            if c%2==0:
                a=a+ii
                recode[p1]=a
                if ii%2==0 and over%6==0:
                    c=1
                elif ii%2==0 or over%6==0:
                    c=0
                else:
                    c=1    
                
            else:
                b=b+ii
                recode[p2]=b
                if ii%2==0 and over%6==0:
                    c=0
                elif ii%2==0 or over%6==0:
                    c=1
                else:
                    c=0
    
    
    li.append([p1,'not out',a])
    
    li.append([p2,'not out',b])
    print()
     #main score card ------------------------------------------------------
    print('------------------score card------------------\n\n')
    print(" "*10,"_"*30)
    for j in range(1,len(li)+1):
        for k in li:
            if j==int(k[0][0]):
                
                sd=f"{k[1]} "
                sd=sd.center(10)
                print(' '*10,f"{k[0]} |"+sd +f"| RUN : { k[2]} ")
    print(" "*10,"_"*30)
  
    print()
    print("total", total)   
    print("extra", extra)
   


        
    print('over:',over//6,' and','ball:',over%6) 
    print('wicket',wkt)
                    
except:    #error only come when we not enter run in proper formate 
    print('wrong input')


            
    
    
    




