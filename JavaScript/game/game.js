// basic settings 
// TODO more levels
// TODO random money spawn
// TODO decorations
// TODO use the latest version

import kaboom from "https://unpkg.com/kaboom@3000.0.1/dist/kaboom.mjs";

kaboom({
    global: true,
    fullscreen: true,
    scale: 2, 
    debug: true,
    clearColor: [0.5,0.5,1,1], // background colour
    font: "sans-serif",
})

const move_speed = 120 
const jump_force = 270
const fall_death = 400

// game models
loadRoot('https://i.imgur.com/')
loadSprite("punk", "HpOBuPn.png")
loadSprite("brick", "LigGnxF.png")
loadSprite("money", "lUW00lK.png")

scene('game', ({score}) => {
    const layers = (['background', 'object', 'ui'], 'object')
    
    // how map will be looked like
    const map = [
        '                                       ',
        '    ===================================',
        '=                                     =',
        '=                                     =',
        '=                                     =',
        '=          $                          =',
        '=               $                     =',
        '=          ==        $                =',
        '=            =       =                =',
        '=       $                 $           =',
        '=             ===               $     =',
        '=                      $        =     =',
        '=                $  =        =        =',
        '=    $              ==      =         =',
        '=====    =============    ===         =',
    ]

    // changing signs to its sprites
    const levelConfig = {
        width: 20,
        height: 20,
        '=': [sprite('brick'), solid],
        '$': [sprite('money'), 'money']
    }

    const gameLevel = addLevel(map, levelConfig)
    
    // label "score" at the top
    const scoreLabel = add([
        text(score),
        color(0,0,0),
        pos(40,150),
        layer('ui'),
        {
            value: score,
        }
    ])
    
    // settings how player wiil be looked like
    const player = add([
        sprite('punk'),
        solid(),
        pos(50,0), // start position
        body(),
        origin('bot')
    ])

    player.collides('money', (c) => {
        destroy(c)
        scoreLabel.value ++
        scoreLabel.text = scoreLabel.value
        if (scoreLabel.value >= 9) {
            go('win', ({ score: 9 }))
        }
    })

    player.action(() => {
        camPos(player.pos)
        if (player.pos.y >= fall_death) {
          go('lose', { score: scoreLabel.value})
        }
        scoreLabel.pos.x = player.pos.x - 20
        scoreLabel.pos.y = player.pos.y - 30
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

    scene('win', ({ score }) => {
        add([text("You won with the score " + score), origin('center'), pos(width()/2, height()/2)])
        wait(2, () => {
            go('game', {score: 0})
        })
    })

    scene('lose', ({ score }) => {
        add([text("Your score is " + score), origin('center'), pos(width()/2, height()/2)])
        wait(2, () => {
            go('game', {score: 0})
        })
    })
})


go("game", {score:0})