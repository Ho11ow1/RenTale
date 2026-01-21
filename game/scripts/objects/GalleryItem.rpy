init -11 python: 
    class GalleryItem:
        def __init__(self, name, isUnlocked, thumbnail, scene, description):
            """
                For thumbnail use "images/" or else the image will not be shown
                For scene use an existing label to replay
            """

            if type(name) != str:
                raise TypeError(f"Expected string, got {type(name).__name__}")
            if type(isUnlocked) != bool:
                raise TypeError(f"Expected bool, got {type(isUnlocked).__name__}")
            if type(thumbnail) != str:
                raise TypeError(f"Expected string, got {type(thumbnail).__name__}")
            if type(scene) != str:
                raise TypeError(f"Expected string, got {type(scene).__name__}")
            if description is not None and type(description) != str:
                raise TypeError(f"Expected string or None, got {type(description).__name__}")

            self.Name = name
            self.IsUnlocked = isUnlocked
            self.Thumbnail = thumbnail
            self.Scene = scene
            self.Description = description

        
        def ToDict(self):
            return {
                "Name": self.Name,
                "IsUnlocked": self.IsUnlocked,
                "Thumbnail": self.Thumbnail,
                "Scene": self.Scene,
                "Description": self.Description
            }


        @staticmethod
        def FromDict(data):
            return GalleryItem(
                data["Name"],
                data["IsUnlocked"],
                data["Thumbnail"],
                data["Scene"],
                data.get("Description")
            )

