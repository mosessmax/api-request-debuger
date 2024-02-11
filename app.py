import requests
import sys

class RequestLogger:
    def __init__(self, api_key=None):
        self.log = []
        self.headers = {}
        if api_key:
            self.headers['Authorization'] = f'Bearer {api_key}'


# try except block to handle the case where the response is not JSON
    def request(self, method, url, **kwargs):
        response = requests.request(method, url, headers=self.headers, **kwargs)
        try:
            response_json = response.json() if response.text else None
        except ValueError:
            response_json = None
            self.log.append({'method': method, 'url': url, 'request': kwargs, 'response': response_json})
        return response
        
    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)
    
    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)
    
    # def request(self, method, url, **kwargs):
    #     response = requests.request(method, url, **kwargs)
    #     self.log.append({'method': method, 'url': url, 'request': kwargs, 'response': response.json()})
    #     return response

    # def get(self, url, **kwargs):
    #     return self.request('GET', url, **kwargs)

    # def post(self, url, **kwargs):
    #     return self.request('POST', url, **kwargs)

if __name__ == "__main__":
    if len(sys.argv) != 2:
         print("Error: Please provide a URL right after you type python app.py please..")
         sys.exit(1)
    
    url = sys.argv[1]

    # prompt for api key or token 
    api_key = input("Please enter your API key or token (press Enter to skip if the API doesn't have one): ").strip()

    logger = RequestLogger(api_key=api_key or None)
    print("preparing to boldly go where no Python script has gone before...")  #inserts dramatic music
    logger = RequestLogger()
    response = logger.get(url)
    print("mission accomplished! Here's the log:")  #mission accomplished.
    print(logger.log)
