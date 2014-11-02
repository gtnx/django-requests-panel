import requests
import functools

get = requests.get
@functools.wraps(get)
def _get(*args, **kwargs):
  print(args)
  print(kwargs)
  return get(*args, **kwargs)

requests.get = _get

requests.get("http://www.twenga.fr")