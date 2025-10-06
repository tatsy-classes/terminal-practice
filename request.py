import json
import urllib
import urllib.request


def main():
    """
    LibreTranslate APIを使って翻訳を行うサンプル
    """

    url = 'http://localhost:5000/translate'

    headers = {'Content-Type': 'application/json'}
    data = {'q': "Je m'appelle Pierre", 'source': 'fr', 'target': 'ja'}
    bytes = json.dumps(data).encode('utf-8')

    request = urllib.request.Request(url, bytes, headers=headers, method='POST')
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')

    print(json.loads(body))


if __name__ == '__main__':
    main()