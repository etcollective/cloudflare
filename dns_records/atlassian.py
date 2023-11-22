import pulumi
import pulumi_cloudflare as cf
from dns_records import zone


atlassian_verification = cf.Record(
    'atlassian-verification-dns-record',
    name='@',
    ttl=86400,
    type='TXT',
    value='atlassian-domain-verification=7m9QvVogbabf7VhUlQxwDXKslWcSsmXgNYS3Xkrypjwel0YqxVlr5klJUbJHDPrp',
    proxied=False,
    zone_id=zone.id,
)
