from pathlib import Path
import csv

path= Path("C:/Users/Fernanda/OneDrive/Escritorio/FonEsp/Notas2025.csv")
lines = path.read_text(encoding='utf-8').splitlines()

reader= csv.reader(lines)
header_row= next(reader)
#print(header_row)
#for index, column_header in enumerate(header_row):
#    print(index, column_header)

#This turns numbers into German gradaes: 1.0, 1.3, 1.7, 2.0, and so on
def approx(x):
    y= round(x, 2) -int(x)
    if y <= 0.15:
        return int(x) + 0.0
    if y > 0.15 and y <= 0.57:
        return int(x) + 0.3
    if y > 0.57 and y <= 0.88:
        return int(x) + 0.7
    else: return int(x) + 1
#get variables of interest
for row in reader:
    name= row[1]
    a1= float(row[4])
    a2= float(row[7])
    a3= float(row[8])
    a_av= (a1+a2+a3)/3
    mt= float(row[9])
    ex= float(row[10])
    final= approx(a_av)*0.2 + (mt*0.3) + (ex*0.5)
    path2 = Path(f"C:/Users/Fernanda/OneDrive/Escritorio/FonEsp/emails2025/{name}.txt")
    path2.write_text(f"Hola {name}, \nEstas son tus notas del curso: \nTareas (20%): ({str(a1)} + {str(a2)} + {str(a3)})/3 = {str(approx(a_av))} \nParcial (30%): {str(mt)} \nExamen (50%): {str(ex)} \nNota final: {str(approx(final))}. \nFelicitaciones y felices vacaciones, \nFernanda")
