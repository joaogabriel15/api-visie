from api_visie import app

app = app.create_app()

app.run(host='0.0.0.0', port=5000)
