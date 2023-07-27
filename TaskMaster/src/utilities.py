```python
import textwrap

utility_settings = {
    'auto_splitter': False,
    'auto_summarize': False,
    'custom_conversation_width': 80,
    'smart_replace': False
}

def auto_splitter(text, width=80):
    if utility_settings['auto_splitter']:
        return textwrap.fill(text, width)
    else:
        return text

def auto_summarize(text, summary_length=100):
    if utility_settings['auto_summarize']:
        return text[:summary_length] + '...' if len(text) > summary_length else text
    else:
        return text

def set_conversation_width(width):
    utility_settings['custom_conversation_width'] = width

def smart_replace(text, replace_dict):
    if utility_settings['smart_replace']:
        for key, value in replace_dict.items():
            text = text.replace(key, value)
    return text

def update_utility_settings(setting, value):
    if setting in utility_settings:
        utility_settings[setting] = value
    else:
        raise ValueError(f"Invalid setting: {setting}")
```