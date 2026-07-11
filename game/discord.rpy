init python:
    import time
    from pypresence import Presence

    class Discord():
        START_TIME = time.time()

        APP_ID = ""         # Update with your discord Application Id from "https://discord.com/developers/applications/APP_ID/information"
        LARGE_IMAGE = ""    # Update this with the key of your application large image from "https://discord.com/developers/applications/APP_ID/rich-presence/assets"
        LARGE_TEXT = ""     # Update this with the text you want to show when hovering over LARGE_IMAGE
        SMALL_IMAGE = ""    # Update this with the key of your applications small image from "https://discord.com/developers/applications/APP_ID/rich-presence/assets"
        SMALL_TEXT = ""     # Update this with the text you want to show when hovering over SMALL_IMAGE

        DISCORD_RPC = None

        @classmethod
        def init(cls) -> None:
            if cls.DISCORD_RPC is None:
                try:
                    cls.DISCORD_RPC = Presence(cls.APP_ID)
                    cls.DISCORD_RPC.connect()

                except Exception as ex:
                    print("RPC Init error: ", ex)
                    cls.DISCORD_RPC = None


        @classmethod
        def update(cls, details: str | None = None, state: str | None = None) -> None:
            if details is not None and type(details) != str:
                raise rentale.RenTaleTypeError((str, type(None)), type(details))
            if state is not None and type(state) != str:
                raise rentale.RenTaleTypeError((str, type(None)), type(state))

            if cls.DISCORD_RPC is None:
                cls.init()

            if cls.DISCORD_RPC is None:
                return

            try:
                cls.DISCORD_RPC.update(details = details, state = state, start = cls.START_TIME, large_image = cls.LARGE_IMAGE, large_text = cls.LARGE_TEXT, small_image = cls.SMALL_IMAGE, small_text = cls.SMALL_TEXT)

            except Exception as ex:
                print("RPC Update error: ", ex)
