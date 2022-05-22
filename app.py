from flask import Flask, url_for, render_template, redirect, send_file, request, session
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = "!2345@abc"

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session['link'] = request.form.get('url')
        url = YouTube(session['link'])
        return render_template('see_video.html', url=url)
    return render_template('index.html')


@app.route('/see-video',methods=['GET','POST'])
def see_video():
    if request.method =='POST':
        url = YouTube(session['link'])
        itag = request.form.get('itag')
        video = url.streams.get_by_itag(itag)
        filename = video.download()
        return send_file(filename,as_attachment=True)
    return redirect(url_for('index'))


@app.route('/contact')
def contact():
    return render_template('contact.html')







if __name__ =="__main__":
    app.run(debug=False,host='0.0.0.0', port=5000)
