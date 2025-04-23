init -1 python:
    key_counts = {
        "up": 0,
        "down": 0,
        "click": 0,
        "right_click": 0,
        "space": 0
    }
    
    # Recent input history
    key_history = []
    
    # Save original keymap to restore later
    original_keymap = dict(config.keymap)
    
    # Function to disable navigation keys
    def disable_navigation():
        # Save existing navigation keys
        global original_keymap
        original_keymap = dict(config.keymap)
        
        # Disable navigation by setting empty keymaps
        config.keymap['game_menu'] = []
        config.keymap['hide_windows'] = []
        config.keymap['self_voicing'] = []
        config.keymap['accessibility'] = []
        config.keymap['rollback'] = []
        config.keymap['rollforward'] = []
        
        # Set custom keymap handlers
        config.keymap['test_up'] = ['K_UP']
        config.keymap['test_down'] = ['K_DOWN']
        config.keymap['test_space'] = ['K_SPACE']
        
        renpy.hide_screen("quick_menu")
    
    # Function to restore navigation
    def restore_navigation():
        global original_keymap
        config.keymap = dict(original_keymap)
    
    # Function to track a key press with special mappings
    def record_keypress(key_name):
        global key_counts, key_history
        
        # Special mapping: SPACE also triggers RIGHT_CLICK
        if key_name == "space":
            # Increment both space and right_click counters
            key_counts["space"] = key_counts.get("space", 0) + 1
            key_counts["right_click"] = key_counts.get("right_click", 0) + 1
            
            # Add to history
            key_history.insert(0, f"space → right_click")
            if len(key_history) > 5:
                key_history.pop()
                
            # Notify
            renpy.notify(f"SPACE mapped to RIGHT CLICK: {key_counts['right_click']}")
        else:
            # Regular key - increment its counter
            key_counts[key_name] = key_counts.get(key_name, 0) + 1
            
            # Add to history
            key_history.insert(0, key_name)
            if len(key_history) > 5:
                key_history.pop()
            
            # Notify
            renpy.notify(f"{key_name}: {key_counts[key_name]}")
        
        # Force screen update
        renpy.restart_interaction()
    
    # Reset all counters
    def reset_all_keys():
        global key_counts, key_history
        key_counts = {k: 0 for k in key_counts}
        key_history = []
        renpy.notify("All counters reset")
# Custom screen with simplified layout
screen makeymakey_test():
    # Use modal to prevent clicks going elsewhere
    modal True
    
    # Background
    add "makeymakey_bg.png"
    
    # Title and Return button area
    vbox:
        xpos 75
        ypos 75
        spacing 20
        
        text "MakeyMakey Test" size 80 color "#78c4ff"
        
        textbutton "Return to Main Menu (Press Enter)":
            text_color "#a0a0a0"
            text_hover_color "#ffffff"
            action [Function(restore_navigation), Return()]
    
    # Key handler - only track up, down, space, and clicks
    key "K_UP" action Function(record_keypress, "up")
    key "K_DOWN" action Function(record_keypress, "down")
    key "K_SPACE" action Function(record_keypress, "space")  # Maps to right_click too
    key "mouseup_1" action Function(record_keypress, "click")
    key "mouseup_3" action Function(record_keypress, "right_click")
    
    # Counter display - top right with clear styling
    frame:
        xalign 0.98
        yalign 0.05
        background "#00000080"
        padding (20, 20)
        
        vbox:
            spacing 15
            
            text "Input Counter:" color "#ffffff" xalign 0.5 size 24
            
            # Only show relevant counters with clearer labels
            text "UP ARROW: [key_counts['up']]" color "#cccccc"
            text "DOWN ARROW: [key_counts['down']]" color "#cccccc"
            text "LEFT CLICK: [key_counts['click']]" color "#cccccc"
            hbox:
                spacing 5
                text "RIGHT CLICK: [key_counts['right_click']]" color "#f1c40f"
                text "←" color "#f1c40f"
                text "Space maps here" color "#f1c40f" size 16
            hbox:
                spacing 5
                text "SPACE: [key_counts['space']]" color "#f1c40f"
                text "→" color "#f1c40f"
                text "Maps to right click" color "#f1c40f" size 16
            
            null height 20
            
            # Recent inputs
            text "Recent Inputs:" color "#ffffff" xalign 0.5 size 24
            if key_history:
                vbox:
                    spacing 5
                    for entry in key_history:
                        if "→" in entry:
                            text entry color "#f1c40f"  # Highlight mapped inputs
                        else:
                            text f"- {entry}" color "#cccccc"
            else:
                text "No inputs yet" color "#555555"
            
            null height 15
            
            # Reset button
            textbutton "Reset Counters":
                xalign 0.5
                action Function(reset_all_keys)
                text_color "#ffffff" 
                text_hover_color "#e74c3c"
    
    # BOTTOM INSTRUCTION BOX
    frame:
        xalign 0.5
        yalign 0.96
        xsize 650
        background "#00000080"
        padding (20, 15)
        
        vbox:
            spacing 10
            xalign 0.5
            
            text "Raw Key Event Capture Active" size 28 color "#ffffff" xalign 0.5
            text "Controller Hander for Haptic Experiment's Robot Hands" size 22 color "#ffffff" xalign 0.5
            
            null height 5
            
            hbox:
                xalign 0.5
                spacing 50
                
                vbox:
                    spacing 8
                    xalign 0.5
                    text "- Pointer finger: Left click" color "#cccccc" size 22
                    text "- Middle finger: Right click" color "#cccccc" size 22
                
                vbox:
                    spacing 8
                    xalign 0.5
                    text "- Yellow Arrow: Up" color "#cccccc" size 22
                    text "- Orange Arrow: Down" color "#cccccc" size 22

# Test label with navigation disabled
label test_makey_makey:
    # Disable navigation to capture raw key events
    $ disable_navigation()
    
    # Reset counters
    $ reset_all_keys()
    
    $ renpy.hide_screen("main_menu")
    
    # Show our test screen with raw key handling
    call screen makeymakey_test
    
    return