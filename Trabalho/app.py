from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


playlists = []
musicas = []

class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

@app.route("/")
def index():
    return render_template("index.html", playlists=playlists)

@app.route("/criar_playlist", methods=["GET", "POST"])
def criar_playlist():
    if request.method == "POST":
        nome = request.form["nome"]
        playlist = Playlist(nome)
        playlists.append(playlist)
        return redirect(url_for("index"))
    return render_template("criar_playlist.html")

@app.route("/adicionar_musica/<int:playlist_id>", methods=["GET", "POST"])
def adicionar_musica(playlist_id):
    playlist = playlists[playlist_id]
    if request.method == "POST":
        nome = request.form["nome"]
        artista = request.form["artista"]
        duracao = request.form["duracao"]
        musica = Musica(nome, artista, duracao)
        playlist.musicas.append(musica)
        return redirect(url_for("index"))
    return render_template("adicionar_musica.html", playlist=playlist)

@app.route("/remover_musica/<int:playlist_id>/<int:musica_id>")
def remover_musica(playlist_id, musica_id):
    playlist = playlists[playlist_id]
    musica = playlist.musicas[musica_id]
    playlist.musicas.remove(musica)
    return redirect(url_for("index"))

@app.route("/editar_playlist/<int:playlist_id>", methods=["GET", "POST"])
def editar_playlist(playlist_id):
    playlist = playlists[playlist_id]
    if request.method == "POST":
        nome = request.form["nome"]
        playlist.nome = nome
        return redirect(url_for("index"))
    return render_template("editar_playlist.html", playlist=playlist)

@app.route("/deletar_playlist/<int:playlist_id>")
def deletar_playlist(playlist_id):
    playlist = playlists[playlist_id]
    playlists.remove(playlist)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)