import requests


def get_api():
    response = requests.get(
        'https://beta-app.vegacdn.com/api/cdn_resource/list?page=1&page_size=10000',
        headers={'X-AUTH-TOKEN': 'u-vcdnsecret-@@2019##'},
    )
    json_response = response.json()['data']
    id_live_conf = []
    id_live_vcl = []
    id_vod = []

    for i in json_response:
        if i['status'] in [1, 10] and i['resource_type_id'] == 1 and not i['advance_setting'] is None and i['advance_setting']['protocol'] == 'HTTP,SSL':
            id_live_conf.append(str(i['id']))
            id_live_vcl.append(str(i['id']))
        if i['status'] in [1, 10] and i['resource_type_id'] == 1 and i['advance_setting'] is not None and i['advance_setting']['protocol'] == 'HTTP':
            id_live_vcl.append(str(i['id']))
        if i['status'] in [1, 10] and i['resource_type_id'] in [2,3]:
            id_vod.append(str(i['id']))
    return id_vod,id_live_conf, id_live_vcl

print (get_api())

