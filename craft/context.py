import wharf

from typing import TYPE_CHECKING, Optional, List, Dict, Any

if TYPE_CHECKING:
    from .bot import Bot

class Context:
    def __init__(self, bot: "Bot", interaction: wharf.Interaction):
        self._interaction = interaction
        self._bot = bot
        self._deferred = False

    @property
    def bot(self):
        return self._bot
    
    @property
    def interaction(self):
        return self._interaction


    async def reply(
        self,
        content: Optional[str] = None,
        *,
        embed: Optional[wharf.Embed] = None,
        flags: Optional[wharf.MessageFlags] = None,
        file: Optional[wharf.File] = None,
        components: Optional[List[Dict[Any, Any]]] = None,
        type: int = 4,
    ) -> None:
        """
        Replies to a discord interaction
        Parameters
        -----------
        content: Optional[:class:`str`]
            The content to send
        embed: Optional[:class:`wharf.Embed`]
            Embed that should or should not be sent
        flags: Optional[:class:`wharf.MessageFlags`]
            Flags that go along with the sent interaction
        file: Optional[:class:`wharf.File`]
            File that should or should not be sent
        type: :class:`int`
            Type that the responded interaction should be
            https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-callback-type
        """

        await self.interaction.reply(
            content,
            embed=embed,
            flags=flags,
            file=file,
            components=components,
            type=type
        )
