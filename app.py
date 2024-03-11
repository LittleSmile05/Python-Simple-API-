# import requests
#
# def get_country_info(country):
#     myresp = requests.get(f"https://restcountries.com/v3.1/name/{country}")
#     data = myresp.json()
#     if myresp.status_code == 200:
#         return data
#     else:
#         return None
#
# if __name__ == "__main__":
#     country = input("Enter country name: ")
#     country_info = get_country_info(country)
#     if country_info:
#         print(country_info)
#     else:
#         print("Error fetching data.")


from flask import Flask, render_template, request
import requests

app = Flask(__name__)

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def get_country_info(country):
    response = requests.get(f"https://restcountries.com/v2/name/{country}")
    data = response.json()
    if response.status_code == 200:
        country_info = {
            "name": data[0]['name'],
            "capital": data[0]['capital']
        }
        return country_info
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country = request.form['country']
        result = get_country_info(country)
        if result:
            return render_template('result.html', country=result)
        else:
            return render_template('error.html')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
