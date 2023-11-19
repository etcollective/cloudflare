import pulumi
import pulumi_cloudflare as cf

from dns_records import zone

# Setup Config / Vars
config = pulumi.Config('google_workspace')
verification_host = config.require_secret('verification_host')
verification_dest = config.require_secret('verification_dest')

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

workspace_verification = cf.Record(
    'google-workspace-verfication-record',
    zone_id=zone.id,
    name=verification_host,
    type='CNAME',
    value=verification_dest,
    ttl=3600,
    opts=pulumi.ResourceOptions(parent=zone, delete_before_replace=True),
)
