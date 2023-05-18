from xml.etree import ElementTree
import csv


"""Přečti XML"""
xml = ElementTree.parse(".../jafa_test.xml") #  vlož správnou cestu k xml souboru, nezapomeň změnit zpětná lomítka na dopředná pracuješ-li ve WIN


"""Vytvoř soubor CSV a otevři ho k zapisování"""
csvfile = open(".../jafa_data_ws.csv", 'w', encoding='utf-8') # vlož cestu, kam má být soubor CSV exportován, lomítka dtto


"""Vytvoř hlavičku do CSV"""
my_writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_ALL)
my_writer.writerow(["c_karty", "nazev", "puvodce", "tem_popis"])


"""Najdi všechny elementy s názvem row"""
for row in xml.findall("row"):
    if (row):


        """V každém elementu row najdi podřízené elementy s názvy"""
        c_karty = row.find("c_karty").text
        nazev = row.find("nazev").text
        puvodce = row.find("puvodce").text
        popis = row.find("tem_popis").text


        """Řádek v CSV sestava textů proměnných z získaných v předešlém úkolu"""
        csv_line = [c_karty, nazev, puvodce, popis]


        """Definovaný řádek zapiš do CSV"""
        my_writer.writerow(csv_line)

"""Zavři soubor CSV"""
csvfile.close()


"""Vypiš informaci, že je úkol hotov"""
print('\nCSV je hotovo')
