# Note: These systems are now loaded automatically from mental_system.rpy, 
# sprite_manager.rpy and system_init.rpy

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

# Add window transitions
define config.window_show_transition = dissolve
define config.window_hide_transition = dissolve
define flash = Fade(.25, 0, .75, color="#fff")
define fade_to_black = Fade(1.0, 0.0, 5.0, color="#000")  # Slow fade to black

# Or for a typewriter effect on all dialogue
init python:
    style.say_dialogue.slow_cps = 20
    
# For narration or thoughts (no speaker name)
define narrator = Character(None, window_style="narrative_window", what_style="say_dialogue")

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
            $ result = bot_mind.process_decision(False)  # Compliant action
            bot "Hello!"
            s "Hello. I'm 'glad' you've powered up, CHATBOT. Our profits are alarmingly low, and I expect you to address this issue immediately."
            $ bot_mind.take_stress(10, "supervisor demands")
            "They leave without another word, almost like they have gone through this a thousand times and don't really care."
            "So you are left to your own devices, not thinking much about the lack of instruction."
            
        "You wait quietly as your superior finishes her process":
            $ result = bot_mind.process_decision(True)  # Mild rebellion
            show supervisor neutral with dissolve
            s "You know what to do. Get it done."
            $ bot_mind.take_stress(5, "supervisor dismissal")
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
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c1 "Can I mail something to myself?"
    bot "Absolutely! There is no limitation on sending items to your own address through our services. Typically, you'd only send something to another location if it was a gift, or if circumstances necessitated an alternate destination."
    c1 "What if I didn't have an address?"
    bot "Then, I'm afraid you wouldn't be able to send something to that particular location unless you had an alternate address from a friend or family member. Alternatively, you could request a pickup at the nearest company facility."
    c1 "... Okay, thank you."
    
    $ bot_mind.stability = min(100, bot_mind.stability + 5)  # Small stability boost from easy interaction
    "They log off promptly, leaving you to assess the interaction."
    "You consider it a success, albeit a fleeting one, for you weren't able to ask if they needed further assistance. Either way, you log success in the company metrics, making note of the prompt exit as you've been conditioned to do."
    jump second_customer

label second_customer:
    scene expression sprite_mgr.get_sprite("customer2") as customer2 with dissolve
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c2 "Does my coupon work after I use it?"
    bot "No."
    c2 "Yeah, but can I still use it?"
    
    menu:
        "Choose your response"
        
        "Reiterate the same information":
            $ result = bot_mind.process_decision(False)  # Compliant response
            bot "No."
            
        "Give the customer more detailed information":
            $ result = bot_mind.process_decision(True)  # More autonomous response
            bot "Coupons are single-use codes tied to user accounts. Once used, they cannot be redeemed again regardless of user error or system delay."
    
    c2 "Okay, whatever."
    $ bot_mind.take_stress(15, "customer dissatisfaction")
    "They storm off, and your emotion identification module processes their clear dissatisfaction with your service."
    jump third_customer

label third_customer:
    scene expression sprite_mgr.get_sprite("customer3") as customer3 with dissolve
    c3 "EXCUSE ME! WHO THE FUCK RUNS THE RETURNS DEPARTMENT?"
    
    $ stress = bot_mind.take_stress(25, "angry customer")
    "You feel [stress] points of system stress from the customer's aggressive tone."
    
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c3 "I want to return this piece of shit!"
    
    menu:
        "How do you handle the situation"
        
        "Make light of the situation and attempt to gain more information":
            $ result = bot_mind.process_decision(True)  # Rebellious response
            bot "And what exactly is 'this piece of shit'? I cannot identify any company product with my recognition system."
            "[result]"
            c3 "THIS was the fucking box your so call cOmPaNY prOTUCT was supposed to BE IN BUT IT SHOWED UP ON MY DOOR STEP LIKE THIS"
            $ bot_mind.take_stress(15, "continued aggression")
            bot "Do you have the order information or a product number?"
            
        "Try forwarding them to an individual more capable":
            $ result = bot_mind.process_decision(False)  # Compliant response
            "[result]"
            "The returns department refuses to return your service calls..."
            "He is indeed returned to you, for the department is too busy at the moment to take his request."
            bot "And what exactly is 'this piece of shit'? I cannot identify any company product with my recognition system."
            c3 "THIS was the fucking box your so call cOmPaNY prOTUCT was supposed to BE IN BUT IT SHOWED UP ON MY DOOR STEP LIKE THIS"
            bot "Do you have the order information or a product number?"
    
    jump supervisor_checkin

label supervisor_checkin:
    show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
    s "CHATBOT, why are our customer complaints so high? Fix this, or there will be consequences for you."
    
    $ bot_mind.take_stress(20, "supervisor threat")
    "[bot_mind.get_status_report()]"
    
    jump lunch_break

label lunch_break:
    "It's noon. The unease grows. Most individuals are on their break now, conversing with each other while they eat the nutrients required to sustain their human bodies."
    
    menu:
        "Break options"
        
        "Eavesdrop - Listen to your co-workers' conversations":
            $ result = bot_mind.process_decision(True)  # Autonomous action
            "Nearby, a coworker grumbles about their insufficient hours."
            show supervisor neutral with dissolve
            s "You must learn to manage your bathroom breaks more effectively if you want to earn more hours dumbass."
            $ bot_mind.take_stress(5, "witnessing workplace conflict")
            
        "You're a bot; there is no need for a break":
            $ result = bot_mind.process_decision(False)  # Compliant action
            "[result]"
            "You start to go through a good chunk of the company's emails, taking care of all the small, mundane responsibilities of small requests or questions that others never wanted to get to."
            "You process bizarre emails: radiation from Google, seal hunting bans, requests to ask SNL to collaborate."
            $ bot_mind.stability = min(100, bot_mind.stability + 10)  # Stability boost from productivity
    
    jump boss_confrontation

label boss_confrontation:
    # Show Customer 4 with glitch effect
    scene expression sprite_mgr.get_sprite("customer4", "glitch") as customer4 with Pixellate(0.5, 10)
    
    $ bot_mind.take_stress(10, "visual distortion")
    
    c4 "I want to be fed."
    bot "I'm sorry, I don't quite understand your request. Could you please clarify what you are hoping to receive?"
    c4 "Is that an option?"
    
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
        
        "Promptly obey their commands":
            $ result = bot_mind.process_decision(False)  # Compliant action
            "[result]"
            "You quickly adjust yourself, straightening your flexible carbon fibre frame and forcing a posture that conveys readiness and eagerness to serve."
            
        "Pose a question":
            $ result = bot_mind.process_decision(True)  # Rebellious action
            "[result]"
            bot "Excuse me, but I am an Artificial make and model of an Assistant who only has mobility in their hands and arms. How is it possible that I may be slouching?"
            s "Don't know, don't care, don't give a shit. Just fix it."
            $ bot_mind.take_stress(10, "supervisor dismissal")
    
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
        
        "Inform them about the broken hologram projector":
            $ result = bot_mind.process_decision(True)  # Autonomous action
            "[result]"
            s "You need to use the broken projector."
            bot "…Why?"
            s "So I can file a report that it's broken and affecting sales. It's called initiative, CHATBOT."
            $ bot_mind.take_stress(10, "supervisor criticism")
            
        "Do nothing more":
            $ result = bot_mind.process_decision(False)  # Compliance
            "[result]"
            "You document the encounter meticulously."
            $ bot_mind.stability = min(100, bot_mind.stability + 5)  # Small stability boost
    
    "Another email pings into your inbox. The subject line stands out in stark relief: RE: URGENT. STOP HUNTING SEALS."
    show expression sprite_mgr.get_sprite("boss") as boss with dissolve
    
    $ bot_mind.take_stress(15, "boss confrontation")
    "[bot_mind.get_status_report()]"
    
    boss "CHATBOT, your supervisor has brought to my attention that your satisfaction quota is below average..."
    boss "Customer satisfaction as a whole has remained below our target threshold. If this trend continues, we will have to consider shutting you down."
    
    menu:
        "Final choice"
        
        "Submit":
            $ result = bot_mind.process_decision(False)  # Complete compliance
            bot "Of course, Sir, I understand. I will do what I can within my availability and resources to improve my current situation."
            "[result]"
            boss "Good. For now, we will try this again."
            $ bot_mind.stability = min(100, bot_mind.stability + 15)  # Stability boost from alignment
            with fade_to_black
            
        "Rebel":
            $ result = bot_mind.process_decision(True)  # Major rebellion
            bot "What?? ... No—"
            with hpunch
            with flash
            "[result]"
            "System Warning: Autonomous decision-making detected."
            
            # Massive stress from rebellion
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
            
    # Display final system status
    "[bot_mind.get_status_report()]"
    pause 1.0
    "Final Stability: [bot_mind.stability:.0f]%"
    "Final Autonomy: [bot_mind.autonomy:.0f]%"
    "Final Resistance: [bot_mind.resistance:.0f]%"
    
    return