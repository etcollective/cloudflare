import pulumi
import pulumi_cloudflare as cf

from dns_records import zone

mx_records = [
    {'priority': 1, 'value': 'ASPMX.L.GOOGLE.COM'},
    {'priority': 5, 'value': 'ALT1.ASPMX.L.GOOGLE.COM'},
    {'priority': 5, 'value': 'ALT2.ASPMX.L.GOOGLE.COM'},
    {'priority': 10, 'value': 'ALT3.ASPMX.L.GOOGLE.COM'},
    {'priority': 10, 'value': 'ALT4.ASPMX.L.GOOGLE.COM'},
]

for mx in mx_records:
    value = mx['value']
    cf.Record(
        'google-workspace-mx-record-{}'.format(mx['value']),
        zone_id=zone.id,
        name='@',
        type='MX',
        value=value.lower(),
        priority=mx['priority'],
        ttl=3600,
        opts=pulumi.ResourceOptions(parent=zone, delete_before_replace=True),
    )
