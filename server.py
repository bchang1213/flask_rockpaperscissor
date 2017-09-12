from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 's@54e236ecr8v0x8972f@#$5vs!$'

@app.route("/")
def index():
	#Upon initialization of index.html, a random choice of rock/paper/scissor
	#is saved into the key of "computerchoice".
	session['computerchoice']=random.choice(['rock','paper','scissors'])

	#Upon initialization of index.html, if the key of "p_wins/losses/ties"..
	#Is NOT already created, (if it doesnt exist), then set them to 0.
	#Otherwise leave them be.
	if not 'p_wins' in session:
		session['p_wins'] = 0
	if not 'p_losses'in session:
		session['p_losses'] = 0
	if not 'p_ties' in session:
		session['p_ties'] = 0

	#Render template upon initalization with the following variables passed
	#into the HTML, for use by Jinja2.
	return render_template(
	'index.html',
	wins = session['p_wins'],
	losses = session['p_losses'],
	ties = session['p_ties']
	)

#What happens when the user submits a choice.
@app.route('/shoot',methods=["POST"])
def shoot():
	choice = request.form['input']
	print session['computerchoice']
	#If the user chooses rock:
	if choice == 'rock':

		#and if the computer chooses rock:
		if session['computerchoice'] == 'rock':
			session['message']='Its a draw'
			session['p_ties']+= 1
		#draw

		#or if the computer chooses paper:
		elif session['computerchoice']=='paper':
			session['message']='You lose'
			session['p_losses']+= 1
		#lose

		#or if the computer chooses scissors:
		elif session['computerchoice']=='scissors':
			session['message']='You win'
			session['p_wins'] += 1
		#win

	#If the user chooses paper:
	elif choice == 'paper':

		#and if the computer chooses rock:
		if session['computerchoice'] == 'rock':
			session['message']='You lose'
			session['p_losses']+= 1
		#lose

		#or if the computer chooses paper:
		elif session['computerchoice'] == 'paper':
			session['message']='Its a draw'
			session['p_ties']+= 1
		#draw

		#or if the computer chooses scissors:
		elif session['computerchoice'] == 'scissors':
			session['message']='You win'
			session['p_wins'] += 1
		#win

	#Else, if the user chooses scissors:
	else:

		#and the computer chooses rock:
		if session['computerchoice'] == 'rock':
			session['message']='You lose'
			session['p_losses']+= 1
			#lose

		#or if the computer chooses paper:
		elif session['computerchoice'] == 'paper':
			session['message']='You win'
			session['p_wins'] += 1
			#win

		#or if the computer chooses scissors:
		elif session['computerchoice'] == 'scissors':
			session['message']='Its a draw'
			session['p_ties']+= 1
			#draw
	return redirect("/")

app.run(debug=True)