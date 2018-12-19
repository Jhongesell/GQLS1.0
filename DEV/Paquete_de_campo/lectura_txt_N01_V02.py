fichero = open ('ADCP/El_Tigre_180417_000_18-04-17_ASC.TXT')

fichero.readline();
fichero.readline();

for linea in fichero:
    print(linea, ' ** longitud:', len(linea))