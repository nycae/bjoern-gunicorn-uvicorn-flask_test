import asyncio
from aioflask import Flask

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/')
async def index():
    return ('', 204)