default discord_save_state_key = None

define discord_states = {
    "_main_menu_screen": {
        "details": "Main Menu"
    },
    "start": {
        "details": "Game"
    }
}


init python:
    config.start_callbacks += [Discord._on_start]
    config.quit_callbacks += [Discord._on_quit]
    config.after_load_callbacks += [Discord._on_load]
    config.label_callbacks += [Discord._on_label]


init -10 python:
    import pypresence
    import time

    class Discord():
        RPC = None
        START_TIME = time.time()
        # NOTE: Update APP_ID with your discord application ID -> https://discord.com/developers/applications/APP_ID/information
        APP_ID = ""

        @classmethod
        def _on_start(cls) -> None:
            """
            DO NOT CALL THIS METHOD
            """
            if cls.RPC is not None or not getattr(renpy.store, "discord_states", False):
                return

            try:
                cls.RPC = pypresence.Presence(cls.APP_ID)
                cls.RPC.connect()

            except Exception as ex:
                print(f"DiscordRPC start exception | {ex}")
                cls.RPC = None


        @classmethod
        def _on_quit(cls) -> None:
            """
            DO NOT CALL THIS METHOD
            """
            if cls.RPC is not None:
                cls.RPC.close()


        @classmethod
        def _on_load(cls) -> None:
            """
            DO NOT CALL THIS METHOD
            """
            cls.update(renpy.store.discord_save_state_key)


        @classmethod
        def _on_label(cls, name, is_abstract = False) -> None:
            """
            DO NOT CALL THIS METHOD
            """
            if not renpy.has_label(name) or not is_abstract:
                return

            cls.update(name)


        @classmethod
        def update(cls, key: str) -> None:
            """
            key: Expected to be a key of `discord_states` dict at the top of this file
            """
            if cls.RPC is None or type(key) != str:
                return

            d = renpy.store.discord_states.get(key, None)
            if d is None:
                return

            try:
                cls.RPC.update(**d, start = cls.START_TIME)
                renpy.store.discord_save_state_key = key

            except Exception as ex:
                print(f"DiscordRPC update exception | {ex}")
