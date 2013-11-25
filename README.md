# Python Cian

Python Cian is a library that provides e-mail notifications about new rental flats from search engine of www.cian.ru.

## Using
```
>>> from pycian import Cian
>>> cian = Cian(email="my@email.com", save_to="/tmp/cian-flats.json")
>>> cian.check(url=http://www.cian.ru/cat.php?deal_type=1&obl_id=1&metro[0]=31&type=4&room1=1&totime=86400)
```
