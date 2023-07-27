import json
import os

def export_data(task_list, ai_agents, ai_wallet):
    data = {
        'task_list': task_list,
        'ai_agents': ai_agents,
        'ai_wallet': ai_wallet
    }

    with open('export_data.json', 'w') as outfile:
        json.dump(data, outfile)

    print("Data exported successfully to export_data.json")

def load_exported_data():
    if os.path.exists('export_data.json'):
        with open('export_data.json') as json_file:
            data = json.load(json_file)
            return data
    else:
        print("No exported data found.")
        return None

def update_data_from_export(export_data):
    if export_data:
        task_list = export_data['task_list']
        ai_agents = export_data['ai_agents']
        ai_wallet = export_data['ai_wallet']
        print("Data updated from export.")
    else:
        print("No data to update from.")