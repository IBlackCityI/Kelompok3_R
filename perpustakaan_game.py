from flask import Flask, render_template

application = Flask(__name__)
@application.route('/')
def index():
    return render_template('index.html')

@application.route('/connect-four')
def connectfour():
    return render_template('connect-four.html')

@application.route('/tetris')
def tetris():
    return render_template('tetris.html')

@application.route('/suit')
def suit():
    return render_template('suit.html')

@application.route('/pukul-tikus-tanah')
def pukultikustanah():
    return render_template('pukul-tikus-tanah.html')

@application.route('/tic-tac-toe')
def tictactoe():
    return render_template('tic-tac-toe.html')

@application.route('/flip-memory-card')
def flipmemorycard():
    return render_template('flip-memory-card.html')

@application.route('/tower-blocks')
def towerblocks():
    return render_template('tower-blocks.html')

@application.route('/game-2048')
def game2048():
    return render_template('game-2048.html')

@application.route('/game-breakout')
def gamebreakout():
    return render_template('game-breakout.html')

@application.route('/dodge-ball')
def dodgeball():
    return render_template('dodge-ball.html')

@application.route('/smash-block')
def smashblock():
    return render_template('smash-block.html')

if __name__ == '__main__':
    application.run(debug=True)