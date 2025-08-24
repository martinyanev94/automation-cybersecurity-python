roles_with_read_permission = [role for role, permissions in permissions.items() if "read" in permissions]
print(roles_with_read_permission)
