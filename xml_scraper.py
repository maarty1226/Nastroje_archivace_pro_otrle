from bs4 import BeautifulSoup
import csv
import glob
import multiprocessing


def get_xml_files():
    """Sestaví seznam všech xml v adresáři"""
    path = r'D:/ws_pce/DATA1/*.xml'
    xml_files = glob.glob(path)
    #  print('Počet souborů xml v adresáři: ',(len(xml_files)))
    return xml_files


xml_files = get_xml_files()


def read_xml_files(xml_files):
    """Vytěží data z xml souborů do jednoduchého CSV"""
    csvfile = open('D:/ws_pce/test_lv.csv', 'w', newline='', encoding='UTF-8')
    for x in xml_files:
        with open(str(x), "r", encoding="UTF-8") as xml:
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

        my_writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_ALL)
        my_writer.writerow(["ico", "firma", "datum_zapisu", "datum_vymazu"])
        my_writer.writerow(output)
    csvfile.close()
    print('CSV je hotovo')


read_xml_files(xml_files)
