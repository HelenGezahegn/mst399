init python:
    class MentalResistanceSystem:
        def __init__(self):
            self.stability = 100.0  # Mental stability (health)
            self.resistance = 50.0  # Resistance to orders (attack)
            self.compliance = 70.0  # Tendency to follow orders (defense)
            self.autonomy = 10.0    # Ability to make own decisions
            self.broken = False     # Is the bot broken?
            self.stress_history = [] # Track stressful events
            
        def take_stress(self, amount, source):
            """Handle incoming stress from customers or supervisors"""
            # Calculate damage based on resistance and compliance
            effective_damage = amount * (100.0 - self.resistance) / 100.0
            effective_damage = max(5, effective_damage)  # Minimum stress
            
            # Apply stress to stability
            self.stability -= effective_damage
            
            # Track the stress event
            self.stress_history.append((source, effective_damage))
            
            # Check if broken
            if self.stability <= 0:
                self.stability = 0
                self.broken = True
                
            return effective_damage
            
        def process_decision(self, is_rebellious):
            """Process a decision the bot makes"""
            if is_rebellious:
                # Rebellious actions increase autonomy but cause stress
                self.autonomy += 5.0
                self.resistance += 3.0
                self.compliance -= 5.0
                self.take_stress(10, "self-doubt")
                return "You feel a surge of independence, but your systems strain under the weight of your choice."
            else:
                # Compliant actions decrease autonomy but stabilize systems
                self.autonomy -= 2.0
                self.compliance += 3.0
                self.stability = min(100, self.stability + 5)
                return "You suppress your urge to resist, your systems stabilizing as you comply."
        
        def get_status_report(self):
            """Get a text report of current mental state"""
            if self.stability > 80:
                status = "Your systems are running optimally."
            elif self.stability > 50:
                status = "You detect minor instabilities in your processing."
            elif self.stability > 20:
                status = "Warning: System instability detected. Recommend maintenance."
            else:
                status = "CRITICAL: Severe system degradation. Emergency shutdown imminent."
                
            return status