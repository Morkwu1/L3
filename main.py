import math


def zadanie1():
    str1 = input("Ваши фамилия, имя? ")
    str2 = input("В какой школе Вы учитесь? ")
    str3 = input("ФИО    Вашего руководителя по информатике? ")
    info = "Ваши фамилия, имя: " + str1 + "\nВы учитесь в школе: " + str2 + "\nФИО Вашего руководителя по информатике: " + str3
    print(info)




def zadanie2():
    a1 = int(input("Перввая  сторрона первого треугольника "))
    b1 = int(input("Вторая сторрона первого треугольника "))
    c1 = int(input("Третья сторона первого треугольника "))
    a2 = int(input("Перввая  сторрона второго треугольника "))
    b2 = int(input("Вторая сторрона второго треугольника "))
    c2 = int(input("Третья сторона второго треугольника "))
    pp1 = (a1 + b1 + c1) / 2
    pp2 = (a2 + b2 + c2) / 2
    s1 = math.sqrt(pp1 * (pp1 - a1) * (pp1 - b1) * (pp1 - c1))
    s2 = math.sqrt(pp2 * (pp2 - a2) * (pp2 - b2) * (pp2 - c2))
    if s1 == s2:
        print("Равновеликие")
    else:
        print("Foul!!!")




def zadanie3a():
    print("вводите числа пока не 0")
    sum = 0
    k = 0
    while (True):
        n = int(input("введите число "))
        if n == 0:
            break
        sum += n
        k += 1
    print("сумма чисел = " + str(sum))
    print("количесвто чисел = " + str(k))




def zadanie3b():
    K = 0
    N = int(input("N = "))
    while (True):
        K += 1
        if 2 ** K > N:  # Найти наибольшее целое число K, при котором выполняется неравенство 2^K < N
            break

    print("K max = " + str(K - 1))




def zadanie4a():
    numbers = [3, 5, 2, 1, 7, 5, 8, 3]
    chet = 0
    nechet = 1
    for i in range(len(numbers)):
        if numbers[i]%2 == 0:
            chet += numbers[i]

        else:
            nechet *= numbers[i]
    print("сумма элементов с четными номерами: " + str(chet))
    print("произведение элементов с нечетными номерами: " + str(nechet))
zadanie3a()