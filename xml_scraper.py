from bs4 import BeautifulSoup
import csv
import glob

#  Tento skript je o trochu chytřejší, extrahuje vybraná data z všech xml souborů uložených v podadresáři /Data1 a vytvoří seznam do souboru CSV.
#  K jeho spuštění je potřeba doplnit Python interpreter o rozšíření s názvem BeautifulSoup/bs4.


def get_xml_files():
    """Sestaví seznam všech xml v adresáři"""
    path = r'.../DATA1/*.xml'  # Zadej správnou cestu k datům a nezapomeň na dopředná lomítka
    xml_files = glob.glob(path)
    #  print('Počet souborů xml v adresáři: ',(len(xml_files)))
    return xml_files


xml_files = get_xml_files()


def read_xml_files(xml_files):
    """Vytěží data z xml souborů do jednoduchého seznamu ve formátu CSV"""
    csvfile = open('.../test_lv.csv', 'w', newline='', encoding='UTF-8')  # Zadej správnou cestu k datům a nezapomeň na dopředná lomítka
    for x in xml_files:
        with open(str(x), "r", encoding="UTF-8") as xml:  # přečte soubory XML a nalezené hodnoty za píše do proměnných.
            file = xml.read()
            soup = BeautifulSoup(file, 'lxml-xml')
            ico = soup.find('are:ICO', None).text
            fma = soup.find('are:ObchodniFirma', None).text
            try:
                zapis = soup.find('are:DatumZapisu', None).text
                vymaz = soup.find('are:DatumVymazu', None).text
            except(AttributeError, NameError):
                pass

            output = (ico, fma, zapis, vymaz)

        my_writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_ALL) #  Nastavení oddělovače v CSV a ohraničení řetězců do dvojitých uvozovek.
        my_writer.writerow(["ico", "firma", "datum_zapisu", "datum_vymazu"]) #  Vytvoření hlavičky v CSV.
        my_writer.writerow(output) #  Vyplní CSV obsahem proměnných.
    csvfile.close()
    print('CSV je hotovo')


read_xml_files(xml_files)
