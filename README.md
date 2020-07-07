# DigitalOcean DDNS script


Fetches the externally visible IP address of a server behind NAT and updates the A record for the given domain using DigitalOcean's API (v2).

Install, in the project dir
```bash
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install requirements.txt
```

Make sure to set environment variables and run with python 3

```bash
. venv/bin/activate
export DO_API_TOKEN=<token>
export DOMAIN=sub.domain.tld
export IP_SERVICES=https://api.ipify.org,https://ident.me
python3 do-ddns
```

IP_SERVICES accepts a comma-separated list of URLs that return the IP in plain text 