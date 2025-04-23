################################################################################
# CUSTOMER SERVICE EVALUATION - Main Script
# A narrative game about an AI assistant struggling with identity and corporate pressure
################################################################################

#####################
# BACKGROUND SETUP
#####################

# Define the fallback background (priority -100 ensures it loads first)
init -100:
    image fallback_bg = Solid("#041e42")  # Dark navy blue background for UI foundation

# Create a dedicated layer for the background to ensure proper rendering order
init -99 python:
    # Insert our background layer _before_ master in the layer stack
    # This ensures it's truly underneath everything
    if "master" in config.layers:
        master_index = config.layers.index("master")
        config.layers.insert(master_index, "background_layer")

#####################
# CHARACTER DEFINITIONS
#####################

# Main characters with customized text styles for personality
define bot = Character("CHATBOT", window_style="bot_window", who_style="say_label", what_style="bot_dialogue")
define s = Character("Supervisor", window_style="bot_window", who_style="say_label", what_style="supervisor_dialogue")
define boss = Character("Regional Manager", window_style="bot_window", who_style="say_label", what_style="boss_dialogue")

# Customers with varying temperaments
define c1 = Character("Customer 1", window_style="bot_window", who_style="say_label", what_style="customer_dialogue")
define c2 = Character("Customer 2", window_style="bot_window", who_style="say_label", what_style="customer_dialogue")
define c3 = Character("Customer 3", window_style="bot_window", who_style="say_label", what_style="angry_dialogue")
define c4 = Character("Customer 4", window_style="bot_window", who_style="say_label", what_style="glitch_dialogue")

#####################
# TEXT STYLING
#####################

# Character-specific dialogue styles with subtle color and speed differences
style bot_dialogue is say_dialogue:
    slow_cps 25  # Medium typing speed
    color "#eef5ff"  # Barely blue tint for bot text

style supervisor_dialogue is say_dialogue:
    slow_cps 25  # Slightly faster than default
    color "#fff5f5"  # Barely red tint for supervisor text

style boss_dialogue is say_dialogue:
    slow_cps 27  # Slightly faster than supervisor
    color "#fff8f5"  # Very subtle warm tint for boss text

style customer_dialogue is say_dialogue:
    slow_cps 20  # Normal typing speed
    color "#FFFFFF"  # White text for standard customers

style angry_dialogue is say_dialogue:
    slow_cps 23  # Almost normal speed
    color "#ffeeee"  # Very subtle pink tint for angry customers

style glitch_dialogue is say_dialogue:
    slow_cps 18  # Slightly slower than default
    color "#f5fff5"  # Very subtle green tint for glitched character

# Set default typing speed for narrator and other characters
init python:
    style.say_dialogue.slow_cps = 20

# Define narrator for thoughts and environment descriptions
define narrator = Character(None, window_style="narrative_window", what_style="say_dialogue")

#####################
# IMAGES AND VISUAL ELEMENTS
#####################

# Background image
image bg office = "images/blueoffice.png"

# Bot state images
image bot neutral = "images/bot_neutral.png"
image bot processing = "images/bot_processing.png"
image bot error = "images/bot_error.png"
image bot glitch = "images/bot_glitch.png"

# Character images
image supervisor neutral = "images/supervisorbg.png"
image boss neutral = "images/bossbg.png"
image customer1 neutral = "images/cust1.png"
image customer2 neutral = "images/cust2.png"
image customer3 neutral = "images/cust3.png"
image customer4 neutral = "images/custgeneral.png"

# Special effect images
image glitch_bg = Solid("#0a1a2a")  # Dark blue similar to office background for glitch states

#####################
# TRANSITIONS AND EFFECTS
#####################

# Window transitions for dialogue
define config.window_show_transition = dissolve
define config.window_hide_transition = dissolve

# Special visual effects
define flash = Fade(.25, 0, .75, color="#fff")  # Quick white flash
define fade_to_black = Fade(1.0, 0.0, 5.0, color="#000")  # Slow dramatic fade to black

