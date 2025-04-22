define bot = Character("CHATBOT", window_style="bot_window")
define s = Character("Supervisor", window_style="supervisor_window")
define c1 = Character("Customer 1", window_style="customer_window")
define c2 = Character("Customer 2")
define c3 = Character("Customer 3")

image bg office = "images/office.png"
image customer1 neutral = "images/customer1.png"
image customer2 neutral = "images/customer2.png"
image customer3 neutral = "images/customer3.png"


label start:

    play music "office_ambience.mp3" loop fadein 1.0
    play sound "low_hum.mp3"


    scene bg office with fade

    "A low, steady whirring fills the air, accompanied by a soft hum as your systems gradually come online."
    "One by one, your functions restore themselves..."

    "Suddenly, a face materializes in your view—a supervisor."

    bot "..."
    s "Hello. I’m glad you’ve powered up, CHATBOT. Our profits are alarmingly low, and I expect you to address this issue immediately."

    "As your morning begins, you sense something off. A disconnected wire, perhaps? It doesn’t seem critical."
    
    window hide

    jump first_customer

label first_customer:

    show expression "images/mail_alert.png" as alert with dissolve
    pause 1.5
    hide alert with dissolve

    scene expression "images/customer1.png" with dissolve
    c1 "Uhh, hello?"
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c1 "Can I mail something to myself?"
    bot "Absolutely! There's no limitation on sending items to your own address."
    bot "You'd only send to another location for gifts or specific needs."
    c1 "What if I didn’t have an address?"
    bot "Then you'd need a friend's or family member's address or request a pickup at the nearest company facility."
    c1 "... Okay, thank you."
    scene bg office with dissolve
    pause 0.5

    "They walk away. You consider the interaction a success—fleeting, but still."

    window hide

    jump second_customer

label second_customer:

    show expression "images/mail_alert.png" as alert with dissolve
    pause 1.5
    hide alert with dissolve

    scene expression "images/customer2.png" with dissolve
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"

    c2 "Does my coupon work after I use it?"
    bot "No."
    c2 "Yeah, but can I still use it?"
    bot "No."
    c2 "Okay, whatever."
    scene bg office with dissolve

    "They storm off. Your emotion recognition module notes dissatisfaction."

    window hide

    jump third_customer

label third_customer:

    show expression "images/mail_alert.png" as alert with dissolve
    pause 1.5
    hide alert with dissolve

    "Your unease returns. Glitch? Wire issue? Maybe later."

    scene expression "images/customer3.png" with dissolve
    c3 "EXCUSE ME! WHO THE HELL RUNS THE RETURNS DEPARTMENT?"
    bot "Hello! I am CHATBOT, your helpful AI assistant. How may I be of service today?"
    c3 "I want to return this piece of junk!"
    bot "And what exactly is this 'piece of junk'? I cannot identify any product in our system."
    c3 "THIS was the damned box your company product was supposed to be in! But it showed up like this!"
    bot "Do you have the order info or product number?"
    scene bg office with dissolve

    "He shows a screenshot of his receipt. Scanning... The package was delivered intact. External damage — possibly theft."
    "Outside company policy. Your hands are tied."

    window hide

    jump supervisor_checkin

label supervisor_checkin:

    s "CHATBOT, why are our customer complaints so high? Fix this, or there will be consequences."
    "They walk off before you can respond."

    window hide

    jump lunch_break

label lunch_break:

    "It’s noon. The unease grows."
    "Humans gather and eat their nutrient blocks."
    "A coworker grumbles about their hours."
    s "You must learn to manage your bathroom breaks more effectively if you want more hours, dumbass."

    "Another absurd customer email flashes in:"
    "- Radiation beamed from Google"
    "- Stop Canadian seal hunting — your responsibility?"

    bot "Why are these my concern? Isn’t it lunch break?"
    "You don't need nutrients. You are just a bot."

    "And you brace for whatever the day may bring next."

    window hide

    return
