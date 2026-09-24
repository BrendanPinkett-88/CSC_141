# new names

current_users = ["Dreaded-Ghost", "Brenpink2008", "The_Ghost", "S1ash3r_1946", "Dino Nugget"]

new_users = ["Marty-O", "Loui-G", "SonicDHedge", "Pikachew", "Amongoose"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} will need to enter a new username.")
    else:
        print(f"{new_user} is available.")