import arcade

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_TITLE = 'Hello World!'

# Open a window
arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Set the background color using RGB
# arcade.set_background_color((189, 55, 180))

# Get ready to draw
arcade.start_render()

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it
arcade.run()
