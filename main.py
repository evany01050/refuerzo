def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . c c c . . . . . . 
                    . . . . . . a b a a . . . . . . 
                    . . . . . c b a f c a c . . . . 
                    . . . . c b b b f f a c c . . . 
                    . . . . b b f a b b a a c . . . 
                    . . . . c b f f b a f c a . . . 
                    . . . . . c a a c b b a . . . . 
                    . . . . . . c c c c . . . . . . 
                    . . . . . . . c . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        Princess,
        500,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    if info.score() < 5:
        game.over(False)
    else:
        game.over(True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    Murci.destroy()
    info.change_score_by(1)
    pause(500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

Murci: Sprite = None
projectile: Sprite = None
Princess: Sprite = None
info.start_countdown(20)
info.set_life(5)
info.set_score(0)
scene.set_background_color(9)
scene.set_background_image(img("""
    5555555555555555555555555555555556666666999999999999999999999991119999666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555555555555555556666669999999911111999999999919999999966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555555555555555556666699999999199999119999999199999999996666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555555555555555556666699999991999999991199991999999999966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555555555555555566666699999999999999999999999999999999966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555555555555555566666699999999999966699999999999999999966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555555555555555666666699999999999666669999999999966669966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555555555555555666666666666666666666666666666699666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555555555555556666666666666666666666666666666666666666666666666666666666666666666666666699999999999999999666666666666666666666666666666666666666
        5555555555555555555555555555566666666666666666666666666666666666666666666666666666666666666666666666669999999999999999999996666666666666666666666666666666666666
        5555555555555555555555555555666666666666666666666666666666666666666666666666666666666666666666666666699999999999999999999999966666666666666666666666666666666666
        5555555555555555555555555556666666666666666666666666666666666666666666666666666666666666666666666666999999999999111111999999966666666666666666666666666666666666
        5555555555555555555555555566666666666666666666666666666666666666666666666666666666666666666666666669999999999999999999119999999999999999996666666666666666666666
        5555555555555555555555555566666666666666666666666666666666666666666666666666666666666666666666999999999999999999999999991199999999999999999996666666666666666666
        5555555555555555555555555566666666666666666666666666666666666666666666666666666666666666666699999999999199999999199999999911999999999999999996666666666666666666
        5555555555555555555555555666666666666666666666666666666666666666666666666666666666666666666666699999999111111111999999999999199999999999999999966666666666666666
        5555555555555555555555556666666666666666666666666666666666666666666666666666666666666666666666669999999999999999999999999999999999999999999999966666666666666666
        5555555555555555555555556666666666666666666666666666666666666666666666666666666666666666666666666999999999999999999999699999999996699999999999966666666666666666
        5555555555555555555555566666666666666666666666666666666666666666666666666666666666666666666666666669999999999999999966666666666666666999999999666666666666666666
        5555555555555555555555666666666666666666666666666666666666666666666666666666666666666666666666666666999999999999666666666666666666666666666666666666666666666666
        5555555555555555555556666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555566666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555566666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555555666666666666666666666666666666666666666666669999996666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555556666666666666666666666666666666666666666666699999999996666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555566666666666666666666666666666666666666666666999999999996666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555666666666666666666666666666666666666666666669999999999999666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555555666666666666666666666666666666666666666666699999999999999999999999996666666666666666666666666666666666666666666666666666666666666666666666666666
        5555555555555556666666666666666666666666666666666666666666999999991911199999999999999666666669999996666666666666666666666666666666666666666666666666666666666666
        5555555555555566666666666666666666666666666666666666666699999999999919999999999999999996699999999999966666666666666666666666666666666666666666666666666666666666
        5555555555556666666666666666666666666666666666666666666999999999999919999999999999999999999999999999966666666666666666666666666666666666666666666666666666666666
        5555555555566666666666666666666666666666666666666666699999999911111199999999999999999999999999999999966666666666666666666666666666666666666666666666666666666666
        5555555556666666666666666666666666666666666666666666666699999999999999999999999919999911999999999999996666666666666666666666666666666666666666666666666666666666
        5555555666666666666666666666666666666666666666666666699999999999999999999999999911111119999999999999966666666666666666666666666666666666666666666666666666666666
        5555566666666666666666666666666666666666666666666666699999999999999999999999999999999999999999999996666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666669999999999999999999999999999999999999999666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666999999966666669999999666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666999966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444446666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444446666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444444444444666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        444444eeeeeee444444444444444444444444444444444666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        44444444444eeeeeeee444444444444444444444444444446666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        444444444444444e444444444444444444444444444444444466666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        44444444444444444444444444444444444444eee44444444444666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        44444444444444444444444444444444444444444ee444444444446666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444444444444e44444444444466666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444444444444eeeeeeeee444444666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444444444444eeeeee44e444444446666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444444444444444444444444444444666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444444444444444444444444444444466666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444444444444444444444444444444446666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444444444444444444444444444444444466666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444444444444444444444444444444444446666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        44444444444444444444444444444eeeeeee4444444444444444444444444444444666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        444444444444444444444444444444444444eee4444444444444444444444444444666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        44444444444444444444444444444444444444eee44444444444444444444444444466666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        4444444444444444444444444444444444444444444444444444444444444444444446666666666666666666666666666666666666666666688888886666666666666666666666666666666666666666
        4444444444eeeee4444444444444444444444444444444444444444444444444444444666666666666666666666666666666666666666666888888888866666666666666666666666666666666666666
        4444eeeeeeeeeeee444444444444444444444444444444444444444444444444444444444666666666666666666666666666666666666668888888888888888888888666666688886666666666666666
        4444444444444444444444444444444444444444444444444444444444444444444444444666666666666666666666666666666666666888888888888888888888888888888888888888666666666666
        4444444444444444444444444444444444444444444444444444444444444444444444444446666666666688888888888888888888888888888888888888888888888888888888888888888886666666
        44444444444444444444444444444444444444444444444eeee4444444444444444444444444466666888888888888888888888888888888888888888888888888888888888888888888888888886666
        444444444444444444444444444444444444444444444444444eeee444444444444444444444446688888888888888888888888888888888888888888888888888888888888888888888888888888888
        444444444444444444444444444444eeee44444444444444444444eeee444444444444444444444488888888888888888888888888888888888888888888888888888888888888888888888888888888
        4444444444444444444444444444eeeeeeee4444444444444444444444444444444444444444444448888888888888888888888888888888888888888888888888888888888888888888888888888888
        44444444444444444444444444eeeeeeeeee4444444444444444444444444444444444444444444444888888888888888888888888888888888888888888888888888888888888888888888888888888
        444444444444444444444444444444444444eee4444444444444444444444444444444444444444444488888888888888888888888888888888888888888888888888888888888888888888888888888
        444444444444444444444444444444444444444eeeee44444444444444444444444444444444444444448888888888888888888888888888888888888888888888888888888888888888888888888888
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444888888888888888888888888888888888888888888888888888888888888888888888888888
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444888888888888888888888888888888888888888888888888888888888888888888888888888
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444488888888888888888888888888888888888888888888888888888888888888888888888888
        44444444444444444444444444444444444444444444444444444444444eeeee444444444444444444444448888888888888888888888888888888888888888888888888888888888888888888888888
        4444444444444444444444444444444444444444444444444444444444e44444eee444444444444444444448888888888888888888888888888888888888888888888888888888888888888888888888
        4444444444444444444444444444444444444444444444444444444444444444444e44444444444444444444888888888888888888888888888888888888888888888888888888888888888888888888
        44444444444444444444444444444444444444444444444444444444444444444444eeeeeeee444444444444488888888888888888888888888888888888888888888888888888888888888888888888
        444444444444eeeeeee44444444444444444444444444444444444444444444444444444444eee4444444444448888888888888888888888888888888888888888888888888888888888888888888888
        444444eeeeee4444444eeee44444444444444444444eeeeeeeeeeee444444444444444444444444444444444444444488888888888888888888888888888888888888888888888888888888888888888
        44444444444444444444444eeee4444444444444444444444444444eeeeeee44444444444444444444444444444444448888888888888888888888888888888888888888888888888888888888888888
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444448888888888888888888888888888888888888888888888888888888888888888
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444448888888888888888888888888888888888888888888888888888888888888888
        4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444888888888888888888888888888888888888888888888888888888888888888
"""))
Princess = sprites.create(img("""
        .........................
            ........55555555.........
            ........55555555.........
            .......5555555555........
            .......555ddd5555........
            .......55ffddff55........
            .......5f16dd61f5........
            .......5519dd9155........
            .......55dddddd55........
            .......555dddd555........
            .....aaa55adda55aaa......
            .....aaa55aaaa55aaa......
            .....aaa55aaaa55aaa......
            .....aaa5aaaaa55aaa......
            .....aaacaaaaa55aaa......
            .....aaacaaaaaacaaa......
            .....aaacaaaaaacaaa......
            .....dddcaaaaaacddd......
            .....dddcaaaaaacddd......
            .......ffffffffff........
            ........ffffffff.........
            ........ffffffff.........
            ........ffffffff.........
            ........ffffffff.........
            ........ffffffff.........
            ........ffffffff.........
            ........ffffffff.........
            ........ffffffff.........
            ........fbbffbbf.........
            ........bbbbbbbb.........
    """),
    SpriteKind.player)
Princess.set_stay_in_screen(True)
controller.move_sprite(Princess)

def on_forever():
    global Murci
    Murci = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 2 2 . . . 2 2 . . . . . 
                    . . . 2 2 2 2 . 2 2 2 2 . . . . 
                    . . 2 2 2 2 2 2 2 2 2 2 2 . . . 
                    . 2 2 2 2 2 2 1 2 2 2 2 2 2 . . 
                    . 2 2 2 2 2 1 1 1 2 2 2 2 2 . . 
                    . 2 2 2 2 2 1 f f 2 2 2 2 2 . . 
                    . . 2 2 2 2 1 f f 2 2 2 2 . . . 
                    . . . 2 2 2 2 2 2 2 2 2 . . . . 
                    . . . . 2 2 2 2 2 2 2 . . . . . 
                    . . . . . 2 2 2 2 2 . . . . . . 
                    . . . . . f 2 2 2 f . . . . . . 
                    . . . . f f f . f f f . . . . . 
                    . . . . f f f . f f f . . . . . 
                    . . . . f f f . f f f . . . . .
        """),
        SpriteKind.enemy)
    Murci.set_position(160, randint(120, 0))
    Murci.set_velocity(-50, 0)
    pause(4000)
forever(on_forever)
