import requests
from requests.auth import HTTPBasicAuth




def test_rabbitmq_http_api(rabbitmq_server, rabbitmq_user='guest', rabbitmq_password='guest', verify_ssl=True):
    """
    Tests connectivity to the RabbitMQ HTTP API.
    """
    api_url = f"{rabbitmq_server.rstrip('/')}/api/overview"  # Basic endpoint to test
    try:
        response = requests.get(api_url, auth=HTTPBasicAuth(rabbitmq_user, rabbitmq_password), verify=verify_ssl)
        
        if response.status_code == 200:
            print("Successfully connected to RabbitMQ HTTP API.")
            print("RabbitMQ Version:", response.json().get("rabbitmq_version"))
        else:
            print(f"Received HTTP {response.status_code}: {response.text}")
    except requests.exceptions.SSLError:
        print("SSL Error: consider setting verify_ssl=False for self-signed certificates.")
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    rabbitmq_user = "setup"
    rabbitmq_password = "stq5vbk5cxw1nk2kowro387ahwnac887akzvdwso"
    rabbitmq_server = "https://mrxlabrabbitmq.mrxlab.com:15671"
    #rabbitmq_server = "10.40.1.14"
    VERIFY_SSL = True  # Set to False if using self-signed certs

    test_rabbitmq_http_api(rabbitmq_server, rabbitmq_user, rabbitmq_password, VERIFY_SSL)
