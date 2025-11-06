import math
import sys
ques =  input("Sua matriz é de terceira ordem?")
if ques.title() != "Sim":
    ques_dois= input("Sua matriz é de segunda ordem?")
    if ques_dois.title() != "Sim":
        print(f"Sua matriz é inválida para este código.")
    else:
        line_one2 = input("Digite os 2 elementos da primeira linha de sua matriz, separados por ';'")
        line_two2 = input("Digite os 2 elementos da segunda linha de sua matriz, separados por ';'")
        line_2_1 = line_one2.strip().split(";")
        line_2_2 = line_two2.strip().split(";")
        line_2_1 = [eval(x.replace("^", "**")) for x in line_2_1]
        line_2_2 = [eval(x.replace("^", "**")) for x in line_2_2]
        if len(line_2_1) != 2 or len(line_2_2) != 2:
            print("Quantidade de elementos insuficientes ou excedente, processo finalizando.")
            sys.exit()
        diag_prin2 = line_2_1[0]*line_2_2[1]
        diag_sec2 = line_2_1[1]*line_2_2[0]
        det2 = diag_prin2 - diag_sec2
        print(f"A determinante da sua matriz é {det2}")
else: 
    line_one3 = input("Digite os 3 elementos da primeira linha de sua matriz, separados por ';'")
    line_two3 = input("Digite os 3 elementos da segunda linha de sua matriz, separados por ';'")
    line_three3 = input("Digite os 3 elementos da terceira linha de sua matriz, separados por ';'")
    line_3_1 = line_one3.strip().split(";")
    line_3_2 = line_two3.strip().split(";")
    line_3_3 = line_three3.strip().split(";")
    line_3_1 = [eval(x.replace("^", "**")) for x in line_3_1]
    line_3_2 = [eval(x.replace("^", "**")) for x in line_3_2]
    line_3_3 = [eval(x.replace("^", "**")) for x in line_3_3]
    if len(el1_3) != 3 or len(el2_3) != 3 or len(el3_3) != 3:
            print("Quantidade de elementos insuficientes ou excedente, processo finalizando.")
            sys.exit()
        ##CORRECAO NECESSARIA A PARTIR DESTE PONTO, AINDA NÃO MEXI
    diag_prin3 = float(el1_3[0])*float(el2_3[1])*float(el3_3[2]) + float(el1_3[1])*float(el2_3[2])*float(el3_3[0]) + float(el1_3[2])*float(el2_3[0])*float(el3_3[1])
    diag_sec3 = float(el1_3[2])*float(el2_3[1])*float(el3_3[0]) + float(el1_3[0])*float(el2_3[2])*float(el3_3[1]) + float(el1_3[1])*float(el2_3[0])*float(el3_3[2])
    det3 = diag_prin3 - diag_sec3
    print(f"A determinante da sua matriz é {det3}")
