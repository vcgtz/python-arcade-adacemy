import arcade

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = 'Nintendo Switch'

def start_render():
    arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

def end_render():
    arcade.finish_render()
    arcade.run()

def draw_main_console():
    arcade.draw_rectangle_filled(
        center_x=400,
        center_y=300,
        width=400,
        height=200,
        color=arcade.color.BLACK)
    
    arcade.draw_rectangle_filled(
        center_x=400,
        center_y=300,
        width=390,
        height=190,
        color=arcade.color.JET)

def draw_left_joycon():
    # Top
    arcade.draw_arc_filled(
        center_x=175,
        center_y=375,
        height=50,
        width=50,
        color=arcade.color.DEEP_SKY_BLUE,
        start_angle=90,
        end_angle=180
    )

    arcade.draw_rectangle_filled(
        center_x=187,
        center_y=387,
        height=26,
        width=26,
        color=arcade.color.DEEP_SKY_BLUE
    )

    # Center
    arcade.draw_rectangle_filled(
        center_x=175,
        center_y=300,
        height=150,
        width=50,
        color=arcade.color.DEEP_SKY_BLUE
    )

    # Botton
    arcade.draw_arc_filled(
        center_x=175,
        center_y=225,
        width=50,
        height=50,
        color=arcade.color.DEEP_SKY_BLUE,
        start_angle=180,
        end_angle=270
    )

    arcade.draw_rectangle_filled(
        center_x=187,
        center_y=213,
        height=26,
        width=26,
        color=arcade.color.DEEP_SKY_BLUE
    )

    # D-pad
    arcade.draw_circle_filled(
        center_x=175,
        center_y=340,
        radius=20,
        color=arcade.color.BLACK
    )

    # Arrows
    arcade.draw_circle_filled(
        center_x=160,
        center_y=280,
        radius=8,
        color=arcade.color.BLACK
    )

    arcade.draw_circle_filled(
        center_x=190,
        center_y=280,
        radius=8,
        color=arcade.color.BLACK
    )

    arcade.draw_circle_filled(
        center_x=175,
        center_y=295,
        radius=8,
        color=arcade.color.BLACK
    )

    arcade.draw_circle_filled(
        center_x=175,
        center_y=265,
        radius=8,
        color=arcade.color.BLACK
    )

    arcade.draw_text(
        text='-',
        start_y=380,
        start_x=185,
        font_size=18,
        color=arcade.color.BLACK)

    arcade.draw_rectangle_filled(
        center_x=190,
        center_y=240,
        width=10,
        height=10,
        color=arcade.color.BLACK
    )

def draw_right_joycon():
    # Top
    arcade.draw_arc_filled(
        center_x=625,
        center_y=375,
        height=50,
        width=50,
        color=arcade.color.DARK_ORANGE,
        start_angle=0,
        end_angle=90
    )

    arcade.draw_rectangle_filled(
        center_x=613,
        center_y=387,
        height=26,
        width=26,
        color=arcade.color.DARK_ORANGE
    )

    # Center
    arcade.draw_rectangle_filled(
        center_x=625,
        center_y=300,
        height=150,
        width=50,
        color=arcade.color.DARK_ORANGE
    )

    # Bottom
    arcade.draw_arc_filled(
       center_x=625,
       center_y=225,
       width=50,
       height=50,
       color=arcade.color.DARK_ORANGE,
       start_angle=270,
       end_angle=360
    )

    arcade.draw_rectangle_filled(
        center_x=613,
        center_y=213,
        height=26,
        width=26,
        color=arcade.color.DARK_ORANGE
    )

    # D-pad
    arcade.draw_circle_filled(
        center_x=625,
        center_y=280,
        radius=20,
        color=arcade.color.BLACK
    )

    # Buttons
    arcade.draw_circle_filled(
        center_x=640,
        center_y=340,
        radius=8,
        color=arcade.color.BLACK
    )

    arcade.draw_circle_filled(
        center_x=610,
        center_y=340,
        radius=8,
        color=arcade.color.BLACK
    )

    arcade.draw_circle_filled(
        center_x=625,
        center_y=355,
        radius=8,
        color=arcade.color.BLACK
    )

    arcade.draw_circle_filled(
        center_x=625,
        center_y=325,
        radius=8,
        color=arcade.color.BLACK
    )

    arcade.draw_text(
        text='+',
        start_y=380,
        start_x=605,
        font_size=14,
        color=arcade.color.BLACK)

    arcade.draw_circle_filled(
        center_x=610,
        center_y=240,
        radius=5,
        color=arcade.color.BLACK
    )

def write_title():
    arcade.draw_text(
        text='Nintendo Switch',
        start_x=310,
        start_y=420,
        font_size=18,
        color=arcade.color.BLACK_OLIVE)

if __name__ == "__main__":
    start_render()

    draw_main_console()
    draw_left_joycon()
    draw_right_joycon()
    write_title()

    end_render()
