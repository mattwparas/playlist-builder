import json
def save_to_json(path, data):
    '''
    Wrapper to save data to json
    Args:
        path (string): exactly what it sounds like
        data (json object): json data to save
    Returns:
        None
    '''
    js = json.dumps(data)
    fp = open(path, 'a')
    fp.write(js)
    fp.close()
    return

def open_file(path):
    '''
    Wrapper to open data to json
    Args:
        path (string): Path to data to open
    Returns:
        The json data
    ''' 
    json1_file = open(path)
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)
    return json1_data