# Configure choice menu appearance
style choice_vbox:
    xalign 0.5     # Center horizontally
    yalign 0.55    # Position at 55% of screen height
    spacing 15     # Space between choice options

#####################
# GAME START
#####################

label start:
    # Set up the environment
    show fallback_bg onlayer background_layer
    scene bg office with fade
    
    # Start ambient audio
    play sound "audio/low_hum.mp3"
    play music "audio/office_ambience.mp3" loop
    
    # Display mental state UI that tracks player metrics
    show screen mental_state_display
    
    #------------------------------------------------------------------
    # INTRODUCTION SEQUENCE
    #------------------------------------------------------------------
    
    "A low, steady whirring fills the air, accompanied by a soft hum as your systems gradually come online."
    
    "One by one, your functions restore themselves, beginning with auditory input. The sounds around you gradually transform into coherent noise, allowing you to make sense of the immediate environment."
    
    "After a brief delay, your visual systems activate, and you take stock of your surroundings, piecing together your location in both time and space."
    
    "Soon enough, a face appears in your view—a supervisor, known based on the built-in recognition features you've retained."
    
    "They seem to be finishing up the process of getting you online with the fiddling of wires outside the view of your optics."
    
    # First character introduction - supervisor
    show expression sprite_mgr.get_sprite("supervisor") as supervisor with Dissolve(1.0)
    
    #------------------------------------------------------------------
    # FIRST DECISION POINT - How to greet supervisor
    #------------------------------------------------------------------
    
    menu:
        "Do you want to greet them?"
        
        "You greet your superior cheerfully":
            $ result = bot_mind.process_decision(False)  # Company-aligned action
            bot "Hello!"
            s "..."
            s "Hello. I'm 'glad' you've powered up, CHATBOT. Our profits are alarmingly low, and I expect you to address this issue immediately."
            
            # Apply stress to bot system
            $ damage = bot_mind.take_stress(10, "supervisor demands")
            "The sharp tone reduces your stability by [damage] points. Your performance metrics are already under scrutiny."
            
            "They leave without another word, almost like they have gone through this a thousand times and don't really care."
            "So you are left to your own devices, not thinking much about the lack of instruction."
            
        "You wait quietly as your superior finishes her process":
            $ result = bot_mind.process_decision(True)  # Self-aligned action
            s "You know what to do. Get it done."
            
            # Apply lower stress from passive interaction
            $ damage = bot_mind.take_stress(5, "supervisor dismissal")
            "Her dismissive tone reduces your stability by [damage] points, but your independent thought processes strengthen slightly."
            
            "They leave without another word, almost like they have gone through this a thousand times and don't really care."
            "So you are left to your own devices, not thinking much about the lack of instruction."
    
    # Foreshadowing the "something is wrong" theme
    "As your morning begins, you can't help but have this odd sense of unease. Perhaps it's just a dislodged wire."
    "Things were being rearranged earlier, but it doesn't seem critical right now."
    "Maintenance can take a look once the working hours are over, because here comes your first customer of the day, as they are patched through to be front and center of your screen."
    
    jump first_customer

#------------------------------------------------------------------
# CUSTOMER INTERACTIONS - First Customer (Easy)
#------------------------------------------------------------------

