# list all membership objects for certificate groups and the certificates that belong to them
res = client.get_certificates_certificate_groups()
print(res)
if type(res) == pypureclient.responses.ValidResponse:
    print(list(res.items))
# list the membership objects to see what certificates are contained within groups
# 'all-trusted-certs' and 'all-ad-certs' belong to, if any
res = client.get_certificates_certificate_groups(certificate_group_names=['all-trusted-certs',
                                                                          'all-ad-certs'])
print(res)
if type(res) == pypureclient.responses.ValidResponse:
    print(list(res.items))
# Other valid fields: continuation_token, certificate_ids, certificate_group_ids, filter,
#                     limit, offset, sort
# See section "Common Fields" for examples
