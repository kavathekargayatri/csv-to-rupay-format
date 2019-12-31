import pandas as pd
from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import dumps
import csv
import json
import jsonCreator
import sys
import dataFromApi
from createDirectories import inputPath

dfApi = dataFromApi.dataframeFromDb()
dfApi.astype(str)

# print(dfApi.head(10))
# print(dfApi.columns)
try:
    consumer = KafkaConsumer(group_id = 'grp6',bootstrap_servers=['localhost:9092'],auto_offset_reset='latest')
    consumer.subscribe(['csv_rupay'])
    print("Subscribed to a topic named csv_rupay. waiting for an event...")
    for message in consumer:
        print("Received an event.")
        print("Procesing... Please wait...")
        try:
            data = json.loads(message.value.decode('ascii'))
            # print(data)
            ID = data['ID']
            token = data['Token']
            print("ID : " + str(ID))
            print("Token : " + str(token))
        except:
            print("invalid input format")
            continue
        try:

            outputCsvPath = data['Payload']['Data']['Location']
            path = str(inputPath) + "/" + str(outputCsvPath)
            csvfile = open(path, 'r')
            for row in csv.DictReader(csvfile,delimiter=";"):
                key = (list(row.keys())[0])
                value = (list(row.values())[0])
                keys = key.split(",")
                values = value.split(",")
                dataList = []
                for k in range(len(keys)):
                    # print(str(keys[k])[1:])
                    # result = dfApi.where(dfApi['name'].astype(str) == 'Primary Account Number(Fortiate)')
                    result = dfApi.loc[dfApi['name'] == str(keys[k])[1:]]
                    result.reset_index(drop=True)
                    id = str(result['de'].values[0])
                    description = str(result['description'].values[0])
                    data = jsonCreator.jsonFormatConversion(id = id,name= keys[k],value=values[k],shortname="",description=description,subelements=[])
                    dataList.append(data)
                dataconsole = json.dumps(dataList,indent=4)
                print(dataconsole)
                producer1 = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                          value_serializer=lambda x: dumps(x).encode('utf-8'))

                producer1.send('parsed_data', value=data)
                print("Processed and published to a topic parsed_data.")
                print("...........................................................................................")

        except Exception as e:
            print(e)
            print("Invalid Payload format")
            continue
        print("Procesing... Please wait...")

    print('Closing consumer')
    consumer.close()
except Exception as e:
    print(e)

