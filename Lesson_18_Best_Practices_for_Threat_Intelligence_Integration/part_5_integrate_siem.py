def integrate_with_siem(enriched_data):
    for item in enriched_data:
        # Hypothetical API call to the SIEM system
        siem_response = send_to_siem(item['ioc'].value, item['risk_level'])
        print(f"Integrated IOC {item['ioc'].value} with Risk Level: {item['risk_level']}")
        if siem_response:
            print("Integration successful!")
        else:
            print("Integration failed.")
