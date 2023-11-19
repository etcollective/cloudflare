import pulumi
import pulumi_cloudflare as cf
from dns_records import zone_id

# Begin Records
support_verification = cf.Record(
    'gsuite-support-verfication-record',
    zone_id=zone_id,
    name='48090117',
    value='google.com',
    ttl=3600,
    type='CNAME',
)
