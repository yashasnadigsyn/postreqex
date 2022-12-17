from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/bro', methods=['POST'])
def bro_post():
    title = request.get_json()
    print(title)
    with open('title.txt', 'w') as f:
        f.write(title)
    return 'done'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, debug=True)