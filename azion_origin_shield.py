#!/usr/bin/python3
import ast
import requests
import os

#https://api.azion.com/#06c5bf91-1ba8-418a-b463-78ad83762601
URL_REQ_TOKEN = "https://api.azionapi.net/tokens"
HEADERS_REQ_TOKEN = {
    'Accept': 'application/json; version=3',
    'Authorization': 'Basic dXNlckBkb21haW46cGFzc3dvcmQK' #CHANGE AZION CREDENTIALS USING URLENCODE
}
PAYLOAD = {}

RESPONSE_REQ_TOKEN = requests.request("POST", URL_REQ_TOKEN, headers=HEADERS_REQ_TOKEN, data=PAYLOAD)

OUTPUT_REQ_TOKEN = RESPONSE_REQ_TOKEN.text
OUTPUT_TOKEN = ast.literal_eval(OUTPUT_REQ_TOKEN).get('token')

#HERE WE`LL GET AZION ORIGIN SHIELD LIST TO ALLOW FROM THIS CDN SOURCE ADDRESSES ONLY
URL_REQ_AZION_ORIGIN_SHIELD = "https://api.azionapi.net/network_lists/187" #https://www.azion.com/pt-br/blog/post/origin-shield-disponivel-rtm-api
HEADERS_AZION_ORIGIN_SHIELD = {
    'Accept': 'application/json; version=3',
    'Authorization': 'Token ' + OUTPUT_TOKEN,
    'Content-Type': 'application/json'
}

RESPONSE_AZION_ORIGIN_SHIELD = requests.request("GET", URL_REQ_AZION_ORIGIN_SHIELD, headers=HEADERS_AZION_ORIGIN_SHIELD,
                                                data=PAYLOAD)

OUTPUT_AZION_ORIGIN_SHIELD = RESPONSE_AZION_ORIGIN_SHIELD.text
OUTPUT_IPS = ast.literal_eval(OUTPUT_AZION_ORIGIN_SHIELD).get('results').get('items_values')


with open(r'/root/ext_dg_azion_origin_shield.txt', 'w') as file:
    for item in OUTPUT_IPS:
        file.write("network " + "%s,\n" % item)

UPDATE_DG_FILE = os.popen("tmsh modify sys file data-group ext_dg_azion_origin_shield source-path file:/root/ext_dg_azion_origin_shield.txt")
