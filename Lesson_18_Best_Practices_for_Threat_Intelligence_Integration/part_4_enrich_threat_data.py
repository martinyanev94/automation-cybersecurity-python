def enrich_threat_data(threat_data):
    enriched_data = []
    for item in threat_data:
        ioc = IndicatorOfCompromise(item['type'], item['value'], item['description'], item['source'])
        # Here you'd implement your logic to determine the risk level
        if "high" in item['description'].lower():
            risk_level = "High"
        elif "medium" in item['description'].lower():
            risk_level = "Medium"
        else:
            risk_level = "Low"
        enriched_data.append({'ioc': ioc, 'risk_level': risk_level})
    return enriched_data
