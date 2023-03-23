from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/emails', methods=['POST'])
def email_generater():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    compname = request.form['compname']

    def emails(firstname, lastname, compname):
        firstname = firstname.lower()
        lastname = lastname.lower()
        compname = compname.lower()
        templatesCompany = [
            "ceo@nameofcompany.com",
            "media@nameofcompany.com",
            "info@nameofcompany.com",
            "sales@nameofcompany.com",
            "customersupport@nameofcompany.com",
            "support@nameofcompany.com",
            "help@nameofcompany.com",
            "management@nameofcompany.com",
        ]
        templatesPersonal = [
            "firstname.lastname@gmail.com", "firstinitial.lastinitial@gmail.com",
            "firstinitial.lastname@gmail.com", "firstname.lastinitial@gmail.com",
            "firstname@gmail.com", "lastname@gmail.com"
        ]
        emailList = []

        for email in templatesCompany:
            newMail = email.replace('nameofcompany', compname)
            emailList.append(newMail)

        for emailp in templatesPersonal:
            newEmail = emailp
            if "firstname" in emailp:
                newEmail = newEmail.replace('firstname', firstname)
            if "lastname" in emailp:
                newEmail = newEmail.replace('lastname', lastname)
            if "firstinitial" in emailp:
                newEmail = newEmail.replace('firstinitial', firstname[0])
            if "lastinitial" in emailp:
                newEmail = newEmail.replace('lastinitial', lastname[0])

            emailList.append(newEmail)
        print(emailList[8])
        return emailList

    emailList = emails(firstname, lastname, compname)
    return render_template('emails.html', emailList=emailList)


app.run(host='0.0.0.0', port=81)
