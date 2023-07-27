```python
import sqlite3
from sqlite3 import Error

class AgentSchema:
    def __init__(self, agent_id, agent_name, agent_status):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.agent_status = agent_status

class AIAgentManagement:
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)
        self.ai_agents = []

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def manageAgents(self, agent_id, agent_name, agent_status):
        agent = AgentSchema(agent_id, agent_name, agent_status)
        self.ai_agents.append(agent)
        self.updateDatabase(agent)

    def updateDatabase(self, agent):
        try:
            sql = ''' INSERT INTO agents(agent_id,agent_name,agent_status)
                      VALUES(?,?,?) '''
            cur = self.conn.cursor()
            cur.execute(sql, (agent.agent_id, agent.agent_name, agent.agent_status))
            self.conn.commit()
        except Error as e:
            print(e)

    def getAgents(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM agents")
        rows = cur.fetchall()
        for row in rows:
            print(row)

if __name__ == '__main__':
    ai_agent_management = AIAgentManagement("TaskMaster/src/database.sqlite")
    ai_agent_management.manageAgents(1, "Agent1", "Active")
    ai_agent_management.getAgents()
```