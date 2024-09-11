import sqlite3

class JobStorage:
    def __init__(self, db_path="job_storage.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_link TEXT UNIQUE
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def has_seen(self, job_link):
        query = "SELECT 1 FROM jobs WHERE job_link = ?"
        cursor = self.conn.execute(query, (job_link,))
        return cursor.fetchone() is not None

    def save_job(self, job_link):
        query = "INSERT INTO jobs (job_link) VALUES (?)"
        self.conn.execute(query, (job_link,))
        self.conn.commit()
