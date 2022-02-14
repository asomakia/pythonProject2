import arcade

def main():
    arcade.open_window(600,400,"drawing many times")
    arcade.start_render()
    for location in range(5):
        arcade.draw_line(location*50,0,location*50,400,arcade.color.YELLOW)
    arcade.finish_render()
    arcade.run()

main()