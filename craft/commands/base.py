from __future__ import annotations

import wharf

from typing import Any, Optional

class CommandOption(wharf.CommandOption):
    __option_types = {
        wharf.Member: wharf.InteractionOptionType.user,
        wharf.User: wharf.InteractionOptionType.user,
        wharf.Role: wharf.InteractionOptionType.role,
        wharf.TextChannel: wharf.InteractionOptionType.channel,
        wharf.Role | wharf.Member: wharf.InteractionOptionType.mentionable,
        bool: wharf.InteractionOptionType.boolean,
        str: wharf.InteractionOptionType.string,
        int: wharf.InteractionOptionType.integer,
        float: wharf.InteractionOptionType.float,
    }   

    def __init__(self, name: str, description: str = "..", * , type: Any  = str, required: bool = False):
        type = self.__option_types.get(type, wharf.InteractionOptionType.string)
        super().__init__(name=name, description=description, type=type, required=required)



