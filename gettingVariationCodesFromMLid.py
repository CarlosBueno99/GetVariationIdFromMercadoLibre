import csv
import http.client
import json

#nome do csv que vai ser gerado (não mudar):
csvName = 'codigoshijos.csv'
idhijo = ''


#lugar onde você quer que o CSV esteja localizado
csvDestination ='C:\\Users\\carlo\\Documents\\git\\GetVariationIdFromMercadoLibre\\OUT\\codigoshijos.csv'



#variaveis diversas, não mexer
directory = ''
incidentNumber = ''



#variaveis do http.client


conn = http.client.HTTPSConnection("api.mercadolibre.com")
payload = ''
headers = {}
conn.request("GET", "/items/MLB2026657802", payload, headers)
res = conn.getresponse()
data = res.read()
response = json.loads(data)


with open( csvDestination , 'w', newline='') as csvout:
    writer = csv.writer(csvout)
    writer.writerow(["Tray-Pai","MLB-Pai","MLB-filho","Value-name"])
    with open('csvIn.csv', newline='') as csvin:
        reader = csv.DictReader(csvin)
        for row in reader:
            
            
            
            print(row['codigo_padre_plataforma'],"|"+"|", row['codigo_MLB_padre'])



print("CSV criado com sucesso:", csvDestination+ csvName)



for variation in response["variations"]:
    
    print(variation["id"])


    print(variation["attribute_combinations"][0]["value_name"].split(" / "))

    cor_vari = variation["attribute_combinations"][0]["value_name"].split(" / ")[0]
    tam_vari = variation["attribute_combinations"][0]["value_name"].split(" / ")[1]
    print(cor_vari,tam_vari)
    
        
        

    