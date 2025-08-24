def update_threat_database(ioc_value, status):
    # This function would update the central threat database
    if status == "mitigated":
        print(f"Updating IOC {ioc_value} to 'Mitigated' in the database.")
    elif status == "confirmed threat":
        print(f"Updating IOC {ioc_value} to 'Confirmed Threat' in the database.")
    else:
        print(f"Status '{status}' for IOC {ioc_value} is unrecognized.")
