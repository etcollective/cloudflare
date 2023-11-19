import pulumi
import pulumi_cloudflare as cf

from account.account import account

domain_name = 'etcollective.org'

zone = cf.Zone(
    domain_name,
    account_id=account.id,
    zone=domain_name,
    plan='free',
    paused=False,
    type='full',
)

pulumi.export('zoneId', zone.id)
