init -90 python:
    class AudioManager():

        MUSIC_CHANNEL = renpy.audio.audio.get_channel("music")
        SOUND_CHANNEL = renpy.audio.audio.get_channel("sound")
        VOICE_CHANNEL = renpy.audio.audio.get_channel("voice")

# =============== MUSIC CHANNEL =============== #
        @staticmethod
        def PlayBGM(file: str, loop: bool = True, fadeIn: float = 0.0, ifChanged: bool = False) -> None:
            """
            Plays the specified audio file on the music channel
            """
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(loop) != bool:
                raise RenTaleTypeError(bool, type(loop))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))
            if type(ifChanged) != bool:
                raise RenTaleTypeError(bool, type(ifChanged))

            renpy.music.play(file, channel = "music", loop = loop, fadein = fadeIn, if_changed = ifChanged)


        @staticmethod
        def StopBGM(fadeOut: float | None = 0.0) -> None:
            """
            Stops any and all audio playing on the music channel
            """
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "music", fadeout = fadeOut)

        
        @classmethod
        def SetBGMVolume(cls, volume: float) -> None:
            """
            Sets the music channel volume to the specified 'volume'
            """
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            cls.MUSIC_CHANNEL.set_volume(volume)


        @classmethod
        def GetBGMVolume(cls) -> float:
            """
            Returns the current music channel volume
            """
            return cls.MUSIC_CHANNEL.chan_volume


# =============== SOUND CHANNEL =============== #
        @staticmethod
        def PlaySFX(file: str, fadeIn: float = 0.0, ifChanged: bool = False) -> None:
            """
            Plays the specified audio file on the sound channel
            """
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))
            if type(ifChanged) != bool:
                raise RenTaleTypeError(bool, type(ifChanged))

            renpy.music.play(file, channel = "sound", loop = False, fadein = fadeIn, if_changed = ifChanged)


        @staticmethod
        def StopSFX(fadeOut: float | None = 0.0) -> None:
            """
            Stops any and all audio playing on the sound channel
            """
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "sound", fadeout = fadeOut)

        
        @classmethod
        def SetSFXVolume(cls, volume: float) -> None:
            """
            Sets the sound channel volume to the specified 'volume'
            """
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            cls.SOUND_CHANNEL.set_volume(volume)


        @classmethod
        def GetSFXVolume(cls) -> float:
            """
            Returns the current sound channel volume
            """
            return cls.SOUND_CHANNEL.chan_volume


# =============== VOICE CHANNEL =============== #
        @staticmethod
        def PlayVO(file: str, fadeIn: float = 0.0, ifChanged: bool = False) -> None:
            """
            Plays the specified audio file on the voice channel
            """
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))
            if type(ifChanged) != bool:
                raise RenTaleTypeError(bool, type(ifChanged))

            renpy.music.play(file, channel = "voice", loop = False, fadein = fadeIn, if_changed = ifChanged)


        @staticmethod
        def StopVO(fadeOut: float | None = 0.0) -> None:
            """
            Stops any and all audio playing on the voice channel
            """
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "voice", fadeout = fadeOut)

        
        @classmethod
        def SetVOVolume(cls, volume: float) -> None:
            """
            Sets the voice channel volume to the specified 'volume'
            """
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            cls.VOICE_CHANNEL.set_volume(volume)


        @classmethod
        def GetVOVolume(cls) -> float:
            """
            Returns the current voice channel volume
            """
            return cls.VOICE_CHANNEL.chan_volume
