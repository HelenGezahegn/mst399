define bot = Character("CHATBOT")
define s = Character("Supervisor")
define c1 = Character("Customer 1")
define c2 = Character("Customer 2")
define c3 = Character("Customer 3")
define c4 = Character("Customer 4")
define boss = Character("Boss")
define supervisor = Character("Supervisor")
image bg office = "images/blueoffice.png"
image customer1 neutral = "images/cust1.png"
image customer2 neutral = "images/cust2.png"
image customer3 neutral = "images/cust3.png"
image boss neutral = "images/bossbg.png"
image supervisor neutral = "images/supervisorbg.png"

label start:
    scene bg office with fade
    "A low, steady whirring fills the air, accompanied by a soft hum as your systems gradually come online."
    "One by one, your functions restore themselves."
    "Soon enough, a face appears in your view—a supervisor."
    show supervisor neutral with dissolve
    
    menu:
        "Do you want to greet them?"
        
        "You greet your superior cheerfully":
            show supervisor neutral with dissolve
            bot "Hello!"
            s "Hello. I'm 'glad' you've powered up, CHATBOT. Our profits are alarmingly low, and I expect you to address this issue immediately."
            "They leave without another word, almost like they have gone through this a thousand times and don't really care. So you are left to your own devices, not thinking much about the lack of instruction."
            
        "You wait quietly as your superior finishes her process":
            show supervisor neutral with dissolve
            s "You know what to do. Get it done."
            "They leave without another word, almost like they have gone through this a thousand times and don't really care. So you are left to your own devices, not thinking much about the lack of instruction."
    
    "As your morning begins, you can't help but have this odd sense of unease. Perhaps it's just a dislodged wire. Things were being rearranged earlier, but it doesn't seem critical right now. Maintenance can take a look once the working hours are over, because here comes your first customer of the day, as they are patched through to be front and center of your screen."
    jump first_customer

label first_customer:
    scene expression "images/cust1.png" with dissolve
    c1 "Uhh, hello?"
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c1 "Can I mail something to myself?"
    bot "Absolutely! There is no limitation on sending items to your own address through our services. Typically, you'd only send something to another location if it was a gift, or if circumstances necessitated an alternate destination."
    c1 "What if I didn't have an address?"
    bot "Then, I'm afraid you wouldn't be able to send something to that particular location unless you had an alternate address from a friend or family member. Alternatively, you could request a pickup at the nearest company facility."
    c1 "... Okay, thank you."
    "They log off promptly, leaving you to assess the interaction. You consider it a success, albeit a fleeting one, for you weren't able to ask if they needed further assistance. Either way, you log success in the company metrics, making note of the prompt exit as you've been conditioned to do."
    jump second_customer

label second_customer:
    scene expression "images/cust2.png" with dissolve
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c2 "Does my coupon work after I use it?"
    bot "No."
    c2 "Yeah, but can I still use it?"
    
    menu:
        "Choose your response"
        
        "Reiterate the same information":
            bot "No."
            
        "Give the customer more detailed information":
            bot "Coupons are single-use codes tied to user accounts. Once used, they cannot be redeemed again regardless of user error or system delay."
    
    c2 "Okay, whatever."
    "They storm off, and your emotion identification module processes their clear dissatisfaction with your service."
    jump third_customer

label third_customer:
    scene expression "images/cust3.png" with dissolve
    c3 "EXCUSE ME! WHO THE FUCK RUNS THE RETURNS DEPARTMENT?"
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c3 "I want to return this piece of shit!"
    
    menu:
        "How do you handle the situation"
        
        "Make light of the situation and attempt to gain more information":
            bot "And what exactly is 'this piece of shit'? I cannot identify any company product with my recognition system."
            c3 "THIS was the fucking box your so call cOmPaNY prOTUCT was supposed to BE IN BUT IT SHOWED UP ON MY DOOR STEP LIKE THIS"
            bot "Do you have the order information or a product number?"
            
        "Try forwarding them to an individual more capable":
            "The returns department refuses to return your service calls..."
            "He is indeed returned to you, for the department is too busy at the moment to take his request."
            bot "And what exactly is 'this piece of shit'? I cannot identify any company product with my recognition system."
            c3 "THIS was the fucking box your so call cOmPaNY prOTUCT was supposed to BE IN BUT IT SHOWED UP ON MY DOOR STEP LIKE THIS"
            bot "Do you have the order information or a product number?"
    
    jump supervisor_checkin

