
work = []
work_is_true = []
work_time = []
#count the work
n = 10
for i in range(n):
    Ans = input("add,display,remove,edit,search,done,details,exit,help :").lower()
    if Ans == "add":
        name_work = input("Enter your name work :").lower()
        if name_work not in  work:
              work.append(name_work)
              work_is_true.append(False)
              work_time.append(None)
              print("ADD!!!")
        else:
              print("Not ADD!!")
    elif Ans in "display":
        for i , Ans in enumerate(work):
            print(i+1, Ans, work_is_true[i], work_time[i])
    elif Ans in "edit":
        name_work = input('Enter your edit name: ').lower()
        if name_work in work:
            new = input("inter your new name:").lower()
            if new not in work:
                i = work.index(new)
                work[i] = new
                print("Edit!!") 
            else:
                print("Exit")
        else:
            print("Not Remove")        
    elif Ans in "remove":
        name = input("name for remove: ").lower()
        if name in work:
            i = work.index(name)
            work.pop(i)
            work_is_true.pop(i)
            work_time.pop(i)
            print("Removed!")
        else:
            print("Not found!")
    elif Ans in "search":
        name = input("name for search: ").lower()
        if name in work:
            i = work.index(name)
            name = work[i]
            status = work_is_true[i]
            time = work_time[i]
            
            print(f"name :{name},Status: {status}, time: {time}")
        else:
            print("Not found!")  
    elif Ans in "done":
        name = input("Enter your name work:")
        if name in work:
            i = work.index(name)
            
            hour_start= int(input("Enter your hour :"))
            Minute_start =int(input("Enter your Minute:"))
            hour_finish= int(input("Enter your hour finish :"))
            Minute_finish = int(input("Enter your Minute finish:"))
            mines_hour = hour_finish - hour_start
            mines_Minute = Minute_finish - Minute_start
            work_is_true[i]=True
            work_time[i] =f"{ hour_start : Minute_start} :{hour_finish}:{Minute_finish} ,deference:{mines_hour}:{mines_Minute} "
            print(f" {work[i]},start:{hour_start}:{Minute_start},Finish :{hour_finish}:{Minute_finish} ,deference:{mines_hour}:{mines_Minute} ")
            print("Done")
        else:
            print("Not done!!!!")
    elif Ans in"details":
        print(f"work:{work},work_is_don:{work_is_true},time:{work_time}")
    elif Ans in "help":
        print("ADD:insert your information work.")
        print("Display:show the all information")
        print("remove:replace the name work .")
        print("Edit:change your information.")
        print("Search:found the name and show the information about the name.")
        print("Done:mark the work and insert your time start and end.")
        print("Display Details:show information work mark and not don work and time worked")
        print("exit:end the plan")
        
    elif Ans == "exit":
        break