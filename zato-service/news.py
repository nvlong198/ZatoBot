# stdlib
import json
from zato.server.service import Service
import re
import random
from anyjson import dumps


class NewsService(Service):

  class SimpleIO:
    output_required = ('topic', 'href', 'newspaper', 'update_time')

  def handle(self):
    headers = {'Content-Type': 'application/json', 'Range': 'bytes=0-15000'}
    newsService = self.outgoing.plain_http.get('News') # theodoibaochi
    response = newsService.conn.post(self.cid, headers=headers)
    # self.logger.info(response.text)
    response = re.sub(', ({"stt": "11").+', ']}', response.text)
    response = json.loads(response)
    response = response["article_list"][random.randint(0,9)]
    
    payload = {}
    for e in ['topic', 'href', 'newspaper', 'update_time']:
        payload[e] = response[e]

    self.response.payload = dumps(payload)