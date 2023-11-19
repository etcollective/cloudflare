import pulumi
import pulumi_cloudflare as cf
from dns_records import zone

# Begin Records
support_verification = cf.Record(
    'gsuite-support-verfication-record',
    zone_id=zone.id,
    name='48090117',
    value='google.com',
    ttl=3600,
    type='CNAME',
    opts=pulumi.ResourceOptions(parent=zone, delete_before_replace=True),
)
