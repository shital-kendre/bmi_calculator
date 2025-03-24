from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculate', methods = ['POST'])
def calculate():
    data = request.form
    print(data)


    if not data:
        return jsonify({"response":"unsuccessful",
                        "error" : "Enter valid input"})
    weight = eval(data['weight'])
    height = eval(data['height'])

    if weight <=0 or height <= 0:
        return jsonify({"response":"unsuccessful",
                        "error" : "Weight and height not in range"}) 
    

    
    bmi = weight/(height**2)

    if bmi < 18.5:
        if bmi < 18.5:
            category = "Underweight"

    elif 18.5 <= bmi < 25:
        category = "Normal weight"

    elif 25 <= bmi < 30:
        category = "Overweight"

    else:
        category = "Obesity"

    return jsonify({
        "Response": "Successful",
        "weight": weight,
        "height": height,
        "BMI": round(bmi, 2),
        "Category": category
    })




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=False)