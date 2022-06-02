import base64
import requests
import re
from alive_progress import alive_bar

def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    try:
        return base64.b64decode(data, altchars)
    except base64.binascii.Error:
        print(data)

def download_pdf(arr, dir):
    x = 0
    with alive_bar(len(arr), title="downloading images") as bar:
        for link in arr:
            xstr = str(x)
            content = requests.get(link).content
            decoded_content = decode_base64(content[150:-8])
            with open(f'{dir}/page{xstr}.jpg', 'wb') as f:
                f.write(decoded_content)

            x += 1
            bar()