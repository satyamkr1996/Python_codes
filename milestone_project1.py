from IPython.display import clear_output
clear_output()
m1=[]
m2=[]
m=[{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]

x=[' ',' ',' ',' ',' ',' ',' ',' ',' ']                                  
t=0                                    
r_list=list(range(1,10))
game_on=True

from termcolor import colored

def op(r):
    print('Going on tik-tok-toe game'      'position numbering')
    print('{} | {} | {}                   1 | 2 | 3'.format(r[0],r[1],r[2]))
    print('---------                   ---------')
    print('{} | {} | {}                   4 | 5 | 6'.format(r[3],r[4],r[5]))
    print('---------                   ---------')
    print('{} | {} | {}                   7 | 8 | 9'.format(r[6],r[7],r[8]))
            
def input_check(number):
    if number in r_list:
        r_list.pop(r_list.index(number))
        return True

def winner():
    if c.issubset(set(m1))==True:
        print (colored('B is winner', 'green'))
    elif c.issubset(set(m2))==True:
        print (colored('A is winner', 'green'))
    else:
        print (colored('none wins', 'green'))

while t<=9 and game_on==True:                       #game_on==True is used to stop working in loop if found wrong.
    for c in m:
        if c.issubset(set(m1))==True:
            game_on=False
            break
        elif c.issubset(set(m2))==True:
            game_on=False
            break
        else:
            pass
    
    t+=1
    
    if t%2==0:                       
        while game_on==True and t<=9:
            u=(input('opponent B-pls(x) input between 1 to 9: '))
            if (u).isdigit()==True:
                if input_check(int(u))==True:
                    x[int(u)-1]='x'
                    m1.append(int(u))
                    clear_output()
                    op(x)
                    break                        #break used to come out of forever loop.
            else:
                clear_output()
                op(x)
                print('wrong value. pls try again')

    else: 
        while game_on==True and t<=9:
            u=(input('opponent A-pls(0) input between 1 to 9: '))             
            if (u).isdigit()==True:
                if input_check(int(u))==True:
                    x[int(u)-1]='o'
                    m2.append(int(u))
                    clear_output()
                    op(x)
                    break
            else:
                clear_output()
                op(x)
                print('wrong value. pls try again')
                
winner()








