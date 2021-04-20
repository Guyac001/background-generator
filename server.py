#258. Building A Flask Server		server.py
import os, csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index4.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name) 

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		if os.stat("database.txt").st_size == 0:
			file = database.write(f'\nemail,subject,message')
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message} ')
		# file = database.write(f'\n{data["email"]},{data["subject"]},{data["message"]} ')
		# Note: \n is to create a new line in the database.txt file

def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		# spamwriter = csv.writer(database2, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		if os.stat("database.csv").st_size == 0:
			csv_writer.writerow(["email","subject","message"])
			# csv_writer.writerow("email","subject","message")
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		# csv_writer = csv.writer(database2, delimiter=',' quotechar='"', newline='', quoting=csv,QUUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		# write_to_file(data)
		write_to_csv(data)
		return redirect('/thankyou.html')
		# show 'Thank you, I will be in touch shortly'
	else:
		return 'Something went wrong. Try again!'


# @app.route('/<username>')
# def index_page(username=None):
#     return render_template('index.html', name=username)

# @app.route('/<username2>/<int:post_id>')
# def index_page2(username2, post_id):
#     return render_template('index2.html', name2=username2, id2=post_id)

# @app.route('/what')
# def index_page3():
#     return render_template('index3.html')

# @app.route('/about')
# def about_page():
#     return render_template('about.html')

# @app.route('/blog')
# def blog():
#     return 'Hello, Blog-reader!'

# @app.route('/blog/2020/dogs')
# def blog_2020_dogs():
#     return 'Hello, Dog-reader!'

# @app.route('/Univers')
# def index_page4():
#     return render_template('index4.html')

# @app.route('/index4.html')
# def index_page4a():
#     return render_template('index4.html') 

# @app.route('/works.html')
# def index_page5():
#     return render_template('works.html')

# @app.route('/work.html')
# def index_page5a():
#     return render_template('work.html')

# @app.route('/about4.html')
# def index_page6():
#     return render_template('about4.html')

# @app.route('/contact.html')
# def index_page7():
#     return render_template('contact.html')

# @app.route('/components.html')
# def index_page8():
#     return render_template('components.html')



