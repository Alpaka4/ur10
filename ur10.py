##import random
##students_list=["Гарри Поттер","Гермиона Гренйджер","Драко Малфой","Рон Уизли",
##          "Луна Лавгуд","Невилл Лонгботтом","Чо Чанг"]
##gryffindor=[]
##slytherin=[]
##hufflepuff=[]
##while len(students_list) !=0:
##    student=random.choice(students_list)
##    choice=random.randint(1,300)
##    if choice <=100:
##        gryffindor.append(student)
##        print(student + " отправляется в Гриффиндор")
##    elif choice <=200:
##        slytherin.append(student)
##        print(student + " отправляется в Слизерин")
##    else:
##        hufflepuff.append(student)
##        print(student + " отправляется в Хафлпаф")
##    students_list.remove(student)
##print(len(gryffindor),"Отправляются в Грифендор")
##print("Это ", gryffindor)
##print(len(slytherin),"Отправляются в Слизерин")
##print("Это ", slytherin)
##print(len(hufflepuff),"Отправляются в Хафлпаф")
##print("Это ", hufflepuff)
##Задача 1
##Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
##Выведите все элементы, которые меньше 5.
##a=[1,1,2,3,5,8,13,21,34,55,89]
##for i in range(len(a)):
##    if a[i]<5:
##        print(a[i])
##Задача 2
##Даны списки:
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
##b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
##Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
##c=[]
##for i in range(len(a)):
##    contains=0
##    num=a[0]
##    for i in range(len(b)):
##        if num==b[i]:
##            contains=1
##            break
##    if contains==1:
##        c.append(num)
##        a.remove(num)
##print(c)
###№Задача 3
##import random
##lst=[]
##s=0
##for i in range(10):
##    lst.append(random.randint(1,10))
##    s+=lst[i]
##print(lst)
##print(s)
##Задача 4
##import random
##lst=[]
##p=1
##for i in range(10):
##    lst.append(random.randint(1,10))
##    if lst[i]%2!=0:
##        p*=lst[i]
##print(lst)
##print(p)
###№Задача 5
##import random
##lst=[]
##ch=0
##for i in range(10):
##    lst.append(random.randint(-10,10))
##    if lst[i]<0 and lst[i]%2==0:
##        ch+=1
##print(lst)
##print(ch)
#Задача 6
lst=[]
x=1
while len(lst)==10:
    for i in range(1,50,5):
        x.append(x)
        x+=5
print(lst)
