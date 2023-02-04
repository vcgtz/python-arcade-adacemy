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

# Draw a rectangle
# x0, x1, y0, y1
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Draw a retangle
# (x, y) Center or rectangle, width, heigh
arcade.draw_rectangle_filled(100, 300, 20, 60, arcade.csscolor.SIENNA)

# Draw a circle
arcade.draw_circle_filled(100, 330, 30, arcade.csscolor.DARK_GREEN)

# More trees
arcade.draw_rectangle_filled(200, 300, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 330, 60, 90, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(300, 300, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 330, 60, 90, arcade.csscolor.DARK_GREEN, 0, 180)

arcade.draw_rectangle_filled(400, 300, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(380, 300, 400, 360, 420, 300, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(500, 300, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)

# Draw a sun
arcade.draw_circle_filled(500, 500, 50, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(400, 500, 500, 500, arcade.color.YELLOW, 3)
arcade.draw_line(550, 500, 600, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 600, 500, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 450, 500, 400, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(450, 550, 500, 500, arcade.color.YELLOW, 3)
arcade.draw_line(450, 450, 500, 500, arcade.color.YELLOW, 3)
arcade.draw_line(550, 550, 500, 500, arcade.color.YELLOW, 3)
arcade.draw_line(550, 450, 500, 500, arcade.color.YELLOW, 3)

# Draw text
arcade.draw_text('Hello World!', 90, 240, arcade.csscolor.BLACK, 30)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it
arcade.run()
