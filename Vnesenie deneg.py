import datetime
file = open ('Vvod_deneg.txt', 'a+', encoding='utf-8')
print("Каким способом вы хотите пополнить счёт?")
print("1. Банковской картой \n"
      "2. С мобильного счёта \n"
      "3. С банкомата \n"
      "4. С электронных кошельков других платежных систем \n")
sposob = int(input("Введите номер варианта: "))

if (sposob == 1):
      sumw = float(input("Введите сумму (руб.): "))
      if (sumw >= 1.00 and sumw <= 15000.00):
          year = datetime.datetime.today()
          file.write(str(year)[:16]+ "; Банковской картой; ", str(sumw) + "\n")
      else:
            print("Неправильная сумма")
elif (sposob == 2):
      sumw = int(input("Введите сумму (руб.): "))
      if (sumw >= 10.00 and sumw <= 50000.00):
            year = datetime.datetime.today()
            file.write(str(year)[:16] + "; Мобильный счёт; " + str(sumw) + "\n")
      else:
            print("Неправильная сумма")
elif (sposob == 3):
      sumw = float(input("Введите сумму (руб.): "))
      if (sumw >= 50 and sumw <= 10000000 and sum % 50 == 0):
            year = datetime.datetime.today()
            file.write(str(year)[:16] + "; Банкомат; " + str(sumw) + "\n")
      else:
            print("Неправильная сумма")
elif (sposob == 4):
      sumw = float(input("Введите сумму (руб.): "))
      if (sumw >= 1.00 and sumw <= 500000.00):
            year = datetime.datetime.today()
            file.write(str(year)[:16] + "; С другого электронного кошелька; " + str(sumw) + "\n")
      else:
            print("Неправильная сумма")
else:
      print("Неверный ответ")
file.close()
