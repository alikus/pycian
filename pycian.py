import json
import smtplib

from pyquery import PyQuery


class Cian:
    _send_to = None
    _save_to = None
    _flats = {}
    _new_flats = {}
    _url = None
    _pq = None

    def __init__(self, email, save_to="/tmp/flats.json", *args, **kwargs):
        self._send_to = email
        self._save_to = save_to
        try:
            f = open(self._save_to, 'r+')
        except IOError:
            pass
        else:
            self._flats = json.loads(f.read())

    def check(self, url):
        """Loads data form search url and notify about new flats form cian"""
        self._url = url
        self._pq = PyQuery(url=url)
        self._pq('tr[id^=tr_]').each(self._handle_node)
        self._save()
        self._send_mail()

    def _handle_node(self, index, node):
        d = self._pq(node)
        fid = d.attr('id').replace('tr_', '')
        address = d.find('td[id$=_metro]').text()
        url = "http://www.cian.ru/rent/flat/%s" % fid
        if fid not in self._flats:
            self._flats[fid] = self._new_flats[fid] = {'address': address, 'url': url}

    def _save(self):
        f = open(self._save_to, 'w')
        f.write(json.dumps(self._flats))
        f.close()

    def _send_mail(self):
        if not self._new_flats:
            return

        sender = 'noreply@localhost'
        message = "From: Cian Reminder <%(sender)s>\n"\
            "To: %(email)s\n" \
            "Subject: New flats from cian\n\n" % {'sender': sender, 'email': self._send_to}
        message += "New flats:\n"
        for fid in self._new_flats:
            message += u"%(address)s: %(url)s\n" % self._new_flats[fid]
        message += "\n\nView all flats: %s" % self._url

        try:
            smtp = smtplib.SMTP('localhost')
            smtp.sendmail(sender, self._send_to, message.encode('utf-8'))
        except smtplib.SMTPException as e:
            print "Error: unable to send email: %s" % e

if __name__ == "__main__":
    cian = Cian(email='my@email.com')
    cian.check('http://www.cian.ru/cat.php?deal_type=1&obl_id=1&metro[0]=31&type=4&room1=1&totime=86400')

