import datetime
import locale

import requests
from bs4 import BeautifulSoup


def current_nummes_mes(mesnum):
    monthn = 0
    months = {1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",7:"julio",8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"}
    indice = 1
    for x in months:
        if indice == mesnum:
            monthn = months.get(indice)
        indice+=1
    return monthn
def current_mes_num(date):
    months = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
    monthn = months[date.month - 1]
    return monthn
def current_mes_format(date):
    months = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    month = months[date.month - 1]
    return month
def uf_hoy(op):
    global uf_mas_dia
    diahoy = datetime.datetime.today()
    if op == 'si':
        diahoyx=diahoy.day
        meshoy=current_mes_num(diahoy)
        meshoyx=current_mes_format(diahoy)
    else:
        meshoy = int(input("Ingrese el mes (1-12) del valor de la UF:"))
        meshoyx = str(current_nummes_mes(meshoy))
        diahoyx = int(input("Ingrese el día (1-31) del mes del valor de la UF:"))
    yearx = diahoy.year
    r = requests.get('http://www.sii.cl/valores_y_fechas/uf/uf2021.htm')
    soup = BeautifulSoup(r.text, 'lxml')
    table_mes = soup.find('div', attrs={'id': 'mes_'+meshoyx})
    diatab = {0:1,1:11,2:21,3:2,4:12,5:22,6:3,7:13,8:23,9:4,10:14,11:24,12:5,13:15,14:25,15:6,16:16,17:26,18:7,19:17,20:27,21:8,22:18,23:28,24:9,25:19,26:29,27:10,28:20,29:30,30:32,31:33,32:31}
    indice = 0
    for x in diatab:
        if(diatab.get(indice)==diahoyx):
            tagd = soup.find('div', {'id': 'mes_' + meshoyx}).select('td')[indice]
            uf=str(tagd)[16:25]
            uf_mas_dia=uf+"-"+str(diahoyx)+":"+meshoyx+"*"+str(yearx)
        indice+=1
    return uf_mas_dia


monto = float(input("Ingrese el monto en UF a calcular en $ CLP:"))
opcion = input("Quiere calcular el monto con la UF de hoy? (si/no):")
ufdi = uf_hoy(opcion)
uf = ufdi[0:9]
ufx = uf.replace('.','')
ufxi = ufx.replace(',','.')
ufd = float(ufxi)
montouf = monto*ufd
locale.setlocale(locale.LC_ALL, '')
resmontuf = locale.format_string("%d",montouf,1)
if opcion == 'si':
    print("\nEl Monto en pesos chilenos con la uf de hoy a $ "+uf+" es: $"+str(resmontuf))
else:
    print("\nEl Monto en pesos chilenos con la uf del "+str(ufdi[ufdi.find("-")+1:ufdi.find(":")])+" de "+ufdi[ufdi.find(":")+1:ufdi.find("*")]+" de "+ufdi[ufdi.find("*")+1:len(ufdi)]+" a $ "+uf+" es: $"+str(resmontuf))
input("Press enter to exit ;)")