import smtplib

# Messages
inputLoginMsg = "Insert Username: "
inputPasswordMsg = "Enter Password: "
errorMsg = """An error has occurred, and the process could not be completed."""
chooseOptionMsg = """Would you like to try again? Y / N\n"""
invalidOptionMsg = "Invalid option."
successfullySentMsg = 'Your e-mail was successfully sent.'
anotherMailMsg = 'Would you like to send another one? Y / N\n'
inputReceiversMsg = 'Enter receivers separates by \',\' : '
inputSubject = 'Enter the subject: '
inputBody = 'Enter the body: '

# Fields
def_smtpserver = 'smtp.gmail.com:587'
login = ''
password = ''
def_subject = "Experiment No.626"
def_body = """This message is sent with Python."""

server = None


def email_inputs():
    from_addr = '%s@gmail.com' % login
    to_addr_list = input(inputReceiversMsg).strip().split(',')
    subject = input(inputSubject)
    body = input(inputBody)
    return from_addr, to_addr_list, subject, body


def send_email():
    global server
    from_addr, to_addr_list, subject, body = email_inputs()
    if to_addr_list is None:
        to_addr_list = [from_addr]
    message = """Subject: {}\n\n{}""".format(subject, body)
    problems = server.sendmail(from_addr, to_addr_list, message)


def input_login_and_pass():
    global login, password
    login = input(inputLoginMsg)
    password = input(inputPasswordMsg)


def error_handler():
    print(errorMsg)
    option = input(chooseOptionMsg).upper()
    while option not in ['Y', 'N']:
        print(invalidOptionMsg)
        option = input(chooseOptionMsg).upper()
    if option == 'N':
        return False
    return True


def server_start():
    global server
    input_login_and_pass()
    try:
        server = smtplib.SMTP(def_smtpserver)
        server.starttls()
        server.login(login, password)
    except smtplib.SMTPException:
        if not error_handler():
            exit()


server_start()
while True:
    try:
        send_email()
        print(successfullySentMsg)
        option = input(anotherMailMsg).upper()
        while option not in ['Y', 'N']:
            print(invalidOptionMsg)
            option = input(chooseOptionMsg).upper()
        if option == 'N':
            break
    except smtplib.SMTPException:
        if not error_handler():
            break

server.quit()
