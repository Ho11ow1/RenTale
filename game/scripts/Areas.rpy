label Example:
    
    $ result = RenTale.Managers.SceneManager.CleanCallScreen("Screen_Example")

    if (result == "Meet_Willow"):
        $ RenTale.Managers.SceneManager.CleanJump("Meet_Willow")

    elif (result == "Meet_Alice"):
        $ RenTale.Managers.SceneManager.CleanJump("Meet_Alice")

    elif (result == "Leave"):
        $ RenTale.Managers.SceneManager.CleanJump("Leave")

