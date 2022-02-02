import arcade

def main():

    arcade.open_window(500,400,"first window")
    block = arcade.create_rectangle(200,200,100,200,arcade.color.BLUE)
    arcade.run()

main()