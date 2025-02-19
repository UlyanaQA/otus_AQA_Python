import requests

class DogApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get_list_all_breeds(self):
        return self.session.get(url=f'{self.base_url}/breeds/list/all')

    def get_single_random_image(self):
        return self.session.get(url=f'{self.base_url}/breeds/image/random')

    def get_multiple_random_images(self, number_of_dogs):
        return self.session.get(url=f'{self.base_url}/breeds/image/random/{number_of_dogs}')

    def get_random_image_from_collection(self, breed):
        return self.session.get(url=f'{self.base_url}/breed/{breed}/images/random')

    def get_list_all_sub_breeds(self, breed='hound'):
        return self.session.get(url=f'{self.base_url}/breed/{breed}/list')