
---

# 🌐 **UTS NLP – Sentiment Analysis of YouTube Comments**

Mata Kuliah: **IF400105 – Natural Language Processing**
Prodi: **Teknik Informatika**
Universitas Halim Sanusi PUI Bandung
Tahun Akademik **2025/2026**

---

# 📌 **Deskripsi Proyek**

Proyek ini adalah implementasi UTS mata kuliah **Natural Language Processing**, dengan tujuan melakukan **analisis sentimen komentar YouTube** terhadap sebuah topik tertentu.

Analisis dilakukan melalui langkah-langkah berikut:

1. **Scraping komentar YouTube** menggunakan YouTube Data API
2. **Menggabungkan dataset** (3 file CSV × 500 komentar = total 1500 komentar)
3. **Cleaning dan preprocessing teks**
4. **Sentiment auto-labeling** menggunakan TextBlob
5. **Pemodelan machine learning** menggunakan:

   * Multinomial Naive Bayes
   * Logistic Regression
6. **Prediksi sentimen seluruh dataset**
7. **Analisis hasil sentimen positif/negatif/neutral**

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

Komentar YouTube diambil menggunakan **YouTube Data API v3** melalui endpoint:

```
commentThreads().list(part='snippet,replies', videoId=VIDEO_ID)
```

Scraping dilakukan bertahap menggunakan `nextPageToken` sampai seluruh komentar diambil.

* Total file: **3 CSV**
* Jumlah per file: **500 komentar**
* Total dataset: **1500 komentar**

Kolom hasil scraping:

* `publishedAt`
* `authorDisplayName`
* `textDisplay`
* `likeCount`

---

# 🧼 **2. Cleaning Data**

Komentar dibersihkan menggunakan fungsi:

```python
def cleaning(text):
    text = text.lower()
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"@\w+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
```

Cleaning menghilangkan:

✔ URL
✔ Mention `@user`
✔ Emoji dan simbol
✔ White spaces berlebih
✔ Huruf besar → kecil

Hasil disimpan pada kolom **`clean_text`**.

---

# 🔧 **3. Preprocessing**

Preprocessing dilakukan dalam **bahasa Inggris** karena komentar berbahasa Inggris.

Tahapan:

* Tokenization
* Stopword removal (NLTK English stopwords)
* Lemmatization (WordNetLemmatizer)

Kode:

```python
def preprocess(text):
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(tokens)
```

Hasil disimpan di kolom **`prep_text`**.

---

# 🧪 **4. Auto Sentiment Labeling**

Karena komentar tidak memiliki label asli, digunakan auto-labeling menggunakan **TextBlob Polarity**:

* polarity > 0 → **positive**
* polarity < 0 → **negative**
* polarity = 0 → **neutral**

```python
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"
```

Label disimpan dalam kolom **`sentiment`**.

---

# 🤖 **5. Modeling Machine Learning**

Dua model digunakan:

---

### 🔵 **Model 1: Multinomial Naive Bayes**

Menggunakan TF-IDF sebagai fitur:

```python
tfidf = TfidfVectorizer(ngram_range=(1,2), min_df=2, max_df=0.95)
```

Model:

```python
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
```

### 📈 **Hasil Evaluasi:**

(Akan muncul dari output code, isi manual setelah dijalankan)

Misalnya:

* Accuracy: **0.82**
* Precision, Recall, F1 tiap kelas
* Confusion matrix

---

### 🔵 **Model 2: Logistic Regression**

```python
logreg_model = LogisticRegression(max_iter=1000)
```

### 📈 **Hasil Evaluasi:**

(isi sesuai output Colab)

Contoh:

* Accuracy: **0.85**
* Precision, Recall, F1 lebih stabil dibanding Naive Bayes

---

# 🧮 **6. Prediksi 1500 Komentar**

Model dengan akurasi terbaik (Logistic Regression atau Naive Bayes) digunakan untuk memprediksi seluruh komentar:

```python
all_data['pred_sentiment'] = nb_model.predict(X_all_tfidf)
```

---

# 📊 **7. Hasil Analisis Sentimen**

(Angka di bawah ini kamu isi dari output sebenarnya)

| Sentimen  | Jumlah   |
| --------- | -------- |
| Positive  | XXX      |
| Negative  | XXX      |
| Neutral   | XXX      |
| **Total** | **1500** |

---

# 📝 **8. Kesimpulan**

Berdasarkan hasil analisis sentimen pada **1500 komentar YouTube**, dapat disimpulkan:

* Mayoritas komentar bernada **(positif / negatif / netral)**.
* Model machine learning dengan performa terbaik adalah **(Naive Bayes atau Logistic Regression)**.
* Proses NLP seperti **cleaning, preprocessing, dan TF-IDF** membantu meningkatkan akurasi model.
* Proyek ini berhasil memenuhi semua instruksi UTS:
  ✔ Scraping
  ✔ Cleaning
  ✔ Preprocessing
  ✔ Machine Learning Modeling
  ✔ Analisis Hasil Sentimen
  ✔ Dokumentasi Proyek

---

# ▶ **9. Cara Menjalankan Proyek**

### 1. Clone repo:

```
git clone https://github.com/TJOETJOE/uts-nlp.git
```

### 2. Jalankan notebook:

* `scraping/Copy_of_YoutubeCommentsCrawlerV2.ipynb` untuk scraping
* `code/sentiment_analysis.ipynb` untuk NLP & ML

### 3. Install dependency:

```
pip install textblob nltk scikit-learn pandas
```

### 4. Jalankan seluruh sel notebook.

---

# 📎 **10. Lampiran (Screenshot)**

Tambahkan di repo:
✔ Screenshot video YouTube
✔ Screenshot komentar
✔ Screenshot scraping berjalan
✔ Screenshot model ML (accuracy report)
✔ Screenshot plot hasil sentimen

---


