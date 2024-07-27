from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

playlists = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/playlists')
def playlist_list():
    return render_template('playlist_list.html', playlists=playlists)

@app.route('/playlist/create', methods=['GET', 'POST'])
def create_playlist():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        playlists.append({'title': title, 'description': description})
        return redirect(url_for('playlist_list'))
    return render_template('playlist_form.html', action='create')

@app.route('/playlist/edit/<int:index>', methods=['GET', 'POST'])
def edit_playlist(index):
    if index < 0 or index >= len(playlists):
        return "Playlist não encontrada", 404
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        playlists[index] = {'title': title, 'description': description}
        return redirect(url_for('playlist_list'))
    playlist = playlists[index]
    return render_template('playlist_form.html', action='edit', playlist=playlist, index=index)

@app.route('/playlist/delete/<int:index>', methods=['POST'])
def delete_playlist(index):
    if index < 0 or index >= len(playlists):
        return "Playlist não encontrada", 404
    playlists.pop(index)
    return redirect(url_for('playlist_list'))

if __name__ == '__main__':
    app.run(debug=True)
