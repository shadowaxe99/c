```python
class LanguageStyleSelection:
    def __init__(self):
        self.language_style = {
            'language': 'English',
            'style': 'Light'
        }

    def get_language_style(self):
        return self.language_style

    def set_language_style(self, language, style):
        self.language_style['language'] = language
        self.language_style['style'] = style

    def select_language_style(self, language, style):
        self.set_language_style(language, style)
        self.update_language_style()

    def update_language_style(self):
        message = LanguageStyleUpdate(self.get_language_style())
        message.send()

class LanguageStyleUpdate:
    def __init__(self, language_style):
        self.language_style = language_style

    def send(self):
        # Code to send the update message to the frontend
        pass
```