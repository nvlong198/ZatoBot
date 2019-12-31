# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from zato.server.service.adapter import JSONAdapter

class Chatbot(JSONAdapter):
    """ Updates a customer's billing information.
    """
    outconn = 'Chatbot'
    method = 'POST'
