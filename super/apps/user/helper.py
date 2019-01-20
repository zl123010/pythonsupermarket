from super.settings import SECRET_KEY
import hashlib


def set_password(password):
    for _ in range(255):
        pwd_str = "{}{}".format(password, SECRET_KEY)
        h = hashlib.md5(pwd_str.encode('utf-8'))
        password = h.hexdigest()
    return password
