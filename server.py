from flask import Flask

app = Flask( __name__ )

@app.route( '/', methods = ['GET'] )
def hello_world():
    return "Hello World!"

@app.route( '/dojo', methods = ['GET'] )
def dojo():
    return "Dojo!"

@app.route( '/say/<string:something>', methods = ['GET'] )
def say(something):
    if something == 'Flask':
        return f"Hi " + something 
    elif something == 'Michael':
        return f"Hi " + something
    elif something == 'John':
        return f"Hi " + something
    return f"Sorry! No response. Try again."  

@app.route( '/repeat/<int:num>/<string:word>', methods = ['GET'] )
def repeat(num, word):
    if word == 'hello':
        return f"{num * word}"
    elif word == 'bye':
        return f"{num * word}"
    elif word == 'dogs':
        return f"{num * word}"
    return f"Sorry! No response. Try again."   

if __name__ == "__main__":
    app.run( debug = True)