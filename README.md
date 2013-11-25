# PyCian

PyCian is a library that provides e-mail notifications about new rental flats from search engine of www.cian.ru.

## Using
Paste below code in script and add to crontab to get notifications.
```
>>> from pycian import Cian
>>> cian = Cian(email="my@email.com", save_to="/tmp/cian-flats.json")
>>> cian.check(url="http://www.cian.ru/cat.php?metro[0]=31&minprice=20000&room1=1")
```
