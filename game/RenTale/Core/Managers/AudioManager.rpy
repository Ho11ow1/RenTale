init -90 python:
    class AudioManager():
# =============== MASTER =============== #
        @staticmethod
        def SetMasterVolume(volume: float) -> None:
            """
            Sets the master channel volume to the specified 'volume'
            """
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            preferences.set_mixer("main", volume)


        @staticmethod
        def GetMasterVolume() -> float:
            """
            Returns the current master channel volume
            """
            return preferences.get_mixer("main")


# =============== BGM =============== #
        @staticmethod
        def PlayBGM(file: str, loop: bool = True, fadeIn: float = 0.0) -> None:
            """
            Plays the specified audio file on the "BGM" channel
            """
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(loop) != bool:
                raise RenTaleTypeError(bool, type(loop))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))

            renpy.music.play(file, channel = "music", loop = loop, fadein = fadeIn)


        @staticmethod
        def StopBGM(fadeOut: float | None = 0.0) -> None:
            """
            Stops any and all audio playing on the "BGM" channel
            """
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "music", fadeout = fadeOut)

        
        @staticmethod
        def SetBGMVolume(volume: float) -> None:
            """
            Sets the BGM channel volume to the specified 'volume'
            """
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            preferences.set_mixer("music", volume)

        @staticmethod
        def GetBGMVolume() -> float:
            """
            Returns the current BGM channel volume
            """
            return preferences.get_mixer("music")

# =============== SFX =============== #
        @staticmethod
        def PlaySFX(file: str, fadeIn: float = 0.0) -> None:
            """
            Plays the specified audio file on the "SFX" channel
            """
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))

            renpy.music.play(file, channel = "sound", loop = False, fadein = fadeIn)


        @staticmethod
        def StopSFX(fadeOut: float | None = 0.0) -> None:
            """
            Stops any and all audio playing on the "SFX" channel
            """
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "sound", fadeout = fadeOut)

        
        @staticmethod
        def SetSFXVolume(volume: float) -> None:
            """
            Sets the SFX channel volume to the specified 'volume'
            """
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            preferences.set_mixer("sfx", volume)


        @staticmethod
        def GetSFXVolume() -> float:
            """
            Returns the current SFX channel volume
            """
            return preferences.get_mixer("sfx")


# =============== VOICE =============== #
        @staticmethod
        def PlayVO(file: str, fadeIn: float = 0.0) -> None:
            """
            Plays the specified audio file on the "VO" channel
            """
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))

            renpy.music.play(file, channel = "voice", loop = False, fadein = fadeIn)


        @staticmethod
        def StopVO(fadeOut: float | None = 0.0) -> None:
            """
            Stops any and all audio playing on the "VO" channel
            """
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "voice", fadeout = fadeOut)

        
        @staticmethod
        def SetVOVolume(volume: float) -> None:
            """
            Sets the VO channel volume to the specified 'volume'
            """
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            preferences.set_mixer("voice", volume)


        @staticmethod
        def GetVOVolume() -> float:
            """
            Returns the current VO channel volume
            """
            return preferences.get_mixer("voice")
