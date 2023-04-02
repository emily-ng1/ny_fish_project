from api import create_app
from settings import DB_NAME, DB_USER, DB_PASSWORD

app=create_app(DB_NAME, DB_USER, DB_PASSWORD)
app.run(debug=True)


