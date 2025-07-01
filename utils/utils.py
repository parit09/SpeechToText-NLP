import base64

def decodeSound(base64_str, fileName):
    with open(fileName, 'wb') as f:
        f.write(base64.b64decode(base64_str))
