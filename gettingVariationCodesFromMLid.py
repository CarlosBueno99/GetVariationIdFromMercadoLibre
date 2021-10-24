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


with open( csvDestination , 'w',encoding="utf-8", newline='') as csvout:
    writer = csv.writer(csvout)

    #define o cabeçalho do arquivo
    writer.writerow(["Tray-Pai","MLB-Pai","MLB-filho","Nome-produto","Var1","var2","var3","Nome-concatenado"])
    with open('csvIn.csv', newline='') as csvin:
        reader = csv.DictReader(csvin)
        for row in reader:
            conn.request("GET", "/items/"+row['codigo_MLB_padre'], payload, headers)
            res = conn.getresponse()
            data = res.read()
            response = json.loads(data)
            product_name = response["title"]

            #this step goes into the response and grabs the desired information from Mercado Libre's API
            for variation in response["variations"]:
    
                print(variation["id"])
                print(row['codigo_MLB_padre'])

                
                

                
                if len(variation["attribute_combinations"][0]["value_name"].split("/")) == 3:
                    vari1 = variation["attribute_combinations"][0]["value_name"].split("/")[0].strip()
                    vari2 = variation["attribute_combinations"][0]["value_name"].split("/")[1].strip()
                    vari3 = variation["attribute_combinations"][0]["value_name"].split("/")[2].strip()

                    #essa com 3
                    nome_concatenado = product_name+" cor:"+vari1+";Tamanho:"+vari2+"vari3:"+vari3
                elif len(variation["attribute_combinations"][0]["value_name"].split("/")) == 2:
                    vari1 = variation["attribute_combinations"][0]["value_name"].split("/")[0].strip()
                    vari2 = variation["attribute_combinations"][0]["value_name"].split("/")[1].strip()
                    vari3 = "N/A"

                    #essa com 2
                    nome_concatenado = product_name+" cor:"+vari1+";Tamanho:"+vari2
                else:
                    vari1 = variation["attribute_combinations"][0]["value_name"].split("/")[0].strip()
                    vari2 = "N/A"
                    vari3 = "N/A"

                    #Essa com 1
                    nome_concatenado = product_name+" cor:"+vari1
                
                

                print(nome_concatenado)


                writer.writerow([row['codigo_padre_plataforma'],row['codigo_MLB_padre'], variation["id"] ,product_name,vari1,vari2,vari3,nome_concatenado])
                

