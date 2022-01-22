"""Who dat?

pattern: `who$`
"""

from telethon import client, events
from .global_functions import log


# Simple test with who
@events.register(events.NewMessage(pattern=r"who$"))
async def on_start(event):
    print((await event.client.get_me()).first_name)
    #if event.is_private:    # If command was sent in private
    await log(event)    # Logs the event
    await event.respond('Aha!')
