import json
from pprint import pprint

online_script = ('''{
      "@context": "https://schema.org",
      "@type": "Dataset",
      "name": "High Resolution Layers - Mal\u00e9 lesn\u00ed prvky (Small Woody Features)",
      "description": "High Resolution Layers (HRL) jsou rastrov\u00e1 data s prostorov\u00fdm rozli\u0161en\u00edm 5 m, kter\u00e9 jsou sou\u010d\u00e1st\u00ed programu Copernicus pro monitorov\u00e1n\u00ed \u00fazem\u00ed. Produkt Mal\u00e9 lesn\u00ed prvky (Small Woody Features) obsahuje informace o line\u00e1rn\u00edch struktur\u00e1ch, jako jsou \u017eiv\u00e9 ploty, a tak\u00e9 ploch\u00e1ch (od 200 m\u00b2 do 5 000 m\u00b2) lesn\u00edch prvk\u016f. Data jsou vytv\u00e1\u0159ena poloautomatick\u00fdmi postupy nad dru\u017eicov\u00fdmi sn\u00edmky ka\u017ed\u00e9 3 roky. Technick\u00e9 specifikace dat naleznete zde: https:\/\/land.copernicus.eu\/user-corner\/technical-library, informace o programu na http:\/\/land.copernicus.eu.",
      "url": "https://micka.cenia.cz/record/basic/60745faa-af78-4c22-b825-2342c0a80164",
      
      "spatialCoverage": {
            "@type":"Place",
            "geo":{
            "@type":"GeoShape",
            "box":"12.09 48.551 18.860 51.056"
         }
      },
      "keywords": ["Krajinn\u00fd pokryv","N\u00e1rodn\u00ed","High Resolution Layers","Mal\u00e9 lesn\u00ed prvky","Copernicus"],
      "distribution": [{
        "encodingFormat": "OGC:WMS-1.3.0-http-get-capabilities",
        "contentUrl": "https://gis.cenia.cz/geoserver/hrl/wms?service=WMS&request=GetCapabilities",
        "name": ""
      },{
        "encodingFormat": "WWW:DOWNLOAD-1.0-http--download",
        "contentUrl": "https://geoportal.gov.cz/atom/hrl/SWF_2015_05m_CR.zip",
        "name": ""
      }],
      
          "creator": {
            "@type": "Organization",
            "url": "https://www.eea.europa.eu/",
            "name": "Evropsk\u00e1 agentura pro \u017eivotn\u00edho prost\u0159ed\u00ed"
          },
        
          "license": "https://creativecommons.org/licenses/by/4.0/",
        
      "dateModified": "2022-12-15"
    }''')


# Parse the JSON content of the script element into a dictionary
json_content = json.loads(online_script)
# Extract the values from json_content as new variables
title = json_content['name']
name = json_content['distribution']
subject = json_content['keywords']
description = json_content['description']
dateModified = json_content['dateModified']
rightsManagement = json_content["license"]
coverage = json_content["spatialCoverage"]["geo"]["box"]
creator = json_content["creator"]["name"]
type = json_content["@type"]

# resource_identifier =
print('\n')
metadata = (title, name, subject, description, dateModified, rightsManagement, coverage, creator, type)
for i in metadata:
    print(str(i))
