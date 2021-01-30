def is_connected():
    """Check computer to ping internet gateway"""
    import requests

    try:
        response = requests.get('https://aws.amazon.com')
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        return False
