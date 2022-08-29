import growattServer
import yaml


class GrowattConnect():

    def __init__(self,username,password,plant_id) -> None:
        self.username_ = username
        self.password_ = password
        self.plant_id_ = plant_id

    def api_client(self):
        api = growattServer.GrowattApi()
        api.login(self.username_,self.password_)
        return api

    def get_percentage(self):
        api = self.api_client()
        battery_percentage = str(api.device_list(self.plant_id_)[0]['capacity'])
        return battery_percentage


if __name__ == "__main__":

    with open('config.yaml', 'r') as yml:
        config = yaml.safe_load(yml)

    instance = GrowattConnect(config['growatt']['username'], config['growatt']['password'],config['growatt']['plant_id'])

    # api = instance.api_client()
    # print(instance.get_percentage())
    print(int(instance.get_percentage().replace('%','')))