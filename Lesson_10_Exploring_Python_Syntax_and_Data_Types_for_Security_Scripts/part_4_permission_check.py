user_role = "editor"

if "delete" in permissions[user_role]:
    print("You have permission to delete.")
else:
    print("Permission denied.")
