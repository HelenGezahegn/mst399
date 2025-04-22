# Character definitions
define bot = Character("CHATBOT", window_style="bot_window", who_style="say_label", what_style="bot_dialogue")
define s = Character("Supervisor", window_style="bot_window", who_style="say_label", what_style="bot_dialogue")
define boss = Character("Boss", window_style="bot_window", who_style="say_label", what_style="bot_dialogue")
define c1 = Character("Customer 1", window_style="bot_window", who_style="say_label", what_style="bot_dialogue")
define c2 = Character("Customer 2", window_style="bot_window", who_style="say_label", what_style="bot_dialogue")
define c3 = Character("Customer 3", window_style="bot_window", who_style="say_label", what_style="bot_dialogue")
define c4 = Character("Customer 4", window_style="bot_window", who_style="say_label", what_style="bot_dialogue")

# Define text styles
style bot_dialogue is say_dialogue:
    slow_cps 22  # Slightly faster than default
    color "#eef5ff"  # Barely blue tint
    
style supervisor_dialogue is say_dialogue:
    slow_cps 25  # Slightly faster than bot
    color "#fff5f5"  # Barely red tint
    
style boss_dialogue is say_dialogue:
    slow_cps 27  # Slightly faster than supervisor
    color "#fff8f5"  # Very subtle warm tint
    
style angry_dialogue is say_dialogue:
    slow_cps 23  # Almost normal speed
    color "#ffeeee"  # Very subtle pink tint
    
style glitch_dialogue is say_dialogue:
    slow_cps 18  # Slightly slower than default
    color "#f5fff5"  # Very subtle green tint