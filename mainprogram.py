
from mainclass import Students
# دالة لإضافة طالب جديد إلى الملف JSON
manage = Students()
while True :    
    try :
        service = int (input("""
what do you want ?
  1 : add student
  2 : update studnt data
  3 : chose random student
  4 : delete student
  5 : marks avrage
  6 : exit
"""))
    except :
        print("ادخل ارقام فقد")

    if service == 1 :
        try :
            name = input("enter the neme\n")
            mark = int(input("enter mark\n"))
            manage.add_student(name,mark)
            
        except:
            print("ادخل الدرجات بالأرقام فقط")
    elif service == 2 :
        try :
            name = input("enter the neme\n")
            mark = int(input("enter mark\n"))
            manage.update(name,mark)
        except:
            print("ادخل الدرجات بالأرقام فقط")
    elif service ==3 :
        manage.random_student()
    elif service == 4 :
         name = input("enter the neme\n")
         manage.delete(name)
    elif service == 5 :
        avrage = manage.average() 
        print(avrage)
    elif service == 6 :
        break
    else : 
        print(" ادخل قيمة صحيحة")  