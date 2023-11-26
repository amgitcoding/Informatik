from flask import Flask, render_template, request

app = Flask(__name__)

def ist_schaltjahr(jahr):
    return (jahr % 400 == 0) or (jahr % 4 == 0 and jahr % 100 != 0)

def finde_schaltjahre(startjahr, endjahr):
    return [jahr for jahr in range(startjahr, endjahr + 1) if ist_schaltjahr(jahr)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_year', methods=['POST'])
def check_year():
    year = int(request.form['year'])
    is_leap = ist_schaltjahr(year)
    return f"{year} ist {'ein' if is_leap else 'kein'} Schaltjahr."

@app.route('/check_range', methods=['POST'])
def check_range():
    start_year = int(request.form['startYear'])
    end_year = int(request.form['endYear'])
    leap_years = finde_schaltjahre(start_year, end_year)
    return f"Schaltjahre zwischen {start_year} und {end_year}: {', '.join(map(str, leap_years))}"

if __name__ == '__main__':
    app.run(debug=True)

