from flask import Flask
import os

app = Flask(__name__)

# Route for "/" for a web-based interface to this micro-service:
@app.route('/')
def index():
  from flask import render_template
  return render_template("index.html")

# Extract a hidden "uiuc" GIF from a PNG image:
@app.route('/extract', methods=["POST"])
def extract_hidden_gif():
  from flask import send_file, request
  # ...your code here...
  os.makedirs('temp_lib',exist_ok=True)

  png = request.files['png']
  if png == False:
    return "ERROR: PNG may not be valid", 500
  else:
    png_save_filepath = os.path.join('temp_lib', png.filename)
    png.save(png_save_filepath)

    command = './png-extractGIF '+ png_save_filepath + ' hidden.gif' 
    cmd_resp = os.system(command)
    print('command', cmd_resp)
    
    if cmd_resp == 0 :
      print('cmdresp:\t', cmd_resp)
      try: 
        if os.path.exists('hidden.gif') == False:
          return "ERROR: PNG was not read correctly", 500
        else:
          send = send_file('hidden.gif', attachment_filename='hidden.gif')
          print('send:\t', send)
          os.remove('hidden.gif')
          return send, 200

      except Exception as exc:
        print('EXCEPTION:\t', exc)
        return "ERROR: PNG may not have a hidden gif", 500