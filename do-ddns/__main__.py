import os
import requests


class IPServiceException(Exception):
    pass


class DOException(Exception):
    pass


class DigitalOceanDDNS:

    def __init__(self, domain, token, ip_services):
        self.token = token
        self.domain = domain
        self.ip_services = ip_services.split(',')

    def update_ip(self):
        # determine external IPc
        ip = None
        for ip_service in self.ip_services:
            try:
                res = requests.get(ip_service)
                ip = res.text
            except requests.exceptions.BaseHTTPError as e:
                print(e)
                continue

        if ip is None:
            raise IPServiceException

        # query DO API for current A record for the domain
        [name, host, tld] = self.domain.split('.')
        url = 'https://api.digitalocean.com/v2/domains/' + host + '.' + tld + '/records'
        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        records = requests.get(url, headers=headers).json()
        a_records = [record for record in records['domain_records'] if record['type'] == 'A' and record['name'] == name]

        if len(a_records) != 1:
            raise DOException

        a_record = a_records[0]

        # if they match, return
        if a_record['data'] == ip:
            return

        # if they don't match, update the record on DO
        a_record['data'] = ip
        requests.put(url + '/' + str(a_record['id']), a_record, headers=headers).json()

        print('IP address updated to ' + ip + ' on DigitalOcean')


if __name__ == '__main__':
    d = os.environ.get('DOMAIN')
    assert d is not None
    t = os.environ.get('DO_API_TOKEN')
    assert t is not None
    ips = os.environ.get('IP_SERVICES')
    assert ips is not None

    do_ddns = DigitalOceanDDNS(d, t, ips)
    do_ddns.update_ip()
