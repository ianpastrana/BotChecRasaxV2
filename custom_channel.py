import asyncio
import inspect
from sanic import Sanic, Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse
from typing import Text, Dict, Any, Optional, Callable, Awaitable, NoReturn

import rasa.utils.endpoints
from rasa.core.channels.channel import (
    InputChannel,
    CollectingOutputChannel,
    UserMessage,
)

class MyIO(InputChannel):
    def name(cls) -> Text:
        print("hola desde metodo name")
        """Name of your custom channel."""
        return "myio"

    def blueprint(
        self, on_new_message: Callable[[UserMessage], Awaitable[None]]
    ) -> Blueprint:

        custom_webhook = Blueprint(
            "custom_webhook_{}".format(type(self).__name__),
            inspect.getmodule(self).__name__,
        )

        @custom_webhook.route("/", methods=["GET"])
        async def health(request: Request) -> HTTPResponse:
            return response.json({"status": "ok"})

        @custom_webhook.route("/webhook", methods=["POST"])
        async def receive(request: Request) -> HTTPResponse:
            print(request)
            sender_id = request.json.get("source_addr") # method to get sender_id.   request.json.get("sender")
            text = request.json.get("message") # method to fetch text. request.json.get("text")
            input_channel = self.name() # method to fetch input channel
            metadata = self.get_metadata(request) # method to get metadata
            country = request.json.get("country")
            dest_addr = request.json.get("dest_addr")
            date = request.json.get("date")
            print(country)

            collector = CollectingOutputChannel()
            
            # include exception handling
            
            # As part of your implementation of the receive endpoint, you will need to tell Rasa to handle the user message.
            # https://rasa.com/docs/rasa/reference/rasa/core/channels/channel#usermessage-objects
            await on_new_message(
                UserMessage(
                    text,
                    collector, # the output channel which should be used to send bot responses back to the user.
                    sender_id,
                    input_channel=input_channel,
                    metadata=metadata
                )
            )

            return response.json(collector.messages)

        return custom_webhook
