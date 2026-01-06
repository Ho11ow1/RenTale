label Example:
    
    $ result = RenTale.Managers.SceneManager.CleanCallScreen("ExampleScreen")

    if (result == "MeetWillow"):
        $ RenTale.Managers.SceneManager.CleanJump("MeetWillow")

    elif (result == "MeetAlice"):
        $ RenTale.Managers.SceneManager.CleanJump("MeetAlice")

    elif (result == "Leave"):
        $ RenTale.Managers.SceneManager.CleanJump("Leave")

