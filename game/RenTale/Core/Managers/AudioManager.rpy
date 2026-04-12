init -90 python:
    class AudioManager():
# =============== MASTER =============== #
        @staticmethod
        def SetMasterVolume(volume: float) -> None:
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            preferences.set_mixer("main", volume)


        @staticmethod
        def GetMasterVolume() -> float:
            return preferences.get_mixer("main")


# =============== BGM =============== #
        @staticmethod
        def PlayBGM(file: str, loop: bool = False, fadeIn: float = 0.0) -> None:
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(loop) != bool:
                raise RenTaleTypeError(bool, type(loop))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))

            renpy.music.play(file, channel = "music", loop = loop, fadein = fadeIn)


        @staticmethod
        def StopBGM(fadeOut: float | None = 0.0) -> None:
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "music", fadeout = fadeOut)

        
        @staticmethod
        def SetBGMVolume(volume: float) -> None:
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            preferences.set_mixer("music", volume)

        @staticmethod
        def GetBGMVolume() -> float:
            return preferences.get_mixer("music")

# =============== SFX =============== #
        @staticmethod
        def PlaySFX(file: str, fadeIn: float = 0.0) -> None:
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))

            renpy.music.play(file, channel = "sound", loop = False, fadein = fadeIn)


        @staticmethod
        def StopSFX(fadeOut: float = 0.0) -> None:
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "sound", fadeout = fadeOut)

        
        @staticmethod
        def SetSFXVolume(volume: float) -> None:
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            preferences.set_mixer("sfx", volume)


        @staticmethod
        def GetSFXVolume() -> float:
            return preferences.get_mixer("sfx")


# =============== VOICE =============== #
        @staticmethod
        def PlayVO(file: str, fadeIn: float = 0.0) -> None:
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))

            renpy.music.play(file, channel = "voice", loop = False, fadein = fadeIn)


        @staticmethod
        def StopVO(fadeOut: float = 0.0) -> None:
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "voice", fadeout = fadeOut)

        
        @staticmethod
        def SetVOVolume(volume: float) -> None:
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            preferences.set_mixer("voice", volume)


        @staticmethod
        def GetVOVolume() -> float:
            return preferences.get_mixer("voice")
