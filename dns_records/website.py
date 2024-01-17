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
