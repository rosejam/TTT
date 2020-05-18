# -*- coding: utf-8 -*-

import logging

import pythoncom
import settings
import win32com.client

import settings

__author__ = 'Moon Kwon Kim'

logger = logging.getLogger(__name__)


class XASessionEvents:

    DISCONNECTED = 0
    CONNECTED = 1
    FAILED = 999
    status = DISCONNECTED

    @classmethod
    def OnLogin(cls, code, msg):
        logger.info(msg.encode('utf-8'))
        if str(code) == '0000':
            XASessionEvents.status = XASessionEvents.CONNECTED
        else:
            XASessionEvents.status = XASessionEvents.FAILED

    @classmethod
    def OnLogout(cls):
        pass

    @classmethod
    def OnDisconnect(cls):
        pass


class XASession(object):

    session = None

    @classmethod
    def login(cls, id, pw, cert=None):
        logger.debug("Trying to log in...")
        if not settings.DEMO:
            server_addr = "hts.etrade.co.kr"
        else:
            server_addr = "demo.etrade.co.kr"

        try:
            pythoncom.CoInitialize()
        except pythoncom.com_error:
            # already initialized.
            pass

        XASession.session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
        if not XASession.session.IsConnected():
            server_port = 20001
            server_type = 0
            XASession.session.ConnectServer(server_addr, server_port)
            XASession.session.Login(id, pw, cert, server_type, 0)

        while XASessionEvents.status == XASessionEvents.DISCONNECTED:
            pythoncom.PumpWaitingMessages()

        if XASessionEvents.status == XASessionEvents.CONNECTED:
            return XASession.session
