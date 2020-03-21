import os

class config(object):
    SECRET_KEY = os.environ.get('316522036') or 'nimrod'

    IMAGE_UPLOADS = "Desktop\projects\DiamondsR4ever"