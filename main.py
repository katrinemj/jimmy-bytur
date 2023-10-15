def on_up_pressed():
    mySprite.vy = -150
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_a_pressed():
    global Øl1, animation2
    Øl1 = sprites.create(Øl[0], SpriteKind.projectile)
    Øl1.set_position(mySprite.x, mySprite.y)
    Øl1.set_velocity(0, -150)
    animation2 = True
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_score():
    game.game_over(True)
info.on_score(100, on_on_score)

def on_on_overlap(sprite, otherSprite):
    tiles.place_on_tile(mySprite, tiles.get_tile_location(3, 14))
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_life_zero():
    game.game_over(False)
info.on_life_zero(on_life_zero)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(mySprite2)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def on_hit_wall(sprite3, location):
    sprites.destroy(Øl1)
scene.on_hit_wall(SpriteKind.projectile, on_hit_wall)

def Skift_billede():
    if Øl1.image == Øl[0]:
        Øl1.set_image(Øl[1])
    else:
        Øl1.set_image(Øl[0])

def on_on_overlap3(sprite4, otherSprite3):
    sprites.destroy(sprite4)
    sprites.destroy(otherSprite3, effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

Øl1: Sprite = None
animation2 = False
Øl: List[Image] = []
mySprite2: Sprite = None
mySprite: Sprite = None
scene.set_background_color(8)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
info.set_life(3)
mySprite = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ........................
            ........................
            ...........f............
            ..........fff...........
            .........fffff..........
            .........fffff..........
            ..........fff...........
            ...........f............
            ..........fff...........
            .........f.f.f..........
            ........f..f..f.........
            ...........f............
            ...........f............
            ..........fff...........
            .........f...f..........
            ........f.....f.........
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
ex_k = sprites.create(img("""
        . . . . . f f 4 4 f f . . . . . 
            . . . . f 5 4 5 5 4 5 f . . . . 
            . . . f e 4 5 5 5 5 4 e f . . . 
            . . f b 3 e 4 4 4 4 e 3 b f . . 
            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
            . f 3 3 e b 3 e e 3 b e 3 3 f . 
            . f 3 3 f f e e e e f f 3 3 f . 
            . f b b f b f e e f b f b b f . 
            . f b b e 1 f 4 4 f 1 e b b f . 
            f f b b f 4 4 4 4 4 4 f b b f f 
            f b b f f f e e e e f f f b b f 
            . f e e f b d d d d b f e e f . 
            . . e 4 c d d d d d d c 4 e . . 
            . . e f b d b d b d b b f e . . 
            . . . f f 1 d 1 d 1 d f f . . . 
            . . . . . f f b b f f . . . . .
    """),
    SpriteKind.enemy)
mySprite2 = sprites.create(img("""
        ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            .....7977777777.....
            .....7777777777.....
            ......66666666......
            ......77777777......
            .....7797777777.....
            .....7977777777.....
            .....7977777777.....
            .....7777777777.....
            .....7777777777.....
            .....7777777776.....
            .....7777777776.....
            ......76666666......
            ....................
            ....................
    """),
    SpriteKind.food)
controller.move_sprite(mySprite, 100, 0)
Øl = [img("""
        ....................
            ....................
            ....................
            ....................
            ....................
            ....................
            .....7977777777.....
            .....7777777777.....
            ......66666666......
            ......77777777......
            .....7797777777.....
            .....7977777777.....
            .....7977777777.....
            .....7777777777.....
            .....7777777777.....
            .....7777777776.....
            .....7777777776.....
            ......76666666......
            ....................
            ....................
    """),
    img("""
        ....................
            ....................
            ......76666666......
            .....7777777776.....
            .....7777777776.....
            .....7777777777.....
            .....7777777777.....
            .....9999999999.....
            .....9999999999.....
            .....9999999999.....
            ......99999999......
            ......66666666......
            .....7777777777.....
            .....7977777777.....
            ....................
            ....................
            ....................
            ....................
            ....................
            ....................
    """)]
animation2 = False
tiles.place_on_tile(mySprite, tiles.get_tile_location(3, 14))
scene.camera_follow_sprite(mySprite)
mySprite.ay = 350

def on_update_interval():
    global ex_k
    ex_k = sprites.create(img("""
            . . . . . f f 4 4 f f . . . . . 
                    . . . . f 5 4 5 5 4 5 f . . . . 
                    . . . f e 4 5 5 5 5 4 e f . . . 
                    . . f b 3 e 4 4 4 4 e 3 b f . . 
                    . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                    . f 3 3 e b 3 e e 3 b e 3 3 f . 
                    . f 3 3 f f e e e e f f 3 3 f . 
                    . f b b f b f e e f b f b b f . 
                    . f b b e 1 f 4 4 f 1 e b b f . 
                    f f b b f 4 4 4 4 4 4 f b b f f 
                    f b b f f f e e e e f f f b b f 
                    . f e e f b d d d d b f e e f . 
                    . . e 4 c d d d d d d c 4 e . . 
                    . . e f b d b d b d b b f e . . 
                    . . . f f 1 d 1 d 1 d f f . . . 
                    . . . . . f f b b f f . . . . .
        """),
        SpriteKind.enemy)
    ex_k.set_position(randint(0, scene.screen_width()), scene.screen_height())
    ex_k.set_velocity(0, 56)
    ex_k.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
game.on_update_interval(2000, on_update_interval)

def on_update_interval2():
    global mySprite2
    mySprite2 = sprites.create(img("""
            ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    .....7977777777.....
                    .....7777777777.....
                    ......66666666......
                    ......77777777......
                    .....7797777777.....
                    .....7977777777.....
                    .....7977777777.....
                    .....7777777777.....
                    .....7777777777.....
                    .....7777777776.....
                    .....7777777776.....
                    ......76666666......
                    ....................
                    ....................
        """),
        SpriteKind.food)
    mySprite2.set_position(randint(0, scene.screen_width()), scene.screen_height())
    mySprite2.set_velocity(0, 56)
    mySprite2.set_flag(SpriteFlag.DESTROY_ON_WALL, True)
game.on_update_interval(1000, on_update_interval2)

def on_update_interval3():
    if animation2 == True:
        Skift_billede()
game.on_update_interval(100, on_update_interval3)
