from flask import Flask, jsonify, request, json
import random

app = Flask(__name__)

a = ["Why did the teddy bear say no to dessert? Because she was stuffed.",
   "Knock knock. Who is there? Interrupting pirates. Interrupting piryarrrrrr!",
   "What do you call a fake noodle? An impasta!",
   "Why was 6 afraid of 7? Because 7, 8, 9",
   "What does a cloud wear under a raincoat? Thunderwear.",
   "Which is faster? Hot or cold? Hot. You can easily catch a cold. ",
   " What kind of tree fits in your hand? A palm tree!",
   "Why can't you trust an atom? They make up everything.",
   "How do you talk to a giant? Use big words!",
   " What did one volcano say to the other? I lava you!"]

@app.route("/")

def index ():
    return (json.dumps(a))

@app.route('/a', methods=['GET'])
def get_jokes():
    num_jokes = request.args.get('n', default=1, type=int)
    random_jokes = random.sample(a, num_jokes)
    return jsonify(random_jokes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




