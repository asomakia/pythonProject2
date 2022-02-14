import arcade

def main():

    arcade.open_window(500,400,"first window")
    block = arcade.create_rectangle(200,200,100,200,arcade.color.BLUE)
    arcade.start_render()
    block.draw()

    arcade.draw_text("we got this",300,300,arcade.color.YELLOW,18)


    arcade.finish_render()

    arcade.run()



main()