init python:
    import random
    
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