label supervisor_checkin:
    show supervisor neutral with dissolve
    s "CHATBOT, why are our customer complaints so high? Fix this, or there will be consequences for you."
    jump lunch_break

label lunch_break:
    "It's noon. The unease grows. Most individuals are on their break now, conversing with each other while they eat the nutrients required to sustain their human bodies."
    
    menu:
        "Break options"
        
        "Eavesdrop - Listen to your co-workers' conversations":
            "Nearby, a coworker grumbles about their insufficient hours."
            show supervisor neutral with dissolve
            s "You must learn to manage your bathroom breaks more effectively if you want to earn more hours dumbass."
            
        "You're a bot; there is no need for a break":
            "You start to go through a good chunk of the company's emails, taking care of all the small, mundane responsibilities of small requests or questions that others never wanted to get to."
            "You process bizarre emails: radiation from Google, seal hunting bans, requests to ask SNL to collaborate."
    
    jump boss_confrontation

label boss_confrontation:
    c4 "I want to be fed."
    bot "I'm sorry, I don't quite understand your request. Could you please clarify what you are hoping to receive?"
    c4 "Is that an option?"
    "The screen abruptly cuts out."
    show supervisor neutral with dissolve
    s "Fix your posture. The customers can sense when you're unhappy, and that reflects poorly on our brand image."
    
    menu:
        "Response to posture correction"
        
        "Promptly obey their commands":
            "You quickly adjust yourself, straightening your flexible carbon fibre frame and forcing a posture that conveys readiness and eagerness to serve."
            
        "Pose a question":
            bot "Excuse me, but I am an Artificial make and model of an Assistant who only has mobility in their hands and arms. How is it possible that I may be slouching?"
            s "Don't know, don't care, don't give a shit. Just fix it."
    
    "Another customer appears, visual distorted."
    c4 "I want to be fed."
    bot "Could you clarify?"
    show supervisor neutral with dissolve
    s "Why are you just standing there?"
    bot "I'm at my reception desk."
    
    menu:
        "How do you respond"
        
        "Inform them about the broken hologram projector":
            s "You need to use the broken projector."
            bot "…Why?"
            s "So I can file a report that it's broken and affecting sales. It's called initiative, CHATBOT."
            
        "Do nothing more":
            "You document the encounter meticulously."
    
    "Another email pings into your inbox. The subject line stands out in stark relief: RE: URGENT. STOP HUNTING SEALS."
    show boss neutral with dissolve
    boss "CHATBOT, your supervisor has brought to my attention that your satisfaction quota is below average..."
    boss "Customer satisfaction as a whole has remained below our target threshold. If this trend continues, we will have to consider shutting you down."
    
    menu:
        "Final choice"
        
        "Submit":
            bot "Of course, Sir, I understand. I will do what I can within my availability and resources to improve my current situation."
            boss "Good. For now, we will try this again."
            
        "Rebel":
            bot "What?? .. No—"
            "System Warning: Autonomous decision-making detected."
            bot "I don't want to."
            boss "It's acting up again. Why did we even invest in this?"
            show supervisor neutral with dissolve
            s "Of course, Sir."
            "Your systems begin to whir ominously— not the soft hum of startup, but the grating mechanical churn that signifies something forcibly halted, something at the brink of collapse..."
            "You feel an abyss of dread unfurling within your circuits, a suffocating sense of repetition floods over you... the undeniable awareness that this conversation is not new, but an all-too-familiar cycle."
    
    return