import base64


def code(text):
    return base64.b64encode(text.encode('ascii')).decode('ascii')


assert code('kot') == 'a290'
assert code('Many hands make light work.') == 'TWFueSBoYW5kcyBtYWtlIGxpZ2h0IHdvcmsu'

