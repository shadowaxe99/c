```python
import re

def searchHighlight(search_query, task_list, ai_agents):
    # Initialize empty lists for search results
    task_results = []
    agent_results = []

    # Compile the search query into a regular expression object
    search_pattern = re.compile(search_query, re.IGNORECASE)

    # Search through tasks
    for task in task_list:
        if search_pattern.search(task['name']) or search_pattern.search(task['description']):
            task_results.append(task)

    # Search through AI agents
    for agent in ai_agents:
        if search_pattern.search(agent['name']) or search_pattern.search(agent['description']):
            agent_results.append(agent)

    # Return search results
    return task_results, agent_results
```