import arcade

class Platformer(arcade.Window):
    def __init__(self):
        pass
    
    def setup(self):
        """Sets up the game for the current level"""
        pass
    
    def on_key_press(self, key: int, modifiers: int):
        """Processes key presses
        
        Arguments: 
            key {int} -- Which key was pressed
            modifieres {int} -- Which modifiers were down at the time
        """
        pass
        
    def on_key_release(self, key: int, modifiers: int):
        """ Processes key releases
        
        Arguments: 
            key {int} -- Which key was released
            modifieres {int} -- Which modifiers were down at the time
        """
        pass
        
    def on_update(self, delta_time: float): 
        """ Updaptes the position of all game objects
        
        Arguments: 
            delta_time {float} -- How much time since the last call
        """
        pass
    
    def on_draw(self):
        pass
    
if __name__ == "__main__":
    window = Platformer()
    window.setup()
    arcade.run()