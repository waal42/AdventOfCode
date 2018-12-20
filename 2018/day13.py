from time import time
from pprint import pprint

start = time()
carts = dict()
tracks = list()


# TODO(XXX) iniciální načtění přepsat ze seznamu seznamů do slovníku se souřadnicemi jako klíčem, boolean parametrem has_cart a int indexem, o které auto se jedná
# TODO(XXX) slovník s auty by mohl obsahovat deque pro určení, kterým směrem příště zatočí, bude se to dobře držet a jednoduše otáčet
with open("day13testinput.txt") as fin:
    i = 0
    cart = 0
    for line in fin.read().split("\n"):
        tracks.append(list(line))
        if ">" in tracks[i]:
            cart_x = tracks[i].index(">")
            carts[cart] = {"pos_x": cart_x, "pos_y": i, "direction": "right"}
            cart += 1
            tracks[i][cart_x] = "-"
        if "<" in tracks[i]:
            cart_x = tracks[i].index("<")
            carts[cart] = {"pos_x": cart_x, "pos_y": i, "direction": "left"}
            cart += 1
            tracks[i][cart_x] = "-"
        if "^" in tracks[i]:
            cart_x = tracks[i].index("^")
            carts[cart] = {"pos_x": cart_x, "pos_y": i, "direction": "up"}
            cart += 1
            tracks[i][cart_x] = "|"
        if "v" in tracks[i]:
            cart_x = tracks[i].index("v")
            carts[cart] = {"pos_x": cart_x, "pos_y": i, "direction": "down"}
            cart += 1
            tracks[i][cart_x] = "|"
        i += 1

pprint(carts)


for line in tracks:
    print("".join(line))


print("computed in " + str(time() - start) + " seconds")
