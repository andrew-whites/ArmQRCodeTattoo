from datetime import date
from uuid import uuid4
from flask import Flask

from Views import ListUnpaidContractView
from Converters.DateConverter import DateConverter

app = Flask(__name__)
app.url_map.converters['date'] = DateConverter

@app.route('/', methods = ['GET'])
def index():
    return "Hello world!!!"

@app.route('/home')
@app.route('/information')
@app.route('/information/<string:name>')
@app.route('/introduction')
def home(name: str = ''):
    greeting_str = name
    if name!='':
        greeting_str = f'Hello {name}! '
    
    return '''
    <html><head><title>Online Personal … System</title>
    </head><body>
    <h1>Online … Counseling System (OPCS)</h1>
    <p>''' + greeting_str + '''This is a template of a web-based counseling
    application where counselors can … … …</em>
    </body></html>
    '''

# @app.route('/exam/passers/list/<float:rate>/<uuid:docId>')
# def report_exam_papers(rating:float, docId:uuid4 = None):
#     exams = list_passing_scores(rating)
#     responce = make_responce(
#         render_template('exam/lists_exam_passers.html', exams=exams, docId=docId), 200)
#     return responce

@app.route('/certificate/accomp/<string:name>/<string:course>/<date:accomplished_date>')
def show_certification(name:str, course:str, accomplished_date:date):
    certificate = """<html><head>
    <title>Certificate of Accomplishment</title>
    </head><body>
    <h1>Certificate of Accomplishment</h1>
    <p>The participant {} is, hereby awarded this certificate
of accomplishment, in {} course on {} date for passing all exams. He/
she proved to be ready for any of his/her future endeavors.</em>
        </body></html>
        """.format(name, course, accomplished_date)
    return certificate, 200

def show_honor_dissmisal(counselor:str, effective_date:date, patient:str):
    letter = """
    … … … … …
    </head><body>
    <h1> Termination of Consultation </h1>
    <p>From: {}
    <p>Head, Counselor
    <p>Date: {}
    <p>To: {}
    <p>Subject: Termination of consultation
    <p>Dear {},
    … … … … … …
    <p>Yours Sincerely,
    <p>{}
    </body>
    </html>
    """.format(counselor, effective_date, patient, patient, counselor)
    return letter, 200

app.add_url_rule('/certificate/terminate/<string:counselor>/<date:effective_date>/<string:patient>', 'show_honor_dissmisal', show_honor_dissmisal)
app.add_url_rule('/contract/unpaid/patients', view_func=ListUnpaidContractView.as_view('list-unpaid-view'))

if __name__ == '__main__' :
    app.run(debug=True)