import time

# Check scan status
while True:
    scan_status = session.get(f"{api_url}/scans/{scan_id}", headers=headers).json()["info"]["status"]
    if scan_status == "completed":
        print("Scan completed. Downloading report...")
        
        # Export and download the report
        export_payload = {"format": "csv"}
        export_response = session.post(f"{api_url}/scans/{scan_id}/export", headers=headers, json=export_payload)
        
        file_id = export_response.json()["file"]
        download_response = session.get(f"{api_url}/scans/{scan_id}/export/{file_id}/download", headers=headers)
        
        with open("scan_report.csv", "wb") as file:
            file.write(download_response.content)
        print("Report downloaded successfully.")
        break
    else:
        print(f"Scan in progress: {scan_status}")
    time.sleep(10)
