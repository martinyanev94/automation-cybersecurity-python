def check_compliance(security_groups):
    compliance_issues = []
    for group in security_groups:
        for permission in group['IpPermissions']:
            if permission['IpProtocol'] == '-1':  # If protocol is all
                compliance_issues.append(group['GroupId'])
    return compliance_issues

# After calling list_security_groups, we would check compliance.
groups = list_security_groups()
issues = check_compliance(groups)

if issues:
    print("Compliance Issues Found:", issues)
else:
    print("All groups are compliant!")
