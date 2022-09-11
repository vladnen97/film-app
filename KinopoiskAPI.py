import requests, json


class KinopoiskAPI():
    token = 'AASCEJF-0Z1MXPZ-HQ3M8S0-9F3252J'
    description = 'Empty'
    image = ''
    def __init__(self, name, year):
        name=name.replace(' ', '+')

        response=requests.get(f'https://api.kinopoisk.dev/movie?token={self.token}&field=year&search={year}&field=name&search={name}&isStrict=false')

        if response.status_code==200:
            response_data =json.loads(response.text)
            self.description = response_data['docs'][0]['description']
            self.image = requests.get(response_data['docs'][0]['poster']['url']).content
        else:
            print ('We have a problem:', response.status_code)

    def get_description(self):
        return self.description

    def get_image(self):
        return self.image
        


##api= KinopoiskAPI('Фантастические твари: Тайны Дамблдора', 2022)



