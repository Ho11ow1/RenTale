init -90 python:
    class AudioManager():
# =============== MASTER =============== #
        @staticmethod
        def SetMasterVolume(volume: float) -> None:
            if type(volume) != float:
                raise TypeError(f"Expected 'Float', got '{type(volume).__name__}'")
            if volume > 1 or volume < 0:
                raise ValueError(f"Expected value between 1 and 0, got: {volume}")

            preferences.set_mixer("main", volume)


        @staticmethod
        def GetMasterVolume() -> float:
            return preferences.get_mixer("main")


# =============== BGM =============== #
        @staticmethod
        def PlayBGM(file: str, loop: bool = False, fadeIn: float = 0.0) -> None:
            if type(file) != str:
                raise TypeError(f"Expected 'String' file path, got '{type(file).__name__}'")
            if type(loop) != bool:
                raise TypeError(f"Expected 'Bool', got '{type(loop).__name__}'")
            if type(fadeIn) != float:
                raise TypeError(f"Expected 'Float', got '{type(fadeIn).__name__}'")

            renpy.music.play(file, channel = "music", loop = loop, fadein = fadeIn)


        @staticmethod
        def StopBGM(fadeOut: float | None = 0.0) -> None:
            if fadeOut is not None and type(fadeOut) != float:
                raise TypeError(f"Expected 'Float' or 'None', got '{type(fadeOut).__name__}'")
            if fadeOut < 0:
                raise ValueError(f"Expected positive number, got: {fadeOut}")

            renpy.music.stop(channel = "music", fadeout = fadeOut)

        
        @staticmethod
        def SetBGMVolume(volume: float) -> None:
            if type(volume) != float:
                raise TypeError(f"Expected 'Float', got '{type(volume).__name__}'")
            if volume > 1 or volume < 0:
                raise ValueError(f"Expected value between 1 and 0, got: {volume}")

            preferences.set_mixer("music", volume)

        @staticmethod
        def GetBGMVolume() -> float:
            return preferences.get_mixer("music")

# =============== SFX =============== #
        @staticmethod
        def PlaySFX(file: str, fadeIn: float = 0.0) -> None:
            if type(file) != str:
                raise TypeError(f"Expected 'String' file path, got '{type(file).__name__}'")
            if type(fadeIn) != float:
                raise TypeError(f"Expected 'Float', got '{type(fadeIn).__name__}'")

            renpy.music.play(file, channel = "sound", loop = False, fadein = fadeIn)


        @staticmethod
        def StopSFX(fadeOut: float = 0.0) -> None:
            if fadeOut is not None and type(fadeOut) != float:
                raise TypeError(f"Expected 'Float' or 'None', got '{type(fadeOut).__name__}'")
            if fadeOut < 0:
                raise ValueError(f"Expected positive number, got: {fadeOut}")

            renpy.music.stop(channel = "sound", fadeout = fadeOut)

        
        @staticmethod
        def SetSFXVolume(volume: float) -> None:
            if type(volume) != float:
                raise TypeError(f"Expected 'Float', got '{type(volume).__name__}'")
            if volume > 1 or volume < 0:
                raise ValueError(f"Expected value between 1 and 0, got: {volume}")

            preferences.set_mixer("sfx", volume)


        @staticmethod
        def GetSFXVolume() -> float:
            return preferences.get_mixer("sfx")


# =============== VOICE =============== #
        @staticmethod
        def PlayVO(file: str, fadeIn: float = 0.0) -> None:
            if type(file) != str:
                raise TypeError(f"Expected 'String' file path, got '{type(file).__name__}'")
            if type(fadeIn) != float:
                raise TypeError(f"Expected 'Float', got '{type(fadeIn).__name__}'")

            renpy.music.play(file, channel = "voice", loop = False, fadein = fadeIn)


        @staticmethod
        def StopVO(fadeOut: float = 0.0) -> None:
            if fadeOut is not None and type(fadeOut) != float:
                raise TypeError(f"Expected 'Float' or 'None', got '{type(fadeOut).__name__}'")
            if fadeOut < 0:
                raise ValueError(f"Expected positive number, got: {fadeOut}")

            renpy.music.stop(channel = "voice", fadeout = fadeOut)

        
        @staticmethod
        def SetVOVolume(volume: float) -> None:
            if type(volume) != float:
                raise TypeError(f"Expected 'Float', got '{type(volume).__name__}'")
            if volume > 1 or volume < 0:
                raise ValueError(f"Expected value between 1 and 0, got: {volume}")

            preferences.set_mixer("voice", volume)


        @staticmethod
        def GetVOVolume() -> float:
            return preferences.get_mixer("voice")
