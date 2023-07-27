import os
import json
import time
from datetime import datetime

# Importing shared dependencies
from task_management import task_list
from ai_agent_management import ai_agents

sync_status = {}

def autoSync():
    while True:
        time.sleep(60)  # Sync every minute
        sync_status['last_sync'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        syncTasks()
        syncAgents()

def syncTasks():
    with open('TaskMaster/src/task_data.json', 'w') as file:
        json.dump(task_list, file)

def syncAgents():
    with open('TaskMaster/src/ai_agent_data.json', 'w') as file:
        json.dump(ai_agents, file)

if __name__ == "__main__":
    autoSync()