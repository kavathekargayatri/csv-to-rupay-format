# Pre-processor

##### Table of Contents:  
+ [Introduction](#introduction) 
+ [Prerequisite](#prerequisite) 
+ [Input](#input) 
+ [Output](#output) 
+ [Dependancy](#dependancy)
+ [Getting the code](#getting_the_code)
+ [How To Run](#how_to_run)
+ [How To Access](#how_to_access)
    +[Using Terminal](#terminal)
    +[Using event api](#event_api))

<a name="introduction"/>



## Introduction:
This module sends json data of each transaction one by one to the topic "parsed_data".

<a name="Prerequisite"/>

## Prerequisite:
1. should have conda installed

            https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart 
      refer this for installation till step - 8

2. create environment to run csv_to_rupay: 

    type the following command in the command prompt inside the folder containing csvtorupay.py file
    
            conda env create -f environment.yaml
    Then you should see a environment created as (fortiate-env) then type the command 

            conda activate fortiate_env

        
3. install apache kafka:

            https://kafka.apache.org/downloads
    To start kafka follow the instructions in the link below:
    
    To start a server:
           
            bin/zookeeper-server-start.sh config/zookeeper.properties
            
    To start Zookeeper:
    
            bin/kafka-server-start.sh config/server.properties



<a name="input"/>

## Input:
Input of this topic is a json data containing location of a csv. 

event based : For input use Topic 'csv_rupay'.

<a name="output"/>

## Output:
Output of this module is a json data of each transaction.  

event based : For output use Topic 'parsed_data'.   


<a name="dependancy"/>

## Dependancy:
Need to start kafka for running event driven api.
1. Start kafka using :
    
   To start a server:
           
            bin/zookeeper-server-start.sh config/zookeeper.properties
            
    To start Zookeeper:
    
            bin/kafka-server-start.sh config/server.properties
                    

2. Add flask,flasgger,kafka-python modules in your environment if not present using:

            conda install kafka-python
            
            conda env export > environment.yaml

3. Need to start fields-dbservice : api.py

4. In case of event driven: cleaner's event.py
         

<a name="getting_the_code"/>

## Getting the code:
git pull in Importer folder inside python workspace:

>(SSH):

            git clone git@github.com:fortiate/preprocessor.git

>(HTTPS) :

            git clone https://github.com/fortiate/preprocessor.git
                   
    
<a name="how_to_run"/>

## How To Run:

### For running on Terminal:
> Open terminal inside Importer folder and run.

            python3 Terminal.py
            

### For Event driven api:
> Open terminal inside Importer folder and run 2 programs.

            python3 event.py
            
            python3 producer.py

<a name="how_to_access"/>

## How to access:
<a name="terminal"/>

1. Through Terminal by running programs.

    1. .Fortiate folder will be created in your system.  Which will be used to take and store the csv files
    
    2.  provide input csv name (ex. data_csv.csv)
    
    3.  provide output csv name(ex. processed_data_csv.csv).    
    
<a name="event_api"/>    
2. Through event driven api:
    
    >Step to start a consumer to consume messeges from a kafka topic:
    
            bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic Import --from-beginning
            
    >Step to start a producer to send messages into the kafka topic:
    
            bin/kafka-console-producer.sh --broker-list localhost:9092 --topic Import 
            
     For communication using topics:
     
    input message should be in json ex:
        
            {"DateTime": "28-11-19 15:58", "ID": "I1574936886", "Message": [], "Status": "Success", "Token": 1574936886, "code": [], "Payload": {"Parameters": {"action": "predict", "overwrite": "yes", "algoType": "regression", "entity1": "18", "algoName": "knn", "entity2": "4", "inputCsv": "", "outputCsv": ""}, "Data": ""}}
     
    Output message will be in a json format with success and error messsages and inputs provided by an "processed" kafka topic.
     


      


