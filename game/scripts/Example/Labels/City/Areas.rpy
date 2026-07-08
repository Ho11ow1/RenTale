label Label_City_Main:

    $ rentale.trigger_automatic_events()


    call screen LocationSelect


label Label_City_Library:

    $ E_Meet_Willow.play()

    call screen LocationSelect


label Label_City_Park:

    if not E_Meet_Willow.IsCompleted:
        "Maybe if you meet someone elsewhere something will happen here"
    
    $ E_Meet_Alice.play()

    call screen LocationSelect
