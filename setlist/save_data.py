import json
def save_to_json(path, data):
    '''
    Wrapper to save data to json
    inputs:
        path - exactly what it sounds like
        data - json data to save
    '''
    js = json.dumps(data)
    fp = open(path, 'a')
    fp.write(js)
    fp.close()

def open_file(path):
    '''
    Wrapper to open data to json
    inputs:
        path - exactly what it sounds like - leads to json file
    ''' 
    json1_file = open(path)
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)
    return json1_data