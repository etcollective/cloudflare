import pulumi
import pulumi_cloudflare as cf

# Setup Account
account = cf.Account(
    'cloudflare-account',
    name='Explorers Theatre Collective',
    enforce_twofactor=False,  # TO-DO Enforce
    type='standard',
)

# Outputs
pulumi.export('accountId', account.id)
