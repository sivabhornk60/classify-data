import requests,json

def create_items(api_key,collection_id,items):
    print(api_key,collection_id)
    url = "https://v2k.vallarismaps.com/core/api/1.0-beta/collections/"+str(collection_id)+"/items?api_key="+str(api_key)   
    payload= str(items).replace("'", '"').replace("None", "null")
    print(payload)
    headers = {
    'Content-Type': 'application/json',              
    }

    response = requests.post(url, headers=headers, data=payload.encode('utf-8'))
    print(response)
    print(response.text)
    if response.status_code == 201 :
    	return True
    else:
    	return False 
    
# outflood = r"D:\6\flooding.geojson"
# with open(outflood) as f:
#     data = json.load(f)

# items = {"type": "FeatureCollection","features": [data['features']]}
# api_key = 'tLjpAaF1CmD04WnmIhwmco28n0fYwzO8T3CiUmyqdQ3h11LCaI6Ll3EJcgsPSs1u'
# collection_id = '605435d2e37bb5b1891fcbeb'
# create_items(api_key,collection_id,items)