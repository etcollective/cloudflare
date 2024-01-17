import pulumi
import pulumi_cloudflare as cloudflare
from dns_records import zone

# Setup Staging
staging = cloudflare.Record(
    'staging-website-record',
    name='staging',
    zone_id=zone.id,
    type='CNAME',
    value='ghs.googlehosted.com',
    ttl=1,
    proxied=True,
)

# Setup Production
ipv4 = '216.239.32.21'
ipv6 = '2001:4860:4802:32::15'

prod_ipv4_root = cloudflare.Record(
    'root-ipv4-website-record',
    name='@',
    zone_id=zone.id,
    type='A',
    value=ipv4,
    ttl=1,
    proxied=True,
    comment='Managed by Pulumi',
)
prod_ipv6_root = cloudflare.Record(
    'root-ipv6-website-record',
    name='@',
    zone_id=zone.id,
    type='AAAA',
    value=ipv6,
    ttl=1,
    proxied=True,
    comment='Managed by Pulumi',
)

prod_ipv4_www = cloudflare.Record(
    'www-ipv4-website-record',
    name='www',
    zone_id=zone.id,
    type='A',
    value=ipv4,
    ttl=1,
    proxied=True,
    comment='Managed by Pulumi',
)
prod_ipv6_www = cloudflare.Record(
    'www-ipv6-website-record',
    name='www',
    zone_id=zone.id,
    type='AAAA',
    value=ipv6,
    ttl=1,
    proxied=True,
    comment='Managed by Pulumi',
)