import requests
import xmltodict

auth_details = ('Ykorringa@gmail.com','c10VkbLmTdPTBFPUFGgYRc96RI5oApOxFifwsMJX0llcbLA-7drwEg')
api_url_1 = 'http://webservices.ns.nl/ns-api-avt?station=ut'
api_url_2 = 'http://webservices.ns.nl/ns-api-avt?station=shl'

res = requests.get(api_url_1, auth=auth_details)
res2 = requests.get(api_url_2, auth=auth_details)

with open('v_tijden.xml','w') as vt_xmlFile:
    vt_xmlFile.write(res.text)
    vt_xmlFile.write(res2.text)


vtXml2 = xmltodict.parse(res.text)

for v in vtXml2 ['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = v['EindBestemming']

    vtijd = v['VertrekTijd']
    vtijd = vtijd[11:16]

    print('{} - {}'.format(eindbestemming,vtijd))