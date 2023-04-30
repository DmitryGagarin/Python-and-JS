// basic settings 
kaboom({
    global: true,
    fullscreen: true,
    scale: 2, 
    debug: true,
    clearColor: [1,1,1,1], // background colour
})

const move_speed = 120 
const jump_force = 270
let win = false
let fail = false

// game models
loadRoot('https://i.imgur.com/')
loadSprite("punk", "HpOBuPn.png")
loadSprite("brick", "LigGnxF.png")
loadSprite("money", "lUW00lK.png")

scene('game', ({score}) => {
    layers(['background', 'object', 'ui'], 'object')
    
    // how map will be looked like
    const map = [
        '                                     ',
        '    =================================',
        '=                                     ',
        '=                                     ',
        '=                                     ',
        '=          $                          ',
        '=               $                     ',
        '=          ==                         ',
        '=            =                        ',
        '=       $                  $          ',
        '=             ===               $     ',
        '=                      $        =     ',
        '=                $  =        =        ',
        '=                  ==      =          ',
        ' ====  ===============    ===         ',
    ]

    // changing signs to its sprites
    const levelConfig = {
        width: 20,
        height: 20,
        '=': [sprite('brick'), solid()],
        '$': [sprite('money'), 'money']
    }

    const gameLevel = addLevel(map, levelConfig)
    
    // label "score" at the top
    const scoreLabel = add([
        text(score),
        color(0,0,0),
        pos(40,15),
        layer('ui'),
        {
            value: score,
        }
    ])

    add([text('level' + 'test', pos(4,6))])

    // settings how player wiil be looked like
    const player = add([
        sprite('punk'), 
        solid(),
        pos(60,0), // start position
        body(),
        origin('bot')
    ])

    player.collides('money', (c) => {
        destroy(c)
        scoreLabel.value ++
        scoreLabel.text = scoreLabel.value
    })

    player.action(() => {
        if (player.pos.y < 10) {
          player.pos.x = 60
          player.pos.y = 0
        }
      })

    keyDown('left', () => {
        player.move(-move_speed, 0)
    })
    keyDown('right', () => {
        player.move(move_speed, 0)
    })
    keyPress('space', () => {
        if (player.grounded()) {
            player.jump(jump_force)
        }
    })
})

start('game', {score:0})