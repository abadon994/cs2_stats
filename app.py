from datetime import datetime, date
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cs2_stats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    map = db.Column(db.String(50), nullable=False)
    mode = db.Column(db.String(50), nullable=False)
    score = db.Column(db.String(20), nullable=False)
    result = db.Column(db.String(10), nullable=False)
    kills = db.Column(db.Integer, nullable=False)
    deaths = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    kd = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today)
    mvps = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    matches = Match.query.order_by(Match.date.desc(), Match.id.desc()).all()
    return render_template('index.html', matches=matches)

@app.route('/stats')
def stats():
    matches = Match.query.all()
    total_matches = len(matches)
    
    wins = sum(1 for m in matches if m.result == 'win')
    losses = total_matches - wins
    total_kills = sum(m.kills for m in matches)
    total_deaths = sum(m.deaths for m in matches)
    
    avg_kd = round(total_kills / total_deaths, 2) if total_deaths else 0.0
    
    winrate = round((wins / total_matches) * 100, 1) if total_matches else 0.0
    lossrate = round((losses / total_matches) * 100, 1) if total_matches else 0.0
    
    return render_template('stats.html', total_matches=total_matches, wins=wins, losses=losses, 
                           total_kills=total_kills, total_deaths=total_deaths, avg_kd=avg_kd, 
                           winrate=winrate, lossrate=lossrate)

@app.route('/add', methods=['GET', 'POST'])
def add_match():
    if request.method == 'POST':
        kills = int(request.form['kills'])
        deaths = int(request.form['deaths'])
        kd_ratio = round(kills / deaths, 2) if deaths > 0 else float(kills)
        
        form_date = request.form['date']
        match_date = datetime.strptime(form_date, '%Y-%m-%d').date()
        
        new_match = Match(
            map=request.form['map'],
            mode=request.form['mode'],
            score=request.form['score'],
            result=request.form['result'],
            kills=kills,
            deaths=deaths,
            assists=int(request.form['assists']),
            kd=kd_ratio,
            date=match_date,
            mvps=int(request.form['mvps'])
        )
        
        db.session.add(new_match)
        db.session.commit()
        return redirect('/')
        
    today = date.today().isoformat()
    return render_template('add.html', today=today)

@app.route('/delete/<int:match_id>', methods=['POST'])
def delete_match(match_id):
    match_to_delete = Match.query.get_or_404(match_id)
    db.session.delete(match_to_delete)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)