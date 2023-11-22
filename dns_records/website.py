import pulumi
import pulumi_cloudflare as cf
from dns_records import zone

staging = cf.Record(
    'staging-website-record',
    name='staging',
    zone_id=zone.id,
    type='CNAME',
    value='ghs.googlehosted.com',
    ttl=120,
    proxied=True,
)
