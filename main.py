# coding=utf-8
import os

from src import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
else:
    os.chdir(os.path.dirname(__file__))
    application = app
