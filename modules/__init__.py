# modules/__init__.py

from joppy.api import Api

# Single reusable instance of the Joplin API
joplin = Api(port=41184)
