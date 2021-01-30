import requests
def is_connected():
    """Check computer to ping internet gateway"""

    try:
        response = requests.get('https://aws.amazon.com')
        if response.status_code == 200:
            return True
        return False
    except requests.ConnectionError:
        print("Error: connection can't be established with AWS")
