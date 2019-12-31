# zato: ide-deploy=True
# -*- coding: utf-8 -*-

# stdlib
from datetime import datetime
import json
from zato.server.service import Service
from lxml import etree
from anyjson import dumps


class LotteryService(Service):

  class SimpleIO:
    output_required = ('today', 'description')

  def handle(self):
    lotteryService = self.outgoing.plain_http.get('Lottery') 
    response = lotteryService.conn.post(self.cid)
    root = etree.XML(response.text.encode('utf-8')) #.decode('utf-8').encode('ascii')
    find_text = etree.XPath("//text()")
    text = find_text(root)
    
    payload = {}
    payload['today'] = text[17]
    payload['description'] = text[19]

    self.response.payload = dumps(payload)