from flaskr.app import create_app

app = create_app()
app.run(port=5001, debug=True)