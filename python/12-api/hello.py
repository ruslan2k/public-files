import connexion

def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='swagger/')
    app.add_api('my_api.yaml', arguments={'title': 'Hello World Example'})
    app.run(port=5000)

