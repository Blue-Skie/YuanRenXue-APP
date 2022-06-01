import requests_pkcs12

def run():
    num = 0
    for page in range(1,101):
        headers = {
            'Host': '180.76.60.244:18443',
            'User-Agent': 'okhttp/3.14.9',
        }
        data = {
          'page': page
        }

        response = requests_pkcs12.post('https://180.76.60.244:18443/api/app5',
                    headers=headers, data=data, pkcs12_filename='5.p12',
                    pkcs12_password='r0ysue', verify=False)
        result = response.json()
        data = result['data']
        for item in data:
            num += int(item['value'])
        print(page,num)

    print(num)

if __name__ == '__main__':
    run()

