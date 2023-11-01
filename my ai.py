

print("Apakah kamu mau cerita? ")
pil = input()
if pil == 'y' :
    button = False
    while not button:

        print("Mau siapa yang mendengarkan mu : ")
        print("1. Nahida \n",
              "2. Kafka ")
        people = int (input("pilih pake angka (tekan 0 untuk keluar ): "))
        if people == 1 :
            print("Sekarang kamu bersama nahida")
            from nahida import Nahida
            print(Nahida)
            button = False
        if people == 2:
            from kafka import Kafka
        if people == 0 :
            print ("bye bye")
            button = True