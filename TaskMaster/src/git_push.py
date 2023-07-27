```python
import os
import subprocess

def git_push():
    try:
        subprocess.check_call(['git', 'add', '.'])
        message = "Automated commit by TaskMaster"
        subprocess.check_call(['git', 'commit', '-m', message])
        subprocess.check_call(['git', 'push'])
        print("Code changes pushed to git successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to push code changes to git. Error: ", str(e))

if __name__ == "__main__":
    git_push()
```