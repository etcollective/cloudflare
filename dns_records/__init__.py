import pulumi
import pulumi_cloudflare as cf

# Setup Config
config = pulumi.Config('etcollective.org')
zone_id = config.require('zoneId')
