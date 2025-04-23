# makeymakey_controller.py - Ren'Py compatible version

class MakeyMakeyController:
    def __init__(self):
        # Track input states
        self.input_states = {
            'up': False,
            'down': False,
            'left': False,
            'right': False,
            'space': False,
            'click': False,
            'right_click': False
        }
        
        # For debug and tracking
        self.last_input = None
        self.callback = None
        
        # Map Ren'Py key names to our input names
        self.key_mapping = {
            'K_UP': 'up',
            'K_DOWN': 'down', 
            'K_LEFT': 'left',
            'K_RIGHT': 'right',
            'K_SPACE': 'space'
        }
    
    def set_input_callback(self, callback_function):
        """Set a callback function to be called when input is detected"""
        self.callback = callback_function
    
    def simulate_input(self, input_name, is_pressed=True):
        """Simulate an input for testing purposes"""
        self.input_states[input_name] = is_pressed
        if is_pressed:
            self.last_input = input_name
        
        if self.callback:
            self.callback(input_name, is_pressed)
    
    def process_events(self):
        """Process events - simplified for demo purposes"""
        # This is a placeholder - in a real implementation, we'd
        # check actual hardware inputs through pygame or other means
        pass
    
    def is_pressed(self, input_name):
        """Check if a specific input is currently pressed"""
        if input_name in self.input_states:
            return self.input_states[input_name]
        return False
    
    def get_last_input(self):
        """Get the last input that was detected"""
        return self.last_input
    
    def clear_last_input(self):
        """Clear the last input"""
        last = self.last_input
        self.last_input = None
        return last
    
# # makeymakey_controller.py
# import pygame_sdl2 as pygame
# import renpy

# class MakeyMakeyController:
#     def __init__(self):
#         # Track input states
#         self.input_states = {
#             'up': False,
#             'down': False,
#             'left': False,
#             'right': False,
#             'space': False,
#             'click': False,  # Left mouse click
#             'right_click': False  # Right mouse click
#         }
        
#         # Map keys to Makey Makey inputs - using pygame_sdl2 constants
#         self.key_mapping = {
#             pygame.K_UP: 'up',
#             pygame.K_DOWN: 'down',
#             pygame.K_LEFT: 'left', 
#             pygame.K_RIGHT: 'right',
#             pygame.K_SPACE: 'space'
#         }
        
#         # For debug and tracking
#         self.last_input = None
#         self.callback = None
    
#     def set_input_callback(self, callback_function):
#         """Set a callback function to be called when input is detected"""
#         self.callback = callback_function
    
#     def process_events(self):
#         """Process inputs using Ren'Py's current key states instead of pygame events"""
#         try:
#             # Check current state of keys
#             keys = pygame.key.get_pressed()
            
#             # Update key states
#             for key_code, input_name in self.key_mapping.items():
#                 # Get current state
#                 is_pressed = bool(keys[key_code])
                
#                 # If state changed, trigger callback
#                 if is_pressed != self.input_states[input_name]:
#                     self.input_states[input_name] = is_pressed
#                     if is_pressed:
#                         self.last_input = input_name
                    
#                     if self.callback:
#                         self.callback(input_name, is_pressed)
            
#             # Check mouse buttons - we can use renpy.get_mouse_pos() for this in Ren'Py
#             mouse_pos = renpy.get_mouse_pos()
            
#             # Mouse button states must be checked indirectly through events in Ren'Py
#             # This is a simplified approach - not ideal, but works for the demo
#             events = pygame.event.get()
#             for ev in events:
#                 if ev.type == pygame.MOUSEBUTTONDOWN:
#                     if ev.button == 1:  # Left click
#                         if not self.input_states['click']:
#                             self.input_states['click'] = True
#                             self.last_input = 'click'
#                             if self.callback:
#                                 self.callback('click', True)
#                     elif ev.button == 3:  # Right click
#                         if not self.input_states['right_click']:
#                             self.input_states['right_click'] = True
#                             self.last_input = 'right_click'
#                             if self.callback:
#                                 self.callback('right_click', True)
                
#                 elif ev.type == pygame.MOUSEBUTTONUP:
#                     if ev.button == 1:  # Left click release
#                         if self.input_states['click']:
#                             self.input_states['click'] = False
#                             if self.callback:
#                                 self.callback('click', False)
#                     elif ev.button == 3:  # Right click release
#                         if self.input_states['right_click']:
#                             self.input_states['right_click'] = False
#                             if self.callback:
#                                 self.callback('right_click', False)
                
#                 # Don't forget to return the event to Ren'Py's event queue if needed
#                 pygame.event.post(ev)
        
#         except Exception as e:
#             # Graceful error handling
#             pass
    
#     def is_pressed(self, input_name):
#         """Check if a specific input is currently pressed"""
#         if input_name in self.input_states:
#             return self.input_states[input_name]
#         return False
    
#     def get_last_input(self):
#         """Get the last input that was detected"""
#         return self.last_input
    
#     def clear_last_input(self):
#         """Clear the last input"""
#         last = self.last_input
#         self.last_input = None
#         return last