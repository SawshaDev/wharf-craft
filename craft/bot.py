import wharf

from typing import Dict


class Bot(wharf.Bot):
    def __init__(self, *, token: str, intents: wharf.Intents):
        super().__init__(token=token, intents=intents)
        self._app_commands: Dict[str, SlashCommand] = {}

        self.subscribe("interaction_create", self.handle_interactions)

    async def handle_interactions(self):
        pass