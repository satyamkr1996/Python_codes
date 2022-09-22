#A self thought idea that came to my mind while taking the lift. Here, a user has to give his floor number and direction of desired movement in a 10-storied building. 
# Finally, two lists are created for up and down movement keeping in mind:
#     1. opposite sorting of list
#     2. Repeated key punching doesn't bring repeatation in the list
#     3. An infinite loop expecting infinite life of lift
#     4. Output gets cleared everytime when while loop starts for good output look
#     5. Invalid input gives invalid message and gives another chance to input


#It's a basic idea for lift working. There are many possibilities to improve the
#working of the code.

from IPython.display import clear_output

list_up=[]
list_down=[]


#floor info
while True:
  clear_output(wait=True)
  y=input('your floor between 1 to 10:')
  try:
    y=int(y)
    if y in [*range(1,11,1)]:
      
      #up and down info
      while True:
        x=input('U for up and D for down:')
        if x=='U':
          list_up.append(y)
          list_up = list(dict.fromkeys(list_up))
          list_up.sort()
          break
        elif x=='D':
          list_down.append(y)
          list_down=list(dict.fromkeys(list_down))
          list_down.sort(reverse=True)
          break
        else:
          print('invalid')

      print(list_up)
      print(list_down)
    else:
      print('invalid floor')
  except:
    print('invalid floor')
    continue
