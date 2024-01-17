import pulumi
import pulumi_cloudflare as cloudflare

from account.account import account

# Account Members
admin_emails = ['christian@cdiaz.cloud']
superadmin_role = '33666b9c79b9a5273fc7344ff42f953d'

for admin in admin_emails:
    admin = cloudflare.AccountMember(
        f'admin-{admin}',
        account_id=account.id,
        email_address=admin,
        role_ids=[superadmin_role],
        opts=pulumi.ResourceOptions(parent=account),
    )
