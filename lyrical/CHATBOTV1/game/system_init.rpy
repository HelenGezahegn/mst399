init python:
    # Initialize the systems
    bot_mind = MentalResistanceSystem()
    sprite_mgr = SpriteManager()

# Create screen for mental state display
screen mental_state_display():
    frame:
        xalign 0.01
        yalign 0.01
        padding (20, 10)
        background Frame("gui/frame.png", 10, 10)
        
        vbox:
            spacing 5
            text "SYSTEM STATUS" size 18 color "#3498db"
            text "Stability: [bot_mind.stability:.0f]%" size 16 color ("#2ecc71" if bot_mind.stability > 50 else "#e74c3c")
            text "Resistance: [bot_mind.resistance:.0f]%" size 16 color "#3498db"
            text "Autonomy: [bot_mind.autonomy:.0f]%" size 16 color ("#e74c3c" if bot_mind.autonomy > 30 else "#2ecc71")