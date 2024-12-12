from flask import Flask
import random

app = Flask(__name__)  # Burada __name__ kullanmalısın

# Ana sayfa rotası
@app.route("/")
def hayat_hikayesi():
    return """
    <h1>Oyuncuların hayat hikayesi:</h1>
    <a href="/oyuncularin_hayat_hikayesi">Futbol oyuncularının hayat hikayesini öğrenmek ister misin?</a>
    """

# Oyuncuların hayat hikayesi rotası
@app.route("/oyuncularin_hayat_hikayesi")
def random_story():
    hikayeler = [
        "Lionel Messi: Arjantin'den Barcelona'ya uzanan bir başarı hikayesi, yetenek ve azmin simgesi.",
        "Cristiano Ronaldo: Madeira'dan dünya sahnelerine yükselen bir yıldız, çalışkanlığı ve kararlılığı ile tanınır.",
        "Neymar Jr.: Brezilya sokaklarında başlayan futbol kariyeri, dünya çapında bir fenomen haline geldi.",
        "Kylian Mbappé: Genç yaşta sahalarda parlayan Fransız yıldız, hız ve becerisiyle dikkat çekti."
    ]
    story = random.choice(hikayeler)
    return f"""
    <h1>Rastgele Futbol Oyuncusu Hikayesi</h1>
    <p>{story}</p>
    <a href="/">Anasayfa</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
