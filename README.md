# ![](docs/logo.png) LvlUpPy

Python bindings for LvlUp.pro API

[Documentation](https://docs.kazigk.me/lvluppy)

## Getting started

### Obtaining LvlUpPy

```bash
git clone https://github.com/kazigk/LvlUpPy.git
cd LvlUpPy
pip3 install -r requirements.txt
./setup.py install --user
```

### Having fun

```python
from lvluppy import UpClient
from lvluppy.exceptions import UnauthorizedException

up = UpClient('your_precious_token')

try:
  info = up.getUserInfo()
  print('Successfully logged in as', info.email)
except UnauthorizedException as e:
  print('Cannot fetch user info, please check your token.')
  print('Exception details:', e.details)
```

You can also use sandbox environment provided by LvlUp to test your scripts, create UpClient instance specifying baseUrl parameter:

```python
SANDBOX_URL = 'https://sandbox-api.lvlup.pro/v4'

up = UpClient('your_precious_token', baseUrl=SANDBOX_URL)
```
