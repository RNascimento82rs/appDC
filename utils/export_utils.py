import csv
import json

def export_municipios_csv(municipios, path='municipios.csv'):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Nome', 'Latitude', 'Longitude'])
        for m in municipios:
            writer.writerow([m.id, m.nome, m.latitude, m.longitude])
    return path

def export_municipios_json(municipios, path='municipios.json'):
    data = [{'id': m.id, 'nome': m.nome, 'latitude': m.latitude, 'longitude': m.longitude} for m in municipios]
    with open(path, 'w') as jsonfile:
        json.dump(data, jsonfile)
    return path
