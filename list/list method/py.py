if player.clicks("wall_icon"):
    selected_item = "wall"

if selected_item == "wall" and player.clicks_on_ground():
    place_object("wall", position=mouse.position)
