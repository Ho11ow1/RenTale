init -90 python in rentale:
    class AudioManager():

        MUSIC_CHANNEL = renpy.audio.audio.get_channel("music")
        SOUND_CHANNEL = renpy.audio.audio.get_channel("sound")
        VOICE_CHANNEL = renpy.audio.audio.get_channel("voice")

# =============== MUSIC CHANNEL =============== #
        @staticmethod
        def play_music(file: str, loop: bool = True, fadeIn: float = 0.0, fadeOut: float | None = None, tight: bool = False, ifChanged: bool = False) -> None:
            """
            Plays the specified audio file on the music channel
            """
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(loop) != bool:
                raise RenTaleTypeError(bool, type(loop))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if type(tight) != bool:
                raise RenTaleTypeError(bool, type(tight))
            if type(ifChanged) != bool:
                raise RenTaleTypeError(bool, type(ifChanged))

            renpy.music.play(file, channel = "music", loop = loop, fadein = fadeIn, fadeout = fadeOut, tight = tight, if_changed = ifChanged)


        @staticmethod
        def stop_music(fadeOut: float | None = None) -> None:
            """
            Stops any and all audio playing on the music channel
            """
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "music", fadeout = fadeOut)

        
        @classmethod
        def set_music_volume(cls, volume: float) -> None:
            """
            Sets the music channel volume to the specified 'volume'
            """
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            cls.MUSIC_CHANNEL.set_volume(volume)


        @classmethod
        def get_music_volume(cls) -> float:
            """
            Returns the current music channel volume
            """
            return cls.MUSIC_CHANNEL.chan_volume


# =============== SOUND CHANNEL =============== #
        @staticmethod
        def play_sound(file: str, fadeIn: float = 0.0, ifChanged: bool = False) -> None:
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
        def stop_sound(fadeOut: float | None = None) -> None:
            """
            Stops any and all audio playing on the sound channel
            """
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "sound", fadeout = fadeOut)

        
        @classmethod
        def set_sound_volume(cls, volume: float) -> None:
            """
            Sets the sound channel volume to the specified 'volume'
            """
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            cls.SOUND_CHANNEL.set_volume(volume)


        @classmethod
        def get_sound_volume(cls) -> float:
            """
            Returns the current sound channel volume
            """
            return cls.SOUND_CHANNEL.chan_volume


# =============== VOICE CHANNEL =============== #
        @staticmethod
        def play_voice(file: str, fadeIn: float = 0.0, ifChanged: bool = False) -> None:
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
        def stop_voice(fadeOut: float | None = None) -> None:
            """
            Stops any and all audio playing on the voice channel
            """
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = "voice", fadeout = fadeOut)

        
        @classmethod
        def set_voice_volume(cls, volume: float) -> None:
            """
            Sets the voice channel volume to the specified 'volume'
            """
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            cls.VOICE_CHANNEL.set_volume(volume)


        @classmethod
        def get_voice_volume(cls) -> float:
            """
            Returns the current voice channel volume
            """
            return cls.VOICE_CHANNEL.chan_volume

# =============== VOICE CHANNEL =============== #
        @staticmethod
        def play_custom(file: str, channel: str, loop: bool = False, fadeIn: float = 0.0, fadeOut: float | None = None, tight: bool = False, ifChanged: bool = False) -> None:
            """
            Plays the specified audio file on the specified channel
            """
            if type(file) != str:
                raise RenTaleTypeError(str, type(file))
            if type(channel) != str:
                raise RenTaleTypeError(str, type(channel))
            if not renpy.music.channel_defined(channel):
                raise RenTaleArgumentException(f"Audio channel {channel} is not defined.")
            if type(loop) != bool:
                raise RenTaleTypeError(bool, type(loop))
            if type(fadeIn) != float:
                raise RenTaleTypeError(float, type(fadeIn))
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeIn))
            if type(tight) != bool:
                raise RenTaleTypeError(bool, type(tight))
            if type(ifChanged) != bool:
                raise RenTaleTypeError(bool, type(ifChanged))

            renpy.music.play(file, channel = channel, loop = loop, fadein = fadeIn, fadeout = fadeOut, tight = tight, if_changed = ifChanged)


        @staticmethod
        def stop_custom(channel: str, fadeOut: float | None = None) -> None:
            """
            Stops any and all audio playing on the specified channel
            """
            if type(channel) != str:
                raise RenTaleTypeError(str, type(channel))
            if not renpy.music.channel_defined(channel):
                raise RenTaleArgumentException(f"Audio channel {channel} is not defined.")
            if fadeOut is not None and type(fadeOut) != float:
                raise RenTaleTypeError((float, type(None)), type(fadeOut))
            if fadeOut < 0:
                raise RenTaleValueError("positive number", fadeOut)

            renpy.music.stop(channel = channel, fadeout = fadeOut)


        @staticmethod
        def set_custom_volume(channel: str, volume: float) -> None:
            """
            Sets the specified channels volume to the specified volume
            """
            if type(channel) != str:
                raise RenTaleTypeError(str, type(channel))
            if not renpy.music.channel_defined(channel):
                raise RenTaleArgumentException(f"Audio channel {channel} is not defined.")
            if type(volume) != float:
                raise RenTaleTypeError(float, type(volume))
            if volume > 1 or volume < 0:
                raise RenTaleValueError("value between 1 and 0", volume)

            renpy.audio.audio.get_channel(channel).set_volume(volume)


        @staticmethod
        def get_custom_volume(channel: str) -> float:
            """
            Returns the specified channels current volume
            """
            if type(channel) != str:
                raise RenTaleTypeError(str, type(channel))
            if not renpy.music.channel_defined(channel):
                raise RenTaleArgumentException(f"Audio channel {channel} is not defined.")

            return renpy.audio.audio.get_channel(channel).chan_volume
