```python
import sqlite3
from sqlite3 import Error

class AIWallet:
    def __init__(self):
        self.ai_wallet = []
        self.database = r"TaskMaster/src/database.sqlite"

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.database)
        except Error as e:
            print(e)
        return conn

    def select_all_agents(self):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM ai_agents")
            rows = cur.fetchall()
            for row in rows:
                self.ai_wallet.append(row)

    def add_agent(self, agent):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO ai_agents VALUES(?, ?, ?)", agent)
            conn.commit()
            self.ai_wallet.append(agent)

    def remove_agent(self, agent_id):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM ai_agents WHERE id=?", (agent_id,))
            conn.commit()
            self.ai_wallet = [agent for agent in self.ai_wallet if agent[0] != agent_id]

    def update_agent(self, agent):
        conn = self.create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("UPDATE ai_agents SET name=?, task=? WHERE id=?", agent)
            conn.commit()
            for i, a in enumerate(self.ai_wallet):
                if a[0] == agent[0]:
                    self.ai_wallet[i] = agent

    def get_wallet(self):
        return self.ai_wallet
```