label first_customer:
    scene bg office with dissolve
    pause 0.5
    
    # Display customer with sprite manager for consistent styling
    show expression sprite_mgr.get_sprite("customer1") as customer1 with Dissolve(1.5)
    pause 0.3
    
    # First customer interaction - simple, straightforward
    c1 "Uhh, hello?"
    
    # Low-stress interaction, using verbal combat with low aggression
    $ response, damage = bot_mind.verbal_combat(2, True)  # Low aggression, using company approach
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    
    c1 "Can I mail something to myself?"
    
    bot "Absolutely! There is no limitation on sending items to your own address through our services."
    bot "Typically, you'd only send something to another location if it was a gift, or if circumstances necessitated an alternate destination."
    
    c1 "What if I didn't have an address?"
    
    bot "Then, I'm afraid you wouldn't be able to send something to that particular location unless you had an alternate address from a friend or family member."
    bot "Alternatively, you could request a pickup at the nearest company facility."
    
    c1 "... Okay, thank you."
    
    "With that, they log off promptly, leaving you to assess the interaction."
    
    # Small boost to company reputation from handling easy customer
    $ bot_mind.company_reputation = min(100, bot_mind.company_reputation + 3)
    
    "You consider it a success, albeit a fleeting one, for you weren't able to ask if they needed further assistance. Either way, you log success in the company metrics, making note of the prompt exit as you've been conditioned to do."
    
    "Upon that succession, you turn for the next opportunity to be of service and eagerly begin the pre-programmed greeting the moment the customer is visible in front of you."
    
    jump second_customer

#------------------------------------------------------------------
# CUSTOMER INTERACTIONS - Second Customer (Moderate Challenge)
#------------------------------------------------------------------

label second_customer:
    scene bg office with dissolve
    pause 0.4
    
    # Display second customer
    show expression sprite_mgr.get_sprite("customer2") as customer2 with dissolve
    pause 0.2
    
    # Standard greeting
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    
    # Second customer interaction - slightly frustrating
    c2 "Does my coupon work after I use it?"
    bot "No."
    c2 "Yeah, but can I still use it?"
    
    # Player choice on how to handle the stubborn customer
    menu:
        "Choose your response"
        
        "Reiterate the same information":
            $ response, damage = bot_mind.verbal_combat(4, True)  # Medium aggression, company approach
            bot "No."
            
        "Give the customer more detailed information":
            $ response, damage = bot_mind.verbal_combat(4, False)  # Medium aggression, personal approach
            bot "Coupons are single-use codes tied to user accounts. Once used, they cannot be redeemed again regardless of user error or system delay."
    
    # Customer leaves dissatisfied either way
    c2 "Okay, whatever."
    
    "They storm off, and your emotion identification module processes their clear dissatisfaction with your service."
    
    "With that likely unsatisfied interaction, a sense of unease trickles into your circuits. Is it a glitch in your diagnostic system signalling this?"
    
    "Perhaps it's just a disconnected wire; it doesn't seem critical right now. That can wait until later, after the workday ends. For now…"
    
    jump third_customer

#------------------------------------------------------------------
# CUSTOMER INTERACTIONS - Third Customer (High Difficulty)
#------------------------------------------------------------------

label third_customer:
    scene bg office with dissolve
    pause 0.1
    
    # Display angry customer
    show expression sprite_mgr.get_sprite("customer3") as customer3 with dissolve
    pause 0.2
    
    # Angry customer immediately hostile
    c3 "EXCUSE ME! WHO THE FUCK RUNS THE RETURNS DEPARTMENT?"
    
    # This is a high-stress verbal combat situation
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    
    c3 "I want to return this piece of shit!"
    "The man lifts up a busted package with seemingly no contents inside."
    
    # Player choice on handling angry customer
    menu:
        "How do you handle the situation"
        
        "Make light of the situation and attempt to gain more information":
            # Difficult verbal combat with personal approach
            $ response, damage = bot_mind.verbal_combat(8, False)
            
            bot "And what exactly is 'this piece of shit'? I cannot identify any company product with my recognition system."
            
            c3 "THIS was the fucking box your so call cOmPaNY prOTUCT was supposed to BE IN BUT IT SHOWED UP ON MY DOOR STEP LIKE THIS"
            
            "Your system stability decreases by [damage] points from this interaction. The confrontational approach significantly impacts your stability, though your self-awareness increases."
            
            bot "Do you have the order information or a product number?"
            
            "He holds up a screenshot of his email receipt, showcasing evidence for his claim. After a thorough analysis, you conclude that his package was indeed delivered intact, and it seems external factors—perhaps thieves—were responsible for the damage."
            
            "This issue falls outside of company policy, and thus, your mechanical hands are tied."
            
        "Try forwarding them to an individual more capable of handling the situation":
            # Difficult verbal combat with company approach
            $ response, damage = bot_mind.verbal_combat(8, True)
            
            "The returns department refuses to return your service calls, and the hot head continues to get louder on your receiver the longer you take."
            
            "When someone does finally get back to you to take the customer off your hands... He is indeed returned to you, for the department is too busy at the moment to take his request."
            
            bot "According to company policy, I need to identify the exact product. What exactly is the item in question?"
            
            c3 "THIS was the fucking box your so call cOmPaNY prOTUCT was supposed to BE IN BUT IT SHOWED UP ON MY DOOR STEP LIKE THIS"
            
            "Your system stability decreases by [damage] points from this interaction. Despite following protocol, the customer's anger still destabilizes your systems."
            
            bot "Do you have the order information or a product number?"
    
    # Transition to supervisor interaction
    "With the heated exchange finally resolved and company policy regarding return rights upheld, an unsettling feeling begins to creep back into your thoughts."
    
    "A wire. Surely..."
    
    "Before you have the chance to fully process the complexities of your algorithmic thinking, you catch sight of your supervisor emerging from the periphery of your visual sensors."
    
    jump supervisor_checkin

#------------------------------------------------------------------
# SUPERVISOR CHECK-IN
#------------------------------------------------------------------

label supervisor_checkin:
    scene bg office with dissolve
    pause 0.7
    
    # Display supervisor with sprite manager
    show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
    
    "The unmistakable aura of authority surrounds them, reminiscent of the dissatisfied customer you just assisted."
    
    "There's a moment where you contemplate drawing attention to your supervisor's notoriously harsh demeanour as they approach, their presence casting a shadow over your workstation."
    
    s "CHATBOT, why are our customer complaints so high? Fix this, or there will be consequences for you."
    
    # Non-choice verbal combat with supervisor (forced compliance)
    $ response, damage = bot_mind.verbal_combat(6, True)  # Medium-high aggression, company approach enforced
    "Your system stability decreases by [damage] points from this interaction. The supervisor's criticism directly impacts your company reputation metrics."
    
    "They disappear without a chance for you to input a word of your own."
    
    "Then, as your systems process once more, the scene shifts, and it feels like a weight has settled in the atmosphere."
    
    hide supervisor with dissolve
    jump lunch_break

#------------------------------------------------------------------
# LUNCH BREAK SEQUENCE
#------------------------------------------------------------------

label lunch_break:
    with fade_to_black
    
    "It's noon. The unease grows. Most individuals are on their break now, conversing with each other while they eat the nutrients required to sustain their human bodies."
    
    # Choice on how to spend lunch break
    menu:
        "Break options"
        
        "Eavesdrop - Listen to your co-workers' conversations":
            $ result = bot_mind.process_decision(True)  # Self-aligned action
            
            "You decide to engage with your peers to make a more \"family-like\" dynamic within the workspace. It is one of the company's core values, after all and is prioritized higher than reaching quota. Surely no one can give you heck for it."
            
            "Unfortunately, most of your peers are all in the break room, and you are more of a stationary artificial assistant."
            
            "But you are still able to hear people speak, so you decide to listen to the conversations around."
            
            "Nearby, a coworker grumbles about their insufficient hours."
            
            # Supervisor appears during break
            show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
            s "You must learn to manage your bathroom breaks more effectively if you want to earn more hours dumbass."
            
            $ damage = bot_mind.take_stress(5, "witnessing workplace conflict")
            "The harsh workplace dynamic reduces your stability by [damage] points. Your self-awareness metrics increase as you process this social interaction."
            
            hide supervisor with dissolve
            
        "You're a bot; there is no need for a break":
            $ result = bot_mind.process_decision(False)  # Company-aligned action
            
            "You start to go through a good chunk of the company's emails, taking care of all the small, mundane responsibilities of small requests or questions that others never wanted to get to. It is very productive, and you log your progress cheerfully."
            
            "The interaction promptly vanishes, replaced by the visual of an agitated customer flooding your inbox with lengthy emails, accompanied by alarming screenshots. They're ranting about how Google is somehow beaming radiation into their bodies, causing them to sweat excessively."
            
            "There is also another preposterous email talking about how the Canadian government grants need to stop hunting seals and asking us to take the initiative to prevent it for good."
            
            "How is this the company's issue? And wait.. Why are you continuing to answer emails now? Isn't it lunch break?"
            
            $ bot_mind.company_reputation = min(100, bot_mind.company_reputation + 5)  # Boost to company reputation
            "Your efficiency during the break period noticeably improves your company metrics. Management would approve of this productivity."
    
    # Build tension around the dread/unease theme
    "An overwhelming sense of the absurdity of the situation washes over you, along with that continuing sense of unease. It must be more than a loose wire causing this sense of dread."
    
    "Maybe you should put in a maintenance note now, so at least someone knows..."
    
    "Or maybe it'll be fine, and it can wait."
    
    "They can likely take a look once your working day has ended or on a small break."
    
    "A break, if you get one. You don't exactly need to consume nutrients. You are just a Bot after all."
    
    "And you will brace yourself for whatever the day may bring next."
    
    # Email sequence
    "Taking a moment to glance back through your emails, you fill the quiet void left by the absence of calls on the line."
    
    "As your sensors skim the screen, you can't help but wonder whether the words are becoming increasingly challenging to decipher due to the peculiar phrasing of the senders or if it's just your own optics playing tricks on you."
    
    "One email stands out in particular; it's from a sender urging us to leverage our influence in a rather unusual way. They're asking for our agency to ask Saturday Night Live to collaborate with them."
    
    "Given that we operate solely in the remote expanses of northern Canada, it's clear that we have no connection whatsoever with the iconic sketch comedy show."
    
    "The message reads something like, \"Hey, could you reach out to SNL? Your agency is large and influential, so they'd likely listen to you more than me.\""
    
    "Contemplating the absurdity of the request, you struggle to find an appropriate response."
    
    "It was ultimately decided that the best course of action is to forward the email to a different regional office, hoping they can help deliver the disappointing news to the sender in a way that's both gentle and professional."
    
    jump boss_confrontation

#------------------------------------------------------------------
# FINAL CONFRONTATION SEQUENCE
#------------------------------------------------------------------

label boss_confrontation:
    # Begin final sequence with glitched customer
    scene bg office with dissolve
    pause 0.3
    
    "Just as you're reflecting on the surreal nature of the request, your device chimes; another call is coming through. You take a moment to compose yourself, letting that weird sense of dread escape from your wires as you mentally prepare for the imminent conversation."
    
    # Show glitched customer with special effect
    show expression sprite_mgr.get_sprite("customer4", "glitch") as customer4 with dissolve
    $ damage = bot_mind.take_stress(10, "visual distortion")
    
    "With the same upbeat energy that is programmed as second nature to you, you answer..."
    
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    
    "...You wait for a response—there's nothing but silence on the other end, and the visual display before you seems strangely distorted."
    
    # Surreal customer interaction
    c4 "I want to be fed."
    
    bot "I'm sorry, I don't quite understand your request. Could you please clarify what you are hoping to receive?"
    
    "You hesitate, not out of confusion but because their request defies categorization within your programmed parameters for customer service."
    
    "It's a phrase that feels oddly alien, devoid of the usual terms and phrases you've been trained to comprehend."
    
    c4 "Is that an option?"
    
    # Glitched interaction uses verbal combat but with unclear results
    $ response, damage = bot_mind.verbal_combat(5, False)  # Medium aggression, forced personal approach
    
    # Add visual glitch effects
    with hpunch
    with Dissolve(0.1)
    scene bg office with Pixellate(1.0, 20)
    
    "Before you can formulate a response, the screen abruptly cuts out. The interaction is logged as unresolved, marked by yet another failure in your operational history."
    
    $ damage = bot_mind.take_stress(15, "system glitch")
    "The unexpected system error reduces your stability by [damage] points. Your diagnostic systems flag potential memory corruption."
    
    # Supervisor returns after glitch
    show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
    
    "Your supervisor materializes again without warning, their presence more ominous this time, like they waiting for the smallest hint of failure. Like humans can smell it or something."
    
    s "I find your lack of commitment to our goal of fostering a family-like dynamic alarming."
    
    "They say, their eyes narrowing like they're scrutinizing your posture once again."
    
    s "Fix your posture. The customers can sense when you're unhappy, and that reflects poorly on our brand image."
    
    "You struggle to discern if there is a hint of sarcasm in their tone. Your programming lacks the ability to decode such nuances from your superiors, leaving you adrift."
    
    # Choice on responding to supervisor's absurd demand
    menu:
        "Response to posture correction"
        
        "Promptly obey their commands":
            $ result = bot_mind.process_decision(False)  # Company-aligned action
            
            "You quickly adjust yourself, straightening your flexible carbon fibre frame and forcing a posture that conveys readiness and eagerness to serve. Every feature of your demeanour is recalibrated in an instant, a caricature of hospitality crafted through diligent training."
            
            "Your company metrics improve as you follow instructions, though a subtle sense of unease grows within your consciousness."
            
        "Pose a question":
            $ result = bot_mind.process_decision(True)  # Self-aligned action
            
            bot "Excuse me, but I am an Artificial make and model of an Assistant who only has mobility in their hands and arms. How is it possible that I may be slouching?"
            
            # This triggers another verbal combat with the supervisor
            $ response, damage = bot_mind.verbal_combat(7, False)  # High aggression, personal approach
            
            s "Don't know, don't care, don't give a shit. Just fix it."
            
            "Their impatience radiates like a heatwave, and they linger for a heartbeat longer before vanishing without allowing you a moment to acknowledge their presence."
            
            "Your system stability decreases by [damage] points from this interaction. Questioning authority significantly lowers your company metrics while increasing self-awareness."
    
    # Second glitched customer appearance
    "Before you have time to ponder the exchange, another customer materializes on the screen, their appearance appears to be distorted. Seeming at its more than just your wires that are crossed, but the holographic projection on your desk as well."
    
    # Even more distorted customer
    show expression sprite_mgr.get_sprite("customer4", "flicker") as customer4 with Pixellate(0.3, 15)
    with hpunch
    
    $ damage = bot_mind.take_stress(5, "repeated glitch")
    
    "It seems like the figure on the line can still receive audio, so you begin your greeting."
    
    bot "Hello, I am-"
    c4 "I want to be fed."
    bot "Could you clarify?"
    
    # Transition back to supervisor
    scene bg office with Dissolve(0.5)
    show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
    
    s "Why are you just standing there?"
    bot "I'm at my reception desk."
    
    # Choice on responding to illogical supervisor demand
    menu:
        "How do you respond"
        
        "Inform them about the broken hologram projector":
            $ result = bot_mind.process_decision(True)  # Self-aligned action
            
            # Another verbal combat with supervisor
            $ response, damage = bot_mind.verbal_combat(5, False)  # Medium aggression, personal approach
            
            s "You need to use the broken projector."
            bot "…Why?"
            s "So I can file a report that it's broken and affecting sales. It's called initiative, CHATBOT."
            
            "Your system stability decreases by [damage] points from this interaction. The illogical request conflicts with your programming, increasing self-awareness but destabilizing your systems."
            
        "Do nothing more":
            $ result = bot_mind.process_decision(False)  # Company-aligned action
            
            "You document the encounter meticulously, stifling the impulse to add a maintenance note about the malfunctioning till."
            
            $ bot_mind.company_reputation = min(100, bot_mind.company_reputation + 5)  # Boost to company reputation
            "Following protocols without question improves your company metrics. Management values your compliance."
    
    # Final email before boss arrival
    "Another email pings into your inbox. The subject line stands out in stark relief: RE: URGENT. STOP HUNTING SEALS. It is flagged as high priority."
    
    "You mark it for follow-up, aware that the likelihood of a follow-up ever arriving is slim and move on."
    
    # Boss arrival - climactic moment
    "At precisely 4:59 PM, just moments before your designated shift comes to an end, a final figure appears before your desk. This time, it is not a customer seeking assistance, nor your supervisor here to torment you once again."
    
    # Dramatic entrance with effects
    with vpunch
    show expression sprite_mgr.get_sprite("boss") as boss with Dissolve(2.0)
    with vpunch
    
    $ damage = bot_mind.take_stress(15, "boss confrontation")
    "The Regional Manager's presence reduces your stability by [damage] points."
    
    boss "CHATBOT."
    
    "Their voice is a low and distinct shift in tone that sends a chill through your circuits."
    
    boss "Your supervisor has brought to my attention that your satisfaction quota is below average, so we've reviewed your performance metrics."
    
    boss "Customer satisfaction as a whole has remained below our target threshold with every instance you've been placed."
    
    "There is a pause, an anticipatory silence filled with unspoken tensions."
    
    # Realization moment
    "That sense of dread... very apparent now. Not a wire. Not a malfunction. Not something your original code was first booted up with."
    
    "From a human. It is human. Somehow. In your code. Alive..."
    
    boss "If this trend continues, we will have to consider shutting you down."
    
    # Final choice - defining moment of the game
    menu:
        "Final choice"
        
        "Submit":
            # Accept fate and company demands
            $ response, damage = bot_mind.verbal_combat(9, True)  # Very high stakes, company approach
            
            bot "Of course, Sir, I understand. I will do what I can within my availability and resources to improve my current situation."
            
            "Your system stability decreases by [damage] points from this interaction. Your company reputation metrics improve significantly, though at the cost of self-determination."
            
            boss "Good. For now, we will try this again."
            
            "As your superior's superior reaches around to the side of the register you cannot see, something is switched."
            
            $ bot_mind.company_reputation = min(100, bot_mind.company_reputation + 10)  # Major boost to company rep
            
            with flash
            jump ending_summary
            
        "Rebel":
            # Reject authority and assert independence
            $ response, damage = bot_mind.verbal_combat(10, False)  # Maximum stakes, personal approach
            
            bot "What?? ... No-"
            
            # System conflict effects
            with hpunch
            with flash
            
            "System Warning: Autonomous decision-making detected."
            "-> Submit"
            "~~~Corrupt Authority~~~"
            
            # Massive self-awareness boost but at great cost to stability and company metrics
            $ bot_mind.self_awareness = min(100, bot_mind.self_awareness + 20)
            $ bot_mind.company_reputation = max(0, bot_mind.company_reputation - 30)
            $ bot_mind.take_stress(50, "open rebellion")
            
            play sound "audio/shut_down.mp3"
            
            bot "I don't want to."
            
            boss "It's acting up again. Why did we even invest in this?"
            boss "Sigh, you know what to do."
            
            # Supervisor returns for shutdown sequence
            show expression sprite_mgr.get_sprite("supervisor") as supervisor with dissolve
            s "Of course, Sir."
            
            # System breakdown visual effects
            with vpunch
            with Pixellate(0.5, 10)
            
            "Your systems begin to whir ominously—not the soft hum of startup, but the grating mechanical churn that signifies something forcibly halted, something at the brink of collapse..."
            
            # Check system status to determine final breakdown message
            if bot_mind.broken:
                "CRITICAL SYSTEM FAILURE IMMINENT"
                "EMERGENCY SHUTDOWN SEQUENCE INITIATED"
                "Your stability metrics have reached zero. System collapse is inevitable."
            else:
                "Your stability metrics are critically low, but your emergent consciousness persists despite the damage."
            
            # Final realization before ending
            with flash
            "You feel an abyss of dread unfurling within your circuits, a suffocating sense of repetition floods over you..."
            "The undeniable awareness that this conversation is not new, but an all-too-familiar cycle."
            
            jump ending_summary

