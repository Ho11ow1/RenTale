init python:
    import time
    import pypresence

    class Discord():
        START_TIME = time.time()
        DISCORD_RPC = None

        APP_ID = ""  # Update with your discord Application Id from "https://discord.com/developers/applications/APP_ID/information".
        
        state_dict = {                  # Update this dictionary as desired for your game, "mainmenu" is provided as an example.
            "mainmenu": {
                "details": "Doing nothing",
                "state": None,
                "large_image": None,
                "large_text": None,
                "small_image": None,
                "small_text": None,
            }
        }

        @classmethod
        def init(cls) -> None:
            if cls.DISCORD_RPC is None:
                try:
                    cls.DISCORD_RPC = pypresence.Presence(cls.APP_ID)
                    cls.DISCORD_RPC.connect()

                except Exception as ex:
                    print(f"RenTale DiscordRPC | Init error: {ex}")
                    cls.DISCORD_RPC = None


        @classmethod
        def update(cls, dictKey: str) -> None:
            if type(dictKey) != str:
                raise RenTaleTypeError(str, type(dictKey))

            if cls.DISCORD_RPC is None:
                cls.init()
            if cls.DISCORD_RPC is None:
                return

            args = None
            try:
                args = cls.state_dict[dictKey]

            except Exception:
                print(f"RenTale DiscordRPC | key '{dictKey}' not found in 'source_dict'")
                return

            try:
                cls.DISCORD_RPC.update(
                    details = args["details"], state = args["state"],
                    start = cls.START_TIME, 
                    large_image = args["large_image"], large_text = args["large_text"], 
                    small_image = args["small_image"], small_text = args["small_text"])

            except pypresence.PipeClosed:
                cls.DISCORD_RPC = None
                print("RenTale DiscordRPC | Failed to update - Pipe was closed")
                cls.init()
                cls.update(dictKey)

            except Exception as ex:
                print(f"RenTale DiscordRPC | Update Discord RPC failed: {ex}")
