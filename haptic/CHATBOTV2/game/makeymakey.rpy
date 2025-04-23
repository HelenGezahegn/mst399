# makeymakey.rpy - Complete Ren'Py-only solution

# Simple counter implementation
init -10 python:
    # Global counter variables
    up_count = 0
    down_count = 0
    left_count = 0
    right_count = 0
    click_count = 0
    right_click_count = 0
    
    # Simple counter functions
    def increment_up():
        global up_count
        up_count += 1
        renpy.notify(f"UP: {up_count}")
    
    def increment_down():
        global down_count
        down_count += 1
        renpy.notify(f"DOWN: {down_count}")
    
    def increment_left():
        global left_count
        left_count += 1
        renpy.notify(f"LEFT: {left_count}")
    
    def increment_right():
        global right_count
        right_count += 1
        renpy.notify(f"RIGHT: {right_count}")
    
    def increment_click():
        global click_count
        click_count += 1
        renpy.notify(f"CLICK: {click_count}")
    
    def increment_right_click():
        global right_click_count
        right_click_count += 1
        renpy.notify(f"RIGHT CLICK: {right_click_count}")
    
    def reset_all():
        global up_count, down_count, left_count, right_count, click_count, right_click_count
        up_count = 0
        down_count = 0
        left_count = 0
        right_count = 0
        click_count = 0
        right_click_count = 0
        renpy.notify("All counters reset")

# Super simple MakeyMakey test screen
screen makeymakey_test():
    # Make the screen modal so it captures all input
    modal True
    
    # Background
    add "makeymakey_bg.png"
    
    # Title
    text "MakeyMakey Test" size 80 color "#78c4ff":
        xpos 75
        ypos 75
    
    # Return button
    textbutton "Return to Main Menu":
        xpos 75
        ypos 165
        text_color "#a0a0a0"
        text_hover_color "#ffffff"
        action Return()
    
    # Input counter display
    frame:
        xalign 0.98
        yalign 0.05
        background "#00000080"
        padding (20, 20)
        
        vbox:
            spacing 10
            
            text "Input Counter:" color "#ffffff" xalign 0.5
            
            text f"UP: {up_count}" color "#cccccc"
            text f"DOWN: {down_count}" color "#cccccc"
            text f"LEFT: {left_count}" color "#cccccc"
            text f"RIGHT: {right_count}" color "#cccccc"
            text f"CLICK: {click_count}" color "#cccccc"
            text f"RIGHT CLICK: {right_click_count}" color "#cccccc"
            
            null height 20
            
            text "Test Inputs:" color "#ffffff" xalign 0.5
            
            # Action buttons
            grid 2 2:
                spacing 15
                
                textbutton "↑ Up":
                    action increment_up
                    text_color "#ffffff"
                    text_hover_color "#78c4ff"
                
                textbutton "↓ Down":
                    action increment_down
                    text_color "#ffffff"
                    text_hover_color "#78c4ff"
                
                textbutton "← Left":
                    action increment_left
                    text_color "#ffffff"
                    text_hover_color "#78c4ff"
                
                textbutton "→ Right":
                    action increment_right
                    text_color "#ffffff"
                    text_hover_color "#78c4ff"
            
            null height 10
            
            grid 2 1:
                spacing 15
                textbutton "Click":
                    action increment_click
                    text_color "#ffffff"
                    text_hover_color "#78c4ff"
                
                textbutton "Right Click":
                    action increment_right_click
                    text_color "#ffffff"
                    text_hover_color "#78c4ff"
            
            null height 20
            
            # Reset button
            textbutton "Reset Counters":
                action reset_all
                text_color "#ffffff"
                text_hover_color "#e74c3c"
    
    # Instructions panel at the bottom
    frame:
        xalign 0.5
        yalign 1.0
        xsize 1000
        background "#00000080"
        padding (20, 20)
        margin (0, 0, 0, 20)
        
        vbox:
            spacing 10
            text "This screen demonstrates how the MakeyMakey controller works." color "#ffffff" xalign 0.5
            text "Click the buttons on the right to simulate MakeyMakey inputs:" color "#ffffff" xalign 0.5
            
            hbox:
                xalign 0.5
                spacing 40
                
                vbox:
                    spacing 5
                    text "• LEFT HAND → LEFT CLICK" color "#cccccc"
                    text "• RIGHT HAND → RIGHT CLICK" color "#cccccc"
                
                vbox:
                    spacing 5
                    text "• LEFT FOOT → UP ARROW" color "#cccccc"
                    text "• RIGHT FOOT → DOWN ARROW" color "#cccccc"

# Simple entry point
label test_makey_makey:
    # Reset counters
    $ reset_all()
    
    # Hide main menu
    $ renpy.hide_screen("main_menu")
    
    # Go to the test screen
    call screen makeymakey_test
    
    # This will get called when Return is clicked
    return