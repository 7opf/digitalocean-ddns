# DigitalOcean DDNS script


Fetches the externally visible IP address of a server behind NAT and updates the A record for the given domain using DigitalOcean's API (v2).

Make sure to set environment variables and run with python 3

```bash
export DO_API_TOKEN=<token>
export DOMAIN=sub.domain.tld
export IP_SERVICES=https://api.ipify.org,https://ident.me
python3 do-ddns
```

IP_SERVICES accepts a comma-separated list of URLs that return the IP in plain text 