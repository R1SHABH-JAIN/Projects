# basic todo list
def todo_list():
    tasks = []
    while True:
        print('1. Add task')
        print('2. show task')
        print('3. Mark as Complete')
        print('4. exit the todo list')
        print('\n')

         
        
        choice = int(input('choose any one of the option: '))  

        if choice == 1:   #Add task
         num_of_task = int(input('provide num of task you want to add: '))
         index_num = 1
         for i in range(0,num_of_task):
             task = input('input: ')
             tasks.append({'task':task,'progress':False,'index_count':index_num})
             index_num+=1
         print('task added successfully')
         
         print('\n')
        




        elif choice ==2:#show task
           for index , i in enumerate(tasks,1):
              if i['progress']:
                 print(f"{index}.{i['task']} - {'Complete'}")

              else:print(f"{index}.{i['task']} - {'Incomplete'}") 
           print('\n')  



        
        
        elif choice == 3:#Mark as Complete
           for index , i in enumerate(tasks,1):
                print(f"{index}: {i['task']}")

           print("which option you want to mark as done ")
           ind = int(input('index: '))

           for i in tasks:
              if ind == i['index_count'] :
                 i['progress'] = 'Completed'
                 
           for index , i in enumerate(tasks,1):
              print(f"{index}.{i['task']} - {i['progress']}")



           print('\n')

                 
           


        elif choice == 4:#exit the todo list
           exit=input('type any key to exit:')
           break



        else:print('invalid choice')


todo_list()













'''
1.issme zayada features nhi hai
2.function banaya hai "def" 
3.basic while loop   
4.normal list usske sath append use kiya hai 
5.for loop hai usske sath range hai 

6.while loop ke sath True iss leye taaki humara code baar baar run ho
or choice == 4 pe break hai taki true wala point tuut jaye

7.aakhir mai function ko call kara hai 

tasks = [{"kaam": 'coding', "progress": True}]

        if choice == '2':
            print("\nTasks:")
            for index, ii in enumerate(tasks,1):
                status = "Done" if ii["progress"] else "Not Done"
                print(f"{index }. {ii['kaam']} - {status}")



ab ye kaam kese karega - 
dict. mai ek ek key hoti hai usse corresponding value hoti hai 
kaam / progress - key hai 
coding / (False or True) - uper di keys ki corresponding values hai 

key ko call karege to value return karega 

hua ye ki enumerate use karte hai to index value bhi aati hai 
2nd line mai 'ii' ke paas 2 keys aayi or usski values aayi hai 
apn key ki values check karege 
progress ki value false hai to wo automatically not done mai chale jayega 

or fir f'string ka use karke hum hum tast name or usska progress print kar denge 


IMP = variable ka name soch ke rakhna chahiye taaki confusion na ho 
or esse banane chahiye ki wo name pehle use na huye ho 
UNIQUE hona chahiye 

'''


'''
faltu ke codes 

              # status = "Done" if i['progress'] else 'Not done'
              # print(f"{index}.{i['task']} - {status}")
        #  Ask_show_list = input('want to see todo list(y/n):')
        #  if Ask_show_list == 'y' or 'Y':
        #     count = 1
        #     for y in tasks:
        #        print(y)
        #        count+=1
        #  else:exit





                  #  for j in tasks:
          #     print(f"{i[index_num]}:{j['task']} - {j['progress']}")
          #  print('\n')
               

          #  print('\n')
'''


