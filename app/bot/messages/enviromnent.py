from jinja2 import Environment

environment = Environment(enable_async=True, trim_blocks=True, autoescape=True)

environment.globals.update(enumerate=enumerate)
