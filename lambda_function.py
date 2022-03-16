import json 
import requests


def lambda_handler(event, context):
    
    ipAddr =  event['requestContext']['identity']['userAgent']
    #ipAddr = '34.200.210.86' 
    req = 'http://worldtimeapi.org/api/ip/' + ipAddr + '.json' 
    res = requests.get(req)
    body = res.json()
    body['version'] = "v6"
    
     # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }
