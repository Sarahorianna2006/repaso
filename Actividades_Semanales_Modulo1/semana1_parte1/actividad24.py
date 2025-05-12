#Fecha formateada, Pide al usuario el día, mes y año por separado e imprime la fecha en formato: "DD/MM/AAAA" y también "AAAA-MM-DD"

dia = int(input("Ingresa un dia de manera numerica: \n>"))
mes = int(input("Ingresa un mes de manera numerica: \n>"))
ano = int(input("Ingresa un ano de manera numerica: \n>"))

#fecha_total1 = dia + "/" + mes + "/" + ano + "/"
#fecha_total2 = ano + "-" + mes + '/' + dia + "/"

print(f"El dia, mes y ano que ingresaste en dos formatos ordenados:\n Formato DD/MM/AAAA = {dia}/{mes}/{ano}\n formato AAAA-MM-DD: {ano}-{mes}-{dia}")