import requests
import pandas as pd

def dataframeFromDb():
    try:
        url = 'http://localhost:48311/api/fields'
        url = requests.get(url)

    except Exception as e:
        print("Cannot connect to an API")
        # sys.exit()
    fromdb = url.json()
    de = []
    name =[]
    description = []
    datatype = []
    fieldlength = []
    fieldmaxlength = []
    fieldminlength =[]
    fieldlengthtype = []
    fieldtype = []
    fields = fromdb['Payload']['Data']['Response']
    for i in fields:
        de.append(i['de'])
        name.append(i['field_name'])
        description.append(i['field_description'])
        datatype.append(i['data_type'])
        fieldlength.append(i['field_length'])
        fieldmaxlength.append(i['field_max_length'])
        fieldminlength.append(i['field_min_length'])
        fieldlengthtype.append(i['field_type_length'])
        fieldtype.append(i['field_type'])

    df = pd.DataFrame(list(zip(de,name,description,datatype,fieldlength,fieldmaxlength,fieldminlength,fieldlengthtype,fieldtype)),columns =['de','name','description','datatype','Field_length', 'Field_max_length', 'Field_min_length','Field_length_type','Field_type'])
    return df