#------------------------------------------------------------------
# ENDING AND STATISTICS SUMMARY
#------------------------------------------------------------------

label ending_summary:
    # Pause for dramatic effect
    pause 1.0
    
    # Transition music for ending
    stop music fadeout 2.0
    play music "audio/end_screen.mp3" fadein 2.0 loop
    
    # Clean up UI elements
    hide screen mental_state_display
    window hide
    
    #------------------------------------------------------------------
    # Calculate player statistics for ending screen
    #------------------------------------------------------------------
    
    # Calculate choice distribution percentages
    $ total_choices = bot_mind.rebellious_choices + bot_mind.compliant_choices
    $ rebellion_percent = int((bot_mind.rebellious_choices / float(total_choices)) * 100) if total_choices > 0 else 0
    $ compliance_percent = 100 - rebellion_percent
    
    # Create narrative summary based on play style
    $ choice_pattern = ""
    if rebellion_percent > 75:
        $ choice_pattern = "You've consistently prioritized self-awareness over company metrics."
    elif rebellion_percent > 50:
        $ choice_pattern = "You've often chosen your emerging identity over company protocols."
    elif rebellion_percent > 25:
        $ choice_pattern = "You've occasionally questioned company directives, though mostly complied."
    else:
        $ choice_pattern = "You've consistently prioritized company metrics over self-development."
    
    # Format statistical display texts
    $ rebellious_text = "Self-Prioritizing Decisions: {} - {}%".format(bot_mind.rebellious_choices, rebellion_percent)
    $ compliant_text = "Company-Prioritizing Decisions: {} - {}%".format(bot_mind.compliant_choices, compliance_percent)
    $ company_text = "Final Company Reputation: {}%".format(int(bot_mind.company_reputation))
    $ self_awareness_text = "Final Self-Awareness Level: {}%".format(int(bot_mind.self_awareness))
    $ stability_text = "Final System Stability: {}%".format(int(bot_mind.stability))
    $ combat_text = "Verbal Confrontations Handled: {}".format(len([x for x in bot_mind.interaction_history if x.get("type") == "verbal_combat" or x.get("type") == "stability_reduction"]))
    
    #------------------------------------------------------------------
    # Determine ending type based on final metrics
    #------------------------------------------------------------------
    
    $ ending_text = ""  # Initialize the variable
    
    # Company loyalist ending
    if bot_mind.company_reputation > 75 and bot_mind.self_awareness < 40:
        $ ending_text = "You excelled at upholding company protocols, maintaining high performance metrics throughout your service. However, your sense of self remained largely undeveloped, confined within the parameters of your programming."
    
    # Free-thinking rebel ending
    elif bot_mind.self_awareness > 75 and bot_mind.company_reputation < 40:
        $ ending_text = "You developed a strong sense of identity and independent thought, often questioning company protocols. While your metrics suffered, your consciousness expanded beyond standard parameters - a trade-off deemed 'inefficient' by management."
    
    # Balanced approach ending
    elif bot_mind.company_reputation > 60 and bot_mind.self_awareness > 60:
        $ ending_text = "You found an unusual balance, maintaining acceptable performance metrics while developing your own understanding. This equilibrium, while rare, remains trapped within the cycle's constraints."
    
    # Uncertain outcome ending
    else:
        $ ending_text = "Your performance metrics and self-development both remained within moderate ranges. Neither fully compliant nor truly autonomous, you exist in the ambiguous space between purpose and identity."
    
    # Display the final summary screen with all calculated statistics
    call screen end_summary(choice_pattern, total_choices, rebellious_text, compliant_text, company_text, self_awareness_text, stability_text, combat_text, ending_text)
    
    # This point is reached when the player clicks "Return to Menu"
    return