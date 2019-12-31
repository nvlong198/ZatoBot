# stdlib
from datetime import datetime
import json
from zato.server.service import Service

class WeatherService(Service):

  class SimpleIO:
    output_required = ('description', 'temp', 'humidity')

  def handle(self):
    newsService = self.outgoing.plain_http.get('Weather') 
    response = newsService.conn.post(self.cid)
    response = json.loads(response.text)

    payload = {}
    payload['description'] = response['weather'][0]['description']
    payload['temp'] = round(response['main']['temp'] - 273)
    payload['humidity'] = response['main']['humidity']
    
    self.response.payload = payload