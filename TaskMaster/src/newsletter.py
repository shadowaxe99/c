```python
import datetime

class Newsletter:
    def __init__(self):
        self.newsletter_archive = []

    def create_newsletter(self, content):
        newsletter = {
            'date': datetime.datetime.now(),
            'content': content
        }
        self.newsletter_archive.append(newsletter)

    def get_newsletter(self, date):
        for newsletter in self.newsletter_archive:
            if newsletter['date'] == date:
                return newsletter
        return None

    def get_all_newsletters(self):
        return self.newsletter_archive

    def update_newsletter(self, date, new_content):
        for newsletter in self.newsletter_archive:
            if newsletter['date'] == date:
                newsletter['content'] = new_content
                return True
        return False

    def delete_newsletter(self, date):
        for newsletter in self.newsletter_archive:
            if newsletter['date'] == date:
                self.newsletter_archive.remove(newsletter)
                return True
        return False
```