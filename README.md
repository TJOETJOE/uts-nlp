# 🌐 **UTS NLP – Sentiment Analysis of YouTube Comments**

Mata Kuliah: **IF400105 – Natural Language Processing**
Prodi: **Teknik Informatika**
Universitas Halim Sanusi PUI Bandung
Tahun Akademik **2025/2026**

---

# 📌 **Deskripsi Proyek**

Proyek ini merupakan implementasi UTS mata kuliah **Natural Language Processing**, yang bertujuan untuk menganalisis sentimen komentar pada salah satu video YouTube.

Analisis mencakup proses:
✔ Scraping komentar YouTube
✔ Pembersihan teks
✔ Preprocessing NLP
✔ Auto-labeling sentimen (TextBlob)
✔ Pemodelan Machine Learning
✔ Prediksi sentimen seluruh dataset
✔ Analisis hasil sentimen

Total komentar yang dianalisis:
👉 **1500 komentar YouTube** (3 file × 500 komentar)

---

# 📁 **Struktur Repo**

```
uts-nlp/
│
├── scraping/
│   ├── Copy_of_YoutubeCommentsCrawlerV2.ipynb
│   ├── copy_of_youtubecommentscrawlerv2.py
│
├── code/
│   ├── sentiment_analysis.ipynb
│   ├── sentiment_analysis.py
│
├── dataset/
│   ├── youtube-comments1.csv
│   ├── youtube-comments2.csv
│   ├── youtube-comments3.csv
│
├── README.md
├── .gitignore
```

---

# 🧹 **1. Scraping Data YouTube**

Scraping dilakukan menggunakan **YouTube Data API v3** dengan endpoint:

```
commentThreads().list(part='snippet,replies', videoId=VIDEO_ID)
```

Pagination ditangani menggunakan `nextPageToken` hingga seluruh komentar diperoleh.

* Total file: **3 CSV**
* Total komentar: **1500**
* Kolom dataset:

  * `publishedAt`
  * `authorDisplayName`
  * `textDisplay`
  * `likeCount`

---

# 🧼 **2. Cleaning Data**

Cleaning dilakukan untuk menghilangkan noise pada teks.

Tahapan:

* lowercase
* hapus URL
* hapus mention `@username`
* hapus simbol & emoji
* hapus spasi berlebih

Kode:

```python
def cleaning(text):
    text = text.lower()
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"@\w+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
```

Hasil disimpan pada kolom **`clean_text`**.

---

# 🔧 **3. Preprocessing (NLP)**

Karena komentar berbahasa Inggris, preprocessing menggunakan:

* Tokenization (NLTK)
* Stopword removal
* Lemmatization (WordNet)

Kode:

```python
def preprocess(text):
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(tokens)
```

Hasil disimpan ke **`prep_text`**.

---

# 🧪 **4. Auto Sentiment Labeling**

Komentar diberi label secara otomatis menggunakan **TextBlob polarity**:

* polarity > 0 → *positive*
* polarity < 0 → *negative*
* polarity = 0 → *neutral*

Hasil sentimen disimpan pada kolom **`sentiment`**.

---

# 🤖 **5. Machine Learning Modeling**

Dua model machine learning digunakan:

---

## 🔹 **Model 1: Multinomial Naive Bayes**

TF-IDF digunakan sebagai fitur:

```python
tfidf = TfidfVectorizer(ngram_range=(1,2), min_df=2, max_df=0.95)
```

Model:

```python
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
```

---

## 🔹 **Model 2: Logistic Regression**

```python
logreg_model = LogisticRegression(max_iter=1000)
logreg_model.fit(X_train_tfidf, y_train)
```

---

## 🔍 **Evaluasi Model**

Evaluasi dilakukan menggunakan:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

Model terbaik digunakan untuk memprediksi seluruh dataset (**Naive Bayes** yang digunakan dalam prediksi final).

---

# 📊 **6. Hasil Analisis Sentimen (1500 komentar)**

Hasil prediksi pada seluruh dataset:

| Sentimen     | Jumlah   | Persentase |
| ------------ | -------- | ---------- |
| **Positive** | **957**  | **63.8%**  |
| **Neutral**  | **407**  | **27.1%**  |
| **Negative** | **136**  | **9.1%**   |
| **Total**    | **1500** | 100%       |

---

# 📝 **7. Kesimpulan**

Berdasarkan analisis sentimen terhadap 1500 komentar YouTube:

* **Mayoritas komentar (63.8%) adalah positif**, menunjukkan bahwa topik video tersebut mendapat sambutan yang baik dari penonton.
* Komentar **neutral** cukup besar (27.1%), biasanya berupa informasi atau opini tanpa emosi kuat.
* Komentar **negatif** relatif sedikit (9.1%), menunjukkan minimnya kritik keras.
* Pemodelan machine learning dengan **Naive Bayes + TF-IDF** berhasil memprediksi sentimen dengan baik, dan pipeline NLP membantu meningkatkan kualitas data sebelum modeling.

Proyek ini telah menyelesaikan semua instruksi UTS:
✔ Scraping
✔ Cleaning
✔ Preprocessing
✔ Modeling
✔ Analisis hasil
✔ Dokumentasi

---

# ▶️ **8. Cara Menjalankan Proyek**

Clone repo:

```
git clone https://github.com/TJOETJOE/uts-nlp.git
cd uts-nlp
```

Install dependencies:

```
pip install pandas nltk textblob scikit-learn
```

Jalankan notebook:

* `scraping/Copy_of_YoutubeCommentsCrawlerV2.ipynb`
* `code/sentiment_analysis.ipynb`

---

# 📎 **9. Lampiran**

Tambahkan screenshot berikut ke repo atau laporan:

* Screenshot video YouTube
* Screenshot komentar
* Screenshot scraping berjalan
* Screenshot preprocessing
* Screenshot hasil akurasi model
* Screenshot grafik hasil sentimen




