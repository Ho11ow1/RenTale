style example_button:
    xalign 0.5
    yalign 0.5


style example_button_text:
    xalign 0.5
    text_align 0.5
    justify True


style example_frame:
    background "#000"

screen ExampleScreen:
    frame:
        xfill True
        yfill True
        style_prefix "example"

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            textbutton "Go and meet Alice":
                action Return("MeetAlice")
                xsize 300

            textbutton "Go and meet Willow":
                action Return("MeetWillow")
                xsize 300

            textbutton "Leave":
                action Return("Leave")
                xsize 300

