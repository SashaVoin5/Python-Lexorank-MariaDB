import pymysql

import random


try:
    Connection = pymysql.connect(
        host="localhost",        
        user="newuser",
        password="password",
        db="Todo"        
    )

    cur = Connection.cursor()


    while True:
        print ("")
        print ("Выберите команду,указав номер команды")
        print ("1.Select * from Todo")
        print ("2.Add the new Todo on the end")
        print ("3.Add the new task on the middle")
        print ("4.select * from Todo order by Priority desc")
        print ("5.Exit for the programm")
        command = str(input())

        def lexorang(a, b):
            # Получаем длину самой длинной строки
            max_len = max(len(a), len(b))
            # Добавляем нули в начало строк, чтобы они имели одинаковую длину
            a = a.ljust(max_len, '0')
            b = b.ljust(max_len, '0')
            # Проходимся по каждому символу и вычисляем значения для каждого из них
            rank_a, rank_b = 0, 0
            for i in range(max_len):
                rank_a += (ord(a[i]) - ord('A') + 1) * (26 ** (max_len - i - 1))
                rank_b += (ord(b[i]) - ord('A') + 1) * (26 ** (max_len - i - 1))
            # Вычисляем среднее арифметическое для полученных значений
            mid_rank = (rank_a + rank_b) // 2
            # Переводим полученное значение обратно в строку и возвращаем
            res = ''
            while mid_rank > 0:
                mid_rank -= 1
                res = chr(mid_rank % 26 + ord('A')) + res
                mid_rank //= 26
            return res.ljust(max_len, 'A')


        def lexorang_nextrank(a):

            # Convert to lowercase for case insensitivity
            a = a.lower()
            # Convert to list of characters
            a_list = list(a)
            # Iterate from right to left to find the first non-'z' character
            for i in range(len(a) - 1, -1, -1):
                if a_list[i] != 'z':
                    # Increment the character
                    a_list[i] = chr(ord(a_list[i]) + 1)
                    # Pad with 'a's on the right
                    a_list[i+1:]= ['a'] * (len(a) - i - 1)
                    break
            else:
                # If all characters are 'z', add 'a' to the end
                a_list.append('a')

            # Convert list back to string and return
            return ''.join(a_list)

        if (command == '1'):
            cur.execute("SELECT * FROM Todo")
            
            print ("")
            # получение результатов
            results = cur.fetchall()

            # вывод результатов
            for row in results:
                print(row)
            print ("")
            

        if (command == '2'):
            cur.execute("SELECT Priority FROM Todo  ORDER BY Priority desc")

            # получение результатов
            results = cur.fetchall()
            
            # вывод результатов
            for row in results:
                mas = str(row)
                break           
            #Строка формата "('n',)" преобразуется в n
            number = mas[2:-3]
            
            print("Введите имя задачи")
            name = str(input())
            print("Введите Комментарий для задачи")
            Comment = str(input())
            print("Введите дедлайн для задачи")
            DeadLineDate = str(input())
            rand = random.randint(20,100)
            outlex = number
            i=0
            for i in range(rand):
                outlex=lexorang_nextrank(outlex)
            
            
            outlex=str(outlex.upper())         
            cur.execute(f"insert into Todo (Name,Comment,DeadLineDate,Priority) VALUES ('{name}','{Comment}','{DeadLineDate}','{outlex}')")
            Connection.commit()
            print(f"Задача успешно добавлена, ее приоритет {outlex}")
            
        
            
        if ((command == '3')):
            print("Введите имя задачи")
            name = str(input())
            print("Введите Комментарий для задачи")
            Comment = str(input())
            print("Введите дедлайн для задачи")
            DeadLineDate = str(input())
            print ("Введите через пробел два ID, между которыми вы хотите поместить вашу новую запись")     
            inp = str(input())
            inpspl = inp.split()
            id1 = inpspl[0]
            id2 = inpspl[1]
            print(id1)
            print(id2)

            cur.execute(f"SELECT Priority FROM Todo  where id ={id1}")          
            results = cur.fetchall()           
            for row in results:
                Lexorank1 = str(row)
                break           
            Lexorank1 = Lexorank1[2:-3]
            print(Lexorank1)
            cur.execute(f"SELECT Priority FROM Todo  where id ={id2}")          
            results = cur.fetchall()           
            for row in results:
                Lexorank2 = str(row)
                break  
            Lexorank2 = Lexorank2[2:-3]
            print(Lexorank2)
            middleLexorank = lexorang(Lexorank1,Lexorank2)
            middleLexorank=middleLexorank.upper()
            print(middleLexorank)

            cur.execute(f"insert into Todo (Name,Comment,DeadLineDate,Priority) VALUES ('{name}','{Comment}','{DeadLineDate}','{middleLexorank}')")
            Connection.commit()
            print(f"Задача успешно добавлена, ее приоритет {middleLexorank}")

        if ((command == '4')):
            cur.execute("select * from Todo order by Priority desc")
            
            print ("")
           
            results = cur.fetchall()
            
            for row in results:
                print(row)
            print ("")
            


        if ((command == '5')):
            cur.close()
            Connection.close()
            print("programm close")
            break
    
except Exception as ex:
    print(ex)