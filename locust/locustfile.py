import pandas as pd
from locust import HttpUser, task, between


HOST = "http://3.1.201.237:8000"
MIN_WAIT = 0.5
MAX_WAIT = 10

PROXIES = {
  'http': 'http://101.132.143.232:80',
  'http': 'http://221.180.170.104:8080'
}

# data_list = pd.read_csv("./sitemap.csv")
# print(data_list['suburl'].values)

class User1(HttpUser):
   host = HOST
   wait_time = between(MIN_WAIT, MAX_WAIT)

   @task
   def index(self):
       self.client.get("/")


class User2(HttpUser):
    '''
        Single instance of user class with predefined Tasks.
        
        Param:
            Httpuser - Send HTTP request to targeted server.
    '''

    host = HOST
    wait_time = between(MIN_WAIT, MAX_WAIT)

    @task
    def index(self):
        self.client.get("/")
        # self.client.get("/category/new-arrivals-163")
        # self.client.get("/product/platinum-jacket-216809-2544")


    # @task
    # def index(self):
    #     with self.client.get("/", proxies=PROXIES) as response:
    #         if response.status_code == 200:
    #             print("Success")

    
