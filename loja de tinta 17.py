area=float(input("Qual o tamanho em metros quadrados da área a ser pintada? "))
area = 1.1*area

if area%108==0:
    lata = area /108
else:
    lata= (area//108)+1

if area%21.6==0:
    galao= area/21.6
else:
    galao=(area//21.6)+1

if area% 108!= 0:
    gal =area//108
    if((area%108)%21.6)==0:
        lat=((area%108)/21.6)+1
    else:
        lat = ((area%108)//21.6)
print ("---------------------------------------------------------------------")
print ("Opção de usar lata: ")
print(f" Pode usar {galao:.0f} lata de 3.6L e custará {(galao*25):.2f} reais")
print ("Opção de usar galão: ")
print(f" Pode usar {lata:.0f} galão de 18L {(lata*80):.2f} reais")
print ("---------------------------------------------------------------------")
if area <= 64.8:
    print(f" Vai usar {galao:.0f} lata de 3.6L e cutará: {(galao*25):.0f} reais") 

elif area > 54 and area > 108:
    print (f"{lata:.0f} lata de 18l. custará: {(lata*80):.2f} reais")


