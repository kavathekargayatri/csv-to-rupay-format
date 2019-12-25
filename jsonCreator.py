


def jsonFormatConversion(id,value,name,shortname,description,subelements):
    data = {
        'id' : id,
        'value' : value,
        'name': name,
        'shortname': shortname,
        'description': description,
        'subelements': subelements,
    }
    return data