import logging
from typing import Text, Dict, Optional, Callable, Awaitable, Any

from sanic import Blueprint, response
from sanic.request import Request

from rasa.core.channels.channel import (
    CollectingOutputChannel,
    UserMessage,
    InputChannel,
)


from rasa.core.channels.callback import (CallbackInput, CallbackOutput)
from rasa.core.channels.rest import RestInput
from rasa.utils.endpoints import EndpointConfig, ClientResponseError
from sanic.response import HTTPResponse


import base64
import json

import logging

logger = logging.getLogger(__name__)



class CallbackOutput(CollectingOutputChannel):
    @classmethod
    def name(cls) -> Text:
        return "callback"

    def __init__(self, endpoint: EndpointConfig) -> None:

        self.callback_endpoint = endpoint
        print(self.callback_endpoint)
        print(dir(self.callback_endpoint))

        super().__init__()

    async def _persist_message(self, message: Dict[Text, Any]) -> None:
        await super()._persist_message(message)
        
        
        #usrPass = "umanizales360:Umanizl8"
        #import requests
        
        #for s in message.keys():
        #    message[s] = message[s].replace('?', '')
        
        message = message["text"]

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Basic dW1hbml6YWxlczM2MDpVbWFuaXpsOA==',
        }

        #data = '{"to": ["573164828430"], "message": message, "from": "msg", "campaignName": "Nombre Campana Chec"}' 
        data = str({"to": ["573164828430", "573136852808", "577147547293", "573122327042", "573007752121"], "message": message, "from": "msg", "campaignName": "Nombre Campana Chec"}).replace("'", '"' )
        print(data)
        
        #b64Val = base64.b64encode(usrPass.encode('utf-8'))
        #headers=["Accept:Application/json","Authorization:Basic dW1hbml6YWxlczM2MDpVbWFuaXpsOA=="]#%b64Val]
        
        
        
        #headers={"Accept": "Application/json", "Authorization": "Basic %s"%b64Val.decode('utf-8')}

        try:
            await self.callback_endpoint.request(
                method="post",  data=data, headers=headers # content_type="application/json",
            )
            
        except ClientResponseError as e:
            '''print('hola0')
            r.raise_for_status()
            logger.info("Got response [%s] for URL: %s", r.status, url)
            html = await r.text()
            print(html)'''
            print('hola1')
            print(getattr(e, "message", None))
            print('hola2')
            print(getattr(e, "__dict__", {}))
            print('hola3', message)
            print('hola4', type(message))
            print(dir(message))

            logger.error(
                "Failed to send output message to callback. "
                "Status: {} Response: {}"
                "".format(e.status, e.text)
            )




class CallbackInput(CallbackInput):
    """A custom REST http input channel that responds using a callback server.

    Incoming messages are received through a REST interface. Responses
    are sent asynchronously by calling a configured external REST endpoint."""

    @classmethod
    def name(cls) -> Text:
        return "callback"

    @classmethod
    def from_credentials(cls, credentials: Optional[Dict[Text, Any]]) -> InputChannel:
        return cls(EndpointConfig.from_dict(credentials))

    def __init__(self, endpoint: EndpointConfig) -> None:
        print(endpoint)
        self.callback_endpoint = endpoint

        

    def blueprint(
        self, on_new_message: Callable[[UserMessage], Awaitable[Any]]
    ) -> Blueprint:
        callback_webhook = Blueprint("callback_webhook", __name__)

        @callback_webhook.route("/", methods=["GET"])
        async def health(_: Request):
            return response.json({"status": "ok"})

        @callback_webhook.route("/webhook", methods=["POST"])
        async def webhook(request: Request) -> HTTPResponse:
            sender_id = await self._extract_sender(request)
            text = self._extract_message(request)

            collector = self.get_output_channel()
            await on_new_message(
                UserMessage(text, collector, sender_id, input_channel=self.name())
            )
            return response.text("success")
        #print(callback_webhook)
        return callback_webhook

    def get_output_channel(self) -> CollectingOutputChannel:
        print(dir(CallbackOutput(self.callback_endpoint)))
        #print(CallbackOutput(self.callback_endpoint.)

        return CallbackOutput(self.callback_endpoint)