
print ("")

print ("Hello, my friend!")
print ("Введите количесто чисел")
kolvo = int(input("Количество = "))
print ("Отлично, а теперь нужно будет ввести сами числа!")
brr = []
for i in range (kolvo):
    brr.append(int(input("Введите число = ")))
 
print ("Введите знак + , - , /, * или **")
znak = input("Ваш знак это: ")
match znak:
    case '+':
        print ("OK")
        print ("Ответ = ", sum(brr))
    case '*':
        proizvedenie = brr [0]
        print ("OK")
        for i in range (len.brr):
            proizvedenie *=brr[i] 
            print ("Произведение всех чисел = ", proizvedenie)
            
    case '/':
        proizvedenie = brr [0]
        print ("OK")
        for i in range (len.brr):
            proizvedenie /=brr[i] 
            print ("Бебра всех чисел = ", proizvedenie)
        
        
        
        
       