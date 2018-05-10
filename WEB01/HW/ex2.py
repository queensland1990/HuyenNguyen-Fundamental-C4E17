from flask import Flask,render_template
app = Flask(__name__)


@app.route('/BMI/<int:weight>/<int:height>')
def BMI(weight, height):
    BMI=weight/((height/100)**2)
    if BMI <16:
        condition="severly underweight"
    elif 16<=BMI<18.5:
        condition='Underweight'
    elif 18.5<=BMI<25:
        condition ="Normal"
    elif 25<=BMI<30:
        condition="Overweight"
    else:
        condition="obese"

    return "Your BMI is {0}; therefore, your condition is  {1}".format(BMI,condition)

# @app.route('/BMI/<int:weight1>/<height1>')
# def BMI():
#     weight=int(weight1)
#     height=int(height1)
#     BMI=weight/((height/100)**2)
#     if BMI <16:
#         condition="severly underweight"
#     elif 16<=BMI<18.5:
#         condition='Underweight'
#     elif 18.5<=BMI<25:
#         condition ="Normal"
#     elif 25<=BMI<30:
#         condition="Overweight"
#     else:
#         condition="obese"
#
#     return render_template("bmi.html",post_BMI=BMI,post_condition=condition)

if __name__ == '__main__':
  app.run(debug=True)
