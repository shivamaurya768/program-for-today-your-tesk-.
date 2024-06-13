#program for  today tesk enter...
print(""*3,'WELCOME TO MANAGEMENT TASK IN APP',""*3,'\n') 
list=[]
le=int(input("How many your task"))
for i in range(1,le+1):
   a=input(f"Enter your task {i} == ")
   list.append(a)
print(f"Today  task \t {list}")
while True:
   add=int(input("Enter 1 : add\nEnter 2 : update\nEnter 3 : Delete\nEnter 4 : View\nEnter 5 : exit/stop \n please choise note \t"))
   if(add==1):
      ad=input("Enter your task : ")
      list.append(ad)
   elif(add==2):
      up=input("Enter your tesk,you want to update ")
      list.remove(up)
      a=input("Enter your new task ")
      list.append(a)
   elif(add==3):
      de=input("Enter your delete task ")
      list.remove(de)
   elif(add==4):
      print(f"your Today task ==   {list} \n")
   elif(add==5):
      print("Your App is exit ")
      break
   else:
         print('Enter vaild note\n')