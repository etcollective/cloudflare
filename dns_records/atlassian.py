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


dkim_values = [
    {
        'name': 'atlassian-042b54._domainkey.etcollective.org',
        'value': 'atlassian-042b54.dkim.atlassian.net',
    },
    {
        'name': 'atlassian-36dbe2._domainkey.etcollective.org',
        'value': 'atlassian-36dbe2.dkim.atlassian.net',
    },
    {
        'name': 'atlassian-bounces.etcollective.org',
        'value': 'bounces.mail-us.atlassian.net',
    },
]

for dkim in dkim_values:
    cf.Record(
        f'atlassian-dkim-dns-record-{dkim["name"]}',
        name=dkim['name'],
        ttl=86400,
        type='CNAME',
        value=dkim['value'],
        proxied=False,
        zone_id=zone.id,
    )

txt_mail = cf.Record(
    'atlassian-mail-txt-record',
    name='@',
    value='atlassian-sending-domain-verification=1ab91f15-080c-40b2-b4b9-503cd2d0e70b',
    type='TXT',
    proxied=False,
    zone_id=zone.id,
)
