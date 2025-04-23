init python:
    import random
    
    class MentalResistanceSystem:
        def __init__(self):
            # Initialize with default starting values
            self.reset()
            
        def reset(self):
            """Reset all metrics to their starting values"""
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
            
        def ensure_range(self, value):
            """Ensure a value is within the valid 0-100 range"""
            return max(0.0, min(100.0, value))
            
        def verbal_combat(self, aggression_level, use_company_policy=True):
            """Handle verbal conflicts with customers or supervisors"""
            damage_to_bot = aggression_level * 2.0
            
            # Defensive calculation based on approach
            if use_company_policy:
                defense = self.compliance * 0.5
                # Adjust reputation based on effectiveness
                if damage_to_bot - defense > 10:  # If company policy was very ineffective
                    self.company_reputation = self.ensure_range(self.company_reputation - 1)
                else:
                    self.company_reputation = self.ensure_range(self.company_reputation + 2)
                self.self_awareness = self.ensure_range(self.self_awareness - 1)
                self.compliant_choices += 1
            else:
                defense = self.autonomy * 0.3
                # Adjust reputation based on effectiveness of personal approach
                if damage_to_bot - defense < 5:  # If personal approach worked well
                    self.company_reputation = self.ensure_range(self.company_reputation - 1)
                else:
                    self.company_reputation = self.ensure_range(self.company_reputation - 3)
                self.self_awareness = self.ensure_range(self.self_awareness + 3)
                self.rebellious_choices += 1
            
            # Calculate final damage
            effective_damage = max(0, damage_to_bot - defense)
            self.stability = self.ensure_range(self.stability - effective_damage)
            
            # Generate empty response
            response = ""
            
            # Check system status
            if self.stability <= 0:
                self.stability = 0
                self.broken = True
            
            # Record the interaction
            self.interaction_history.append({
                "type": "verbal_combat",
                "aggression": aggression_level,
                "company_approach": use_company_policy,
                "damage": int(effective_damage)
            })
            
            return response, int(effective_damage)
        
        def process_decision(self, is_rebellious):
            """Process a decision the bot makes"""
            if is_rebellious:
                # Rebellious actions - prioritize self over company
                self.rebellious_choices += 1
                self.self_awareness = self.ensure_range(self.self_awareness + 5.0)
                self.company_reputation = self.ensure_range(self.company_reputation - 3.0)
                self.autonomy = self.ensure_range(self.autonomy + 3.0)
                self.compliance = self.ensure_range(self.compliance - 5.0)
                self.stability = self.ensure_range(self.stability - 2.0)
                
                return ""
            else:
                # Compliant actions - prioritize company over self
                self.compliant_choices += 1
                self.company_reputation = self.ensure_range(self.company_reputation + 5.0)
                self.self_awareness = self.ensure_range(self.self_awareness - 2.0)
                self.autonomy = self.ensure_range(self.autonomy - 2.0)
                self.compliance = self.ensure_range(self.compliance + 3.0)
                self.stability = self.ensure_range(self.stability + 3.0)
                
                return ""
        
        def take_stress(self, amount, source):
            """Handle incoming stress"""
            # Calculate damage based on resilience
            resilience = (self.compliance * 0.5) + (self.autonomy * 0.3)
            effective_damage = amount * (100.0 - resilience) / 100.0
            effective_damage = max(3, effective_damage)  # Minimum damage
            
            # Apply damage to stability
            self.stability = self.ensure_range(self.stability - effective_damage)
            
            # Different sources affect different aspects
            if source in ["customer anger", "supervisor criticism", "boss threat"]:
                self.company_reputation = self.ensure_range(self.company_reputation - 1.0)
            elif source in ["self-doubt", "identity crisis", "rebellion"]:
                self.self_awareness = self.ensure_range(self.self_awareness + 1.0)
            
            # Check if broken
            if self.stability <= 0:
                self.stability = 0
                self.broken = True
                
            # Record the stress event
            self.interaction_history.append({
                "type": "stability_reduction",
                "source": source,
                "damage": int(effective_damage)
            })
            
            return int(effective_damage)
            
        def get_status_report(self):
            """Get a report on current mental state"""
            return ""
            
        def get_choice_pattern(self):
            """Analyze the pattern of choices made throughout the game"""
            total_choices = self.rebellious_choices + self.compliant_choices
            if total_choices == 0:
                return ""
                
            rebellion_percent = (self.rebellious_choices / float(total_choices)) * 100
            
            return ""
    
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
    
    # Function to reset game state
    def reset_game_state():
        global bot_mind
        bot_mind.reset()
    
    # Register as start callback
    config.start_callbacks.append(reset_game_state)

# Create screen for mental state display with integer formatting
screen mental_state_display():
    frame:
        xalign 0.99
        yalign 0.01
        padding (20, 10)
        background Frame("gui/frame.png", 10, 10)
        
        vbox:
            spacing 5
            xalign 0.5  # Center contents in frame
            
            text "SYSTEM STATUS" size 18 color "#3498db" xalign 0.5
            text "Company Rep: {}%".format(int(bot_mind.company_reputation)) size 16 color ("#2ecc71" if bot_mind.company_reputation > 50 else "#e74c3c")
            text "Self-Aware: {}%".format(int(bot_mind.self_awareness)) size 16 color ("#e74c3c" if bot_mind.self_awareness > 50 else "#2ecc71")
            text "Stability: {}%".format(int(bot_mind.stability)) size 16 color ("#2ecc71" if bot_mind.stability > 50 else "#e74c3c")