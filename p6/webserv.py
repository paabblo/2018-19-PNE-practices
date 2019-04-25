import http.server
import socketserver
import termcolor
from Seqp6 import Seq

PORT = 8000


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- printing the request line
        global lenght, opbases
        termcolor.cprint(self.requestline, 'green')
        path = self.path

        if self.path == '/':
            with open("program.html", "r") as file:
                things = file.read()
            response = 200
        elif path[:4] == '/get':
            response = 200

            msg = path.split('&')
            sequence = msg[0].split('=')[1]
            sequence = sequence.upper()
            if sequence.upper().strip('ACGT') == '':
                sequence = Seq(sequence)

                # i create new dics for the options
                count = {'base=A': ('Count A: ' + str(sequence.count('A'))),
                         'base=C': ('Count C: ' + str(sequence.count('C'))),
                         'base=G': ('Count G: ' + str(sequence.count('G'))),
                         'base=T': ('Count T: ' + str(sequence.count('T')))}
                percentage = {'base=A': ('Percentage A: ' + str(sequence.perc('A')) + '%'),
                        'base=C': ('Percentage C: ' + str(sequence.perc('C')) + '%'),
                        'base=T': ('Percentage T: ' + str(sequence.perc('T')) + '%'),
                        'base=G': ('Percentage G: ' + str(sequence.perc('G')) + '%')}

                # now, i create another dic to place both previous dics
                possibleoperations = {'count': count, 'perc': percentage}

                # when you write no message you get a len of 3, so you have to star from there

                if len(msg) == 3:
                    # now a create an empty list with the length, so when i don choose it i get no answer from it
                    lenght = ''
                    operation = msg[2].split('=')[1]
                    bases = msg[1]
                    # i try to find things inside the dics with the function key, that introduces inside the dics
                    if bases in possibleoperations[operation].keys():
                        opbases = possibleoperations[operation][bases]

                elif len(msg) == 4:  # that means that i actually wrote a message
                    lenght = 'Length: ' + str(sequence.len())
                    operation = msg[3].split('=')[1]
                    bases = msg[2]
                    if bases in possibleoperations[operation].keys():
                        opbases = possibleoperations[operation][bases]

                fs = open('response.html', 'w')
                info = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>RESPONSE SERVER</title>
</head>
<body style="background-color: lightyellow;">
    <h1>RESULTS:</h1>
    <p>sequence</p>
    <p>length</p>
    <p>operation</p>
    <a href="/">PROGRAM</a>
</body>
</html>"""
                print(opbases)
                info = info.replace("sequence", sequence.strbases.upper()).replace("length", lenght).replace("operation", opbases)
                fs.write(info)
                fs.close()
                with open('response.html', 'r') as file:
                    things = file.read()
            else:
                with open('errorsequence.html', 'r') as file:
                    things = file.read()
        else:
            response = 404
            with open("error.html", "r") as file:
                things = file.read()

        self.send_response(response)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(things)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(things))
        return


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

print("The server stopped")