import csv
import json

# Define the function to transform the dataset
def transform_csv_to_json(csv_file, json_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        transformed_data = []

        for row in reader:
            document = {
                "DR_NO": row["DR_NO"],
                "DateReported": row["Date Rptd"],
                "DateOccurred": row["DATE OCC"],
                "TimeOccurred": row["TIME OCC"],
                "Area": {
                    "Code": row["AREA"],
                    "Name": row["AREA NAME"]
                },
                "ReportDistrict": row["Rpt Dist No"],
                "Part": row["Part 1-2"],
                "CrimeCode": {
                    "Primary": row["Crm Cd"],
                    "Description": row["Crm Cd Desc"],
                    "AdditionalCodes": [
                        row["Crm Cd 1"],
                        row["Crm Cd 2"],
                        row["Crm Cd 3"],
                        row["Crm Cd 4"]
                    ]
                },
                "MOCodes": row["Mocodes"],
                "Victim": {
                    "Age": row["Vict Age"],
                    "Sex": row["Vict Sex"],
                    "Descent": row["Vict Descent"]
                },
                "Premises": {
                    "Code": row["Premis Cd"],
                    "Description": row["Premis Desc"]
                },
                "Weapon": {
                    "Code": row["Weapon Used Cd"],
                    "Description": row["Weapon Desc"]
                },
                "Status": {
                    "Code": row["Status"],
                    "Description": row["Status Desc"]
                },
                "Location": {
                    "Address": row["LOCATION"],
                    "CrossStreet": row["Cross Street"],
                    "Coordinates": {
                        "Latitude": float(row["LAT"]) if row["LAT"] else None,
                        "Longitude": float(row["LON"]) if row["LON"] else None
                    }
                }
            }

            # Remove empty additional crime codes
            document["CrimeCode"]["AdditionalCodes"] = [
                code for code in document["CrimeCode"]["AdditionalCodes"] if code
            ]

            transformed_data.append(document)

    # Write to JSON file
    with open(json_file, mode='w') as file:
        json.dump(transformed_data, file, indent=4)

# Replace with your file paths
csv_file_path = "mongodb/dataset/Crime_Data_from_2020_to_Present.csv"
json_file_path = "mongodb/dataset/Crime_Data.json"

transform_csv_to_json(csv_file_path, json_file_path)

print(f"Data has been transformed and saved to {json_file_path}.")