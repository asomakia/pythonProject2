import arcade

def mains():

    arcade.open_window(1000,1000,"my house")
    arcade.set_background_color(arcade.color.BABY_BLUE)
    base = arcade.create_rectangle(500,500,350,350,arcade.color.GREEN)
    door = arcade.create_rectangle(500,375,50,100,arcade.color.BROWN)
    window1 = arcade.create_ellipse_filled_with_colors(400,600,30,30,arcade.color.CAMEO_PINK,arcade.color.CAMEO_PINK)
    window2 = arcade.create_ellipse_filled_with_colors(600, 600, 30, 30, arcade.color.CAMEO_PINK,arcade.color.CAMEO_PINK)
    roof = arcade.create_polygon([(325,675),(675,675),(500,850)],arcade.color.ROSE,)

    arcade.start_render()

    base.draw()
    door.draw()
    window1.draw()
    window2.draw()
    roof.draw()

    arcade.finish_render()

    arcade.run()

mains()