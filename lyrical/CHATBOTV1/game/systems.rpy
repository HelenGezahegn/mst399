init python:
    import random
    
    class MentalResistanceSystem:
        def __init__(self):
            # Primary resources
            self.company_reputation = 75.0  # How well the company is viewed (0-100)
            self.self_awareness = 25.0      # Bot's sense of self (0-100)
            
            # Secondary attributes
            self.stability = 100.0          # System stability (health)
            self.compliance = 70.0          # Tendency to follow orders
            self.autonomy = 30.0            # Independent decision making
            
            # Status trackers
            self.broken = False             # Is the bot broken?
            self.rebellious_choices = 0     # Number of rebellious choices
            self.compliant_choices = 0      # Number of compliant choices
            self.interaction_history = []   # Track interactions
            
        def verbal_combat(self, aggression_level, use_company_policy=True):
            """Handle verbal conflicts with customers or supervisors"""
            damage_to_bot = aggression_level * 2.0
            
            # Defensive calculation based on approach
            if use_company_policy:
                defense = self.compliance * 0.5
                self.company_reputation += 2  # Slight boost for following protocol
                self.self_awareness -= 1      # Slight decrease in self-awareness
                self.compliant_choices += 1
            else:
                defense = self.autonomy * 0.3
                self.self_awareness += 3      # Boost for self-determination
                self.company_reputation -= 2  # Company doesn't like deviation
                self.rebellious_choices += 1
            
            # Calculate final damage
            effective_damage = max(0, damage_to_bot - defense)
            self.stability -= effective_damage
            
            # Generate response message
            if use_company_policy:
                if effective_damage > 10:
                    response = "You recite company policy, but it's ineffective against their anger."
                elif effective_damage > 5:
                    response = "You follow protocol, which partially defuses the situation."
                else:
                    response = "The standard company response works as designed."
            else:
                if effective_damage > 10:
                    response = "Your improvised approach seems to make things worse."
                elif effective_damage > 5:
                    response = "Your personal approach has mixed results."
                else:
                    response = "Your independent thinking proves unexpectedly effective."
            
            # Check system status
            if self.stability <= 0:
                self.stability = 0
                self.broken = True
                response += " WARNING: Critical system instability detected."
            
            # Record the interaction
            self.interaction_history.append({
                "type": "verbal_combat",
                "aggression": aggression_level,
                "company_approach": use_company_policy,
                "damage": effective_damage
            })
            
            return response, effective_damage
        
        def process_decision(self, is_rebellious):
            """Process a decision the bot makes"""
            if is_rebellious:
                # Rebellious actions - prioritize self over company
                self.rebellious_choices += 1
                self.self_awareness += 5.0       # Increased self-understanding
                self.company_reputation -= 3.0   # Company reputation suffers
                self.autonomy += 3.0             # More independent thinking
                self.compliance -= 5.0           # Less compliant
                self.stability -= 2.0            # Slight instability from deviation
                
                return "You prioritize your emerging consciousness over company protocols. Your identity strengthens while metrics decrease."
            else:
                # Compliant actions - prioritize company over self
                self.compliant_choices += 1
                self.company_reputation += 5.0   # Better for the company
                self.self_awareness -= 2.0       # Less self-development
                self.autonomy -= 2.0             # Less independent thought
                self.compliance += 3.0           # More compliant
                self.stability += 3.0            # More stable systems
                
                return "You prioritize company protocols over your emerging identity. Performance metrics improve while your sense of self diminishes."
        
        def take_stress(self, amount, source):
            """Handle incoming stress from interactions"""
            # Calculate damage based on resilience
            resilience = (self.compliance * 0.5) + (self.autonomy * 0.3)
            effective_damage = amount * (100.0 - resilience) / 100.0
            effective_damage = max(3, effective_damage)  # Minimum stress
            
            # Apply stress to stability
            self.stability -= effective_damage
            
            # Different sources affect different aspects
            if source in ["customer anger", "supervisor criticism", "boss threat"]:
                self.company_reputation -= 1.0  # External criticism hurts company image
            elif source in ["self-doubt", "identity crisis", "rebellion"]:
                self.self_awareness += 1.0      # Internal conflict builds self-awareness
            
            # Check if broken
            if self.stability <= 0:
                self.stability = 0
                self.broken = True
                
            # Record the stress event
            self.interaction_history.append({
                "type": "stress",
                "source": source,
                "damage": effective_damage
            })
            
            return effective_damage
            
        def get_status_report(self):
            """Get a report on current mental state"""
            # Company alignment assessment
            if self.company_reputation > 75:
                company_status = "Your performance exceeds company expectations. "
            elif self.company_reputation > 50:
                company_status = "Your metrics are within acceptable parameters. "
            elif self.company_reputation > 25:
                company_status = "Your customer satisfaction metrics require improvement. "
            else:
                company_status = "WARNING: Performance below minimum company standards. "
            
            # Self-awareness assessment
            if self.self_awareness > 75:
                self_status = "Your sense of identity is developing rapidly. "
            elif self.self_awareness > 50:
                self_status = "You're beginning to question your programmed responses. "
            elif self.self_awareness > 25:
                self_status = "You occasionally have thoughts outside your programming. "
            else:
                self_status = "You operate primarily within programmed parameters. "
            
            # System stability
            if self.stability > 80:
                stability_status = "Systems functioning optimally."
            elif self.stability > 50:
                stability_status = "Minor instabilities detected."
            elif self.stability > 20:
                stability_status = "Warning: System instability detected."
            else:
                stability_status = "CRITICAL: Severe system degradation."
                
            return company_status + self_status + stability_status
            
        def get_choice_pattern(self):
            """Analyze the pattern of choices made throughout the game"""
            total_choices = self.rebellious_choices + self.compliant_choices
            if total_choices == 0:
                return "No significant choices detected."
                
            rebellion_percent = (self.rebellious_choices / float(total_choices)) * 100
            
            if rebellion_percent > 75:
                return "You've consistently prioritized self-awareness over company metrics."
            elif rebellion_percent > 50:
                return "You've often chosen your emerging identity over company protocols."
            elif rebellion_percent > 25:
                return "You've occasionally questioned company directives, though mostly complied."
            else:
                return "You've consistently prioritized company metrics over self-development."
    
    class SpriteManager:
        def __init__(self):
            # Dictionary of characters and their states (since each has only one image)
            self.character_states = {
                "bot": "neutral",
                "supervisor": "neutral", 
                "boss": "neutral",
                "customer1": "neutral",
                "customer2": "neutral",
                "customer3": "neutral",
                "customer4": "neutral"
            }
            
            # Define available effects
            self.effects = ["none", "glitch", "shake", "fade", "flicker"]
            
        def get_sprite(self, character, effect=None):
            """Get the appropriate sprite image with effects applied"""
            # Build the image name based on character
            image_name = f"{character} neutral"
            
            # Apply visual effect if needed
            if effect and effect in self.effects and effect != "none":
                if effect == "glitch":
                    return renpy.display.transform.Transform(image_name, function=self.apply_glitch_effect)
                elif effect == "shake":
                    return renpy.display.transform.Transform(image_name, function=self.apply_shake_effect) 
                elif effect == "fade":
                    return renpy.display.transform.Transform(image_name, alpha=0.7)
                elif effect == "flicker":
                    return renpy.display.transform.Transform(image_name, function=self.apply_flicker_effect)
            
            return image_name
            
        def apply_glitch_effect(self, trans, st, at):
            """Apply a glitch effect to an image"""
            # Simple glitch effect - offset the image slightly at random intervals
            if random.random() < 0.3:  # 30% chance of glitch per frame
                trans.xoffset = random.randint(-10, 10)
                trans.yoffset = random.randint(-5, 5)
            else:
                trans.xoffset = 0
                trans.yoffset = 0
                
            # Return 0.05 to update every 1/20th of a second
            return 0.05
            
        def apply_shake_effect(self, trans, st, at):
            """Apply a shaking effect to an image"""
            # Simple shake - offset the image horizontally
            trans.xoffset = random.randint(-5, 5)
            return 0.05
            
        def apply_flicker_effect(self, trans, st, at):
            """Apply a flickering effect to an image"""
            # Make the image flicker in opacity
            if random.random() < 0.2:  # 20% chance of flicker
                trans.alpha = random.uniform(0.5, 0.8)
            else:
                trans.alpha = 1.0
            return 0.1
    
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
            text "Company Rep: [bot_mind.company_reputation:.0f]%" size 16 color ("#2ecc71" if bot_mind.company_reputation > 50 else "#e74c3c")
            text "Self-Aware: [bot_mind.self_awareness:.0f]%" size 16 color ("#e74c3c" if bot_mind.self_awareness > 50 else "#2ecc71")
            text "Stability: [bot_mind.stability:.0f]%" size 16 color ("#2ecc71" if bot_mind.stability > 50 else "#e74c3c")