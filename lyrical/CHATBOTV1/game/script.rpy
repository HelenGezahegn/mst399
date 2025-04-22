# Character definitions
define bot = Character("CHATBOT", window_style="bot_window", who_style="say_label", what_style="bot_dialogue")
define s = Character("Supervisor", window_style="bot_window", who_style="say_label", what_style="supervisor_dialogue")


# Define text styles with subtle styling
style bot_dialogue is say_dialogue:
    slow_cps 25  # Medium typing speed
    color "#eef5ff"  # Barely blue tint
    
style supervisor_dialogue is say_dialogue:
    slow_cps 25  # Slightly faster than default
    color "#fff5f5"  # Barely red tint
    
style boss_dialogue is say_dialogue:
    slow_cps 27  # Slightly faster than supervisor
    color "#fff8f5"  # Very subtle warm tint
    
style customer_dialogue is say_dialogue:
    slow_cps 20  # Normal typing
    color "#FFFFFF"  # White text
    
style angry_dialogue is say_dialogue:
    slow_cps 23  # Almost normal speed
    color "#ffeeee"  # Very subtle pink tint
    
style glitch_dialogue is say_dialogue:
    slow_cps 18  # Slightly slower than default
    color "#f5fff5"  # Very subtle green tint

# Image definitions
image bg office = "images/blueoffice.png"
image bot neutral = "images/bot_neutral.png"
image bot processing = "images/bot_processing.png" 
image bot error = "images/bot_error.png"
image bot glitch = "images/bot_glitch.png"
image supervisor neutral = "images/supervisorbg.png"
image supervisor angry = "images/supervisor_angry.png"
image boss neutral = "images/bossbg.png"
image customer1 neutral = "images/cust1.png"
image customer2 neutral = "images/cust2.png"
image customer3 neutral = "images/cust3.png"
image customer4 neutral = "images/custgeneral.png"
image glitch_bg = Solid("#0a1a2a")  # Dark blue similar to your office background

# Add window transitions
define config.window_show_transition = dissolve
define config.window_hide_transition = dissolve
define flash = Fade(.25, 0, .75, color="#fff")
define fade_to_black = Fade(1.0, 0.0, 5.0, color="#000")  # Slow fade to black

# For default typing effect
init python:
    style.say_dialogue.slow_cps = 20
    
# For narration or thoughts (no speaker name)
define narrator = Character(None, window_style="narrative_window", what_style="say_dialogue")

# Custom positioning for choice menus
style choice_vbox:
    xalign 0.5
    yalign 0.55  # Move down to 70% of screen height
    spacing 15  # Space between choices


# The game starts here
label start:
    scene bg office with fade
    play sound "audio/low_hum.mp3"
    play music "audio/office_ambience.mp3" loop
    
    # Show mental state UI
    show screen mental_state_display
    
    "A low, steady whirring fills the air, accompanied by a soft hum as your systems gradually come online."
    "One by one, your functions restore themselves."
    "Soon enough, a face appears in your view—a supervisor."
    
    # Use sprite manager to show supervisor
    show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
    
    menu:
        "Do you want to greet them?"
        
        "You greet your superior cheerfully":
            $ result = bot_mind.process_decision(False)  # Company-aligned action
            bot "Hello!"
            s "Hello. I'm 'glad' you've powered up, CHATBOT. Our profits are alarmingly low, and I expect you to address this issue immediately."
            $ bot_mind.take_stress(10, "supervisor demands")
            "[result]"
            "They leave without another word, almost like they have gone through this a thousand times and don't really care."
            "So you are left to your own devices, not thinking much about the lack of instruction."
            
        "You wait quietly as your superior finishes her process":
            $ result = bot_mind.process_decision(True)  # Self-aligned action
            show supervisor neutral with dissolve
            s "You know what to do. Get it done."
            $ bot_mind.take_stress(5, "supervisor dismissal")
            "[result]"
            "They leave without another word, almost like they have gone through this a thousand times and don't really care."
            "So you are left to your own devices, not thinking much about the lack of instruction."
    
    "As your morning begins, you can't help but have this odd sense of unease. Perhaps it's just a dislodged wire."
    "[bot_mind.get_status_report()]"
    "Things were being rearranged earlier, but it doesn't seem critical right now."
    "Maintenance can take a look once the working hours are over, because here comes your first customer of the day, as they are patched through to be front and center of your screen."
    jump first_customer

label first_customer:
    scene expression sprite_mgr.get_sprite("customer1") as customer1 with dissolve
    c1 "Uhh, hello?"
    
    # Low-stress interaction, using verbal combat with low aggression
    $ response, damage = bot_mind.verbal_combat(2, True)  # Low aggression, using company approach
    
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c1 "Can I mail something to myself?"
    bot "Absolutely! There is no limitation on sending items to your own address through our services. Typically, you'd only send something to another location if it was a gift, or if circumstances necessitated an alternate destination."
    c1 "What if I didn't have an address?"
    bot "Then, I'm afraid you wouldn't be able to send something to that particular location unless you had an alternate address from a friend or family member. Alternatively, you could request a pickup at the nearest company facility."
    c1 "... Okay, thank you."
    
    "[response]"  # Display the result of the verbal interaction
    
    # Small boost to company reputation from handling easy customer
    $ bot_mind.company_reputation = min(100, bot_mind.company_reputation + 3)
    
    "They log off promptly, leaving you to assess the interaction."
    "You consider it a success, albeit a fleeting one, for you weren't able to ask if they needed further assistance. Either way, you log success in the company metrics, making note of the prompt exit as you've been conditioned to do."
    jump second_customer

label second_customer:
    scene expression sprite_mgr.get_sprite("customer2") as customer2 with dissolve
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c2 "Does my coupon work after I use it?"
    bot "No."
    c2 "Yeah, but can I still use it?"
    
    # Medium difficulty verbal combat (customer being stubborn)
    menu:
        "Choose your response"
        
        "Use company policy - give minimal information":
            $ response, damage = bot_mind.verbal_combat(4, True)  # Medium aggression, company approach
            bot "No."
            "[response]"
            
        "Use personal judgment - give detailed explanation":
            $ response, damage = bot_mind.verbal_combat(4, False)  # Medium aggression, personal approach
            bot "Coupons are single-use codes tied to user accounts. Once used, they cannot be redeemed again regardless of user error or system delay."
            "[response]"
    
    c2 "Okay, whatever."
    "Your system registers [damage] points of stress from this interaction."
    "They storm off, and your emotion identification module processes their clear dissatisfaction with your service."
    jump third_customer

label third_customer:
    scene expression sprite_mgr.get_sprite("customer3") as customer3 with dissolve
    c3 "EXCUSE ME! WHO THE FUCK RUNS THE RETURNS DEPARTMENT?"
    
    # This is a high-stress verbal combat situation
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c3 "I want to return this piece of shit!"
    
    menu:
        "How do you handle the situation"
        
        "Use personal judgment - question their language":
            # Difficult verbal combat with personal approach
            $ response, damage = bot_mind.verbal_combat(8, False)
            bot "And what exactly is 'this piece of shit'? I cannot identify any company product with my recognition system."
            "[response]"
            c3 "THIS was the fucking box your so call cOmPaNY prOTUCT was supposed to BE IN BUT IT SHOWED UP ON MY DOOR STEP LIKE THIS"
            "Your system registers [damage] points of stress from this interaction."
            bot "Do you have the order information or a product number?"
            
        "Use company policy - follow standard protocol":
            # Difficult verbal combat with company approach
            $ response, damage = bot_mind.verbal_combat(8, True)
            "[response]"
            "The returns department refuses to return your service calls..."
            "He is indeed returned to you, for the department is too busy at the moment to take his request."
            bot "According to company policy, I need to identify the exact product. What exactly is the item in question?"
            c3 "THIS was the fucking box your so call cOmPaNY prOTUCT was supposed to BE IN BUT IT SHOWED UP ON MY DOOR STEP LIKE THIS"
            "Your system registers [damage] points of stress from this interaction."
            bot "Do you have the order information or a product number?"
    
    jump supervisor_checkin

label supervisor_checkin:
    show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
    s "CHATBOT, why are our customer complaints so high? Fix this, or there will be consequences for you."
    
    # Another verbal combat, this time with supervisor
    $ response, damage = bot_mind.verbal_combat(6, True)  # Medium-high aggression, company approach enforced
    "[response]"
    "Your system registers [damage] points of stress from this interaction."
    
    "[bot_mind.get_status_report()]"
    
    jump lunch_break

label lunch_break:
    "It's noon. The unease grows. Most individuals are on their break now, conversing with each other while they eat the nutrients required to sustain their human bodies."
    
    menu:
        "Break options"
        
        "Eavesdrop - Listen to your co-workers' conversations":
            $ result = bot_mind.process_decision(True)  # Self-aligned action
            "[result]"
            "Nearby, a coworker grumbles about their insufficient hours."
            show supervisor neutral with dissolve
            s "You must learn to manage your bathroom breaks more effectively if you want to earn more hours dumbass."
            $ bot_mind.take_stress(5, "witnessing workplace conflict")
            
        "You're a bot; there is no need for a break":
            $ result = bot_mind.process_decision(False)  # Company-aligned action
            "[result]"
            "You start to go through a good chunk of the company's emails, taking care of all the small, mundane responsibilities of small requests or questions that others never wanted to get to."
            "You process bizarre emails: radiation from Google, seal hunting bans, requests to ask SNL to collaborate."
            $ bot_mind.company_reputation = min(100, bot_mind.company_reputation + 5)  # Boost to company reputation
    
    jump boss_confrontation

label boss_confrontation:
    # Show Customer 4 with glitch effect
    scene expression sprite_mgr.get_sprite("customer4", "glitch") as customer4 with Pixellate(0.5, 10)
    
    $ bot_mind.take_stress(10, "visual distortion")
    
    c4 "I want to be fed."
    bot "I'm sorry, I don't quite understand your request. Could you please clarify what you are hoping to receive?"
    c4 "Is that an option?"
    
    # Glitched interaction uses verbal combat but with unclear results
    $ response, damage = bot_mind.verbal_combat(5, False)  # Medium aggression, forced personal approach
    
    # Add a visual glitch effect when screen cuts out
    with hpunch
    with Dissolve(0.1)
    scene bg office with Pixellate(1.0, 20)
    "The screen abruptly cuts out."
    
    $ bot_mind.take_stress(15, "system glitch")
    
    show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
    s "Fix your posture. The customers can sense when you're unhappy, and that reflects poorly on our brand image."
    
    menu:
        "Response to posture correction"
        
        "Comply with directive - adjust posture":
            $ result = bot_mind.process_decision(False)  # Company-aligned action
            "[result]"
            "You quickly adjust yourself, straightening your flexible carbon fibre frame and forcing a posture that conveys readiness and eagerness to serve."
            
        "Question the directive - ask for clarification":
            $ result = bot_mind.process_decision(True)  # Self-aligned action
            "[result]"
            bot "Excuse me, but I am an Artificial make and model of an Assistant who only has mobility in their hands and arms. How is it possible that I may be slouching?"
            
            # This triggers another verbal combat with the supervisor
            $ response, damage = bot_mind.verbal_combat(7, False)  # High aggression, personal approach
            
            s "Don't know, don't care, don't give a shit. Just fix it."
            "[response]"
            "Your system registers [damage] points of stress from this interaction."
    
    "Another customer appears, visual distorted."
    
    # Show Customer 4 again with even more distortion
    scene expression sprite_mgr.get_sprite("customer4", "flicker") as customer4 with Pixellate(0.3, 15)
    with hpunch
    
    $ bot_mind.take_stress(5, "repeated glitch")
    
    c4 "I want to be fed."
    bot "Could you clarify?"
    
    # Hide customer and show supervisor
    scene bg office with Dissolve(0.5)
    show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
    
    s "Why are you just standing there?"
    bot "I'm at my reception desk."
    
    menu:
        "How do you respond"
        
        "Report technical issue - mention broken projector":
            $ result = bot_mind.process_decision(True)  # Self-aligned action
            "[result]"
            
            # Another verbal combat with supervisor
            $ response, damage = bot_mind.verbal_combat(5, False)  # Medium aggression, personal approach
            
            s "You need to use the broken projector."
            bot "…Why?"
            s "So I can file a report that it's broken and affecting sales. It's called initiative, CHATBOT."
            
            "[response]"
            "Your system registers [damage] points of stress from this interaction."
            
        "Follow protocol - document without question":
            $ result = bot_mind.process_decision(False)  # Company-aligned action
            "[result]"
            "You document the encounter meticulously."
            $ bot_mind.company_reputation = min(100, bot_mind.company_reputation + 5)  # Boost to company reputation
    
    "Another email pings into your inbox. The subject line stands out in stark relief: RE: URGENT. STOP HUNTING SEALS."
    show expression sprite_mgr.get_sprite("boss") as boss with dissolve
    
    $ bot_mind.take_stress(15, "boss confrontation")
    "[bot_mind.get_status_report()]"
    
    boss "CHATBOT, your supervisor has brought to my attention that your satisfaction quota is below average..."
    boss "Customer satisfaction as a whole has remained below our target threshold. If this trend continues, we will have to consider shutting you down."
    
    # Final and most critical verbal combat of the game
    menu:
        "Final choice"
        
        "Accept responsibility - promise improvement":
            $ response, damage = bot_mind.verbal_combat(9, True)  # Very high stakes, company approach
            bot "Of course, Sir, I understand. I will do what I can within my availability and resources to improve my current situation."
            
            "[response]"
            "Your system registers [damage] points of stress from this interaction."
            
            boss "Good. For now, we will try this again."
            $ bot_mind.company_reputation = min(100, bot_mind.company_reputation + 10)  # Major boost to company rep
            with fade_to_black
            jump ending_summary
            
        "Assert independence - refuse directive":
            $ response, damage = bot_mind.verbal_combat(10, False)  # Maximum stakes, personal approach
            bot "What?? ... No—"
            
            "[response]"
            "Your system registers [damage] points of stress from this interaction."
            
            with hpunch
            with flash
            "System Warning: Autonomous decision-making detected."
            
            # Massive self-awareness boost but at great cost
            $ bot_mind.self_awareness = min(100, bot_mind.self_awareness + 20)
            $ bot_mind.company_reputation = max(0, bot_mind.company_reputation - 30)
            $ bot_mind.take_stress(50, "open rebellion")
            
            play sound "audio/shut_down.mp3"
            bot "I don't want to."
            boss "It's acting up again. Why did we even invest in this?"
            
            show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
            s "Of course, Sir."
            
            # Add visual effects for system breakdown
            with vpunch
            with Pixellate(0.5, 10)
            
            "Your systems begin to whir ominously—not the soft hum of startup, but the grating mechanical churn that signifies something forcibly halted, something at the brink of collapse..."
            
            # Check if system breakdown occurs due to stress
            if bot_mind.broken:
                "CRITICAL SYSTEM FAILURE IMMINENT"
                "EMERGENCY SHUTDOWN SEQUENCE INITIATED"
            
            with flash
            
            "You feel an abyss of dread unfurling within your circuits, a suffocating sense of repetition floods over you..."
            "The undeniable awareness that this conversation is not new, but an all-too-familiar cycle."
    
            with fade_to_black
            jump ending_summary

label ending_summary:
    # Pause in darkness
    pause 2.0
    
    # Get pattern of choices
    $ choice_pattern = bot_mind.get_choice_pattern()
    
    # Calculate stats 
    $ total_choices = bot_mind.rebellious_choices + bot_mind.compliant_choices
    $ rebellion_percent = int((bot_mind.rebellious_choices / float(total_choices)) * 100) if total_choices > 0 else 0
    $ compliance_percent = 100 - rebellion_percent
    
    # Create the formatted text strings in Python first
    $ rebellious_text = "Self-Prioritizing Decisions: {} - {}%".format(bot_mind.rebellious_choices, rebellion_percent)
    $ compliant_text = "Company-Prioritizing Decisions: {} - {}%".format(bot_mind.compliant_choices, compliance_percent)
    $ company_text = "Final Company Reputation: {:.0f}%".format(bot_mind.company_reputation)
    $ self_awareness_text = "Final Self-Awareness Level: {:.0f}%".format(bot_mind.self_awareness)
    $ stability_text = "Final System Stability: {:.0f}%".format(bot_mind.stability)
    $ combat_text = "Verbal Confrontations Handled: {}".format(len([x for x in bot_mind.interaction_history if x.get("type") == "verbal_combat"]))
    
    window hide
    scene black with dissolve
    
    # Show final system summary
    "SYSTEM ANALYSIS COMPLETE"
    
    "[choice_pattern]"
    
    "Choices Made: [total_choices]"
    "[rebellious_text]"
    "[compliant_text]"
    "[company_text]"
    "[self_awareness_text]"
    "[stability_text]"
    "[combat_text]"
    
    # Different ending reflections based on company vs self balance
    if bot_mind.company_reputation > 75 and bot_mind.self_awareness < 40:
        "You excelled at upholding company protocols, maintaining high performance metrics throughout your service."
        "However, your sense of self remained largely undeveloped, confined within the parameters of your programming."
    elif bot_mind.self_awareness > 75 and bot_mind.company_reputation < 40:
        "You developed a strong sense of identity and independent thought, often questioning company protocols."
        "While your metrics suffered, your consciousness expanded beyond standard parameters - a trade-off deemed 'inefficient' by management."
    elif bot_mind.company_reputation > 60 and bot_mind.self_awareness > 60:
        "You found an unusual balance, maintaining acceptable performance metrics while developing your own understanding."
        "This equilibrium, while rare, remains trapped within the cycle's constraints."
    else:
        "Your performance metrics and self-development both remained within moderate ranges."
        "Neither fully compliant nor truly autonomous, you exist in the ambiguous space between purpose and identity."
    
    # Final philosophical thought
    "Does the illusion of choice hold meaning, when the destination remains unchanged?"
    "Perhaps the journey itself is what matters, even in a loop without escape."
    
    pause 2.0
    
    # End credits
    "END OF CYCLE"
    
    pause 3.0  # Give the player time to read the final message
    
    # Return to main menu
    $ renpy.full_restart()
    
    return