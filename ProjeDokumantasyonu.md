
# Proje Dokümantasyonu  
**Proje Adı:** Gerçek Zamanlı Gramer Tabanlı Sözdizimi Vurgulayıcı  
**Ders:** Programlama Dilleri Projesi  
**Hazırlayan:** Hilal Kaya  



## 1. Dil ve Gramer Seçimi

Bu projede programlama dili olarak **Python 5** seçilmiştir. Kullanıcıdan alınan kodların sözdizimsel olarak analiz edilmesini sağlamak için, C benzeri basitleştirilmiş bir dil grameri oluşturulmuştur.

### Gramer Özeti:
- Değişken tanımlama: `int x;`
- Atama: `x = 5 + 3;`
- Koşullu ifadeler: `if (x > 3) { ... }`
- Döngüler: `while (x < 10) { ... }`


## 2. Sözdizimsel Analiz Süreci

Sözdizimsel analiz işlemi, **top-down** yöntem kullanılarak gerçekleştirilmiştir. Her gramer kuralı için `parser.py` içinde ayrı bir Python fonksiyonu tanımlanmıştır. Örnek olarak:
- `statement()` → her tür ifadeyi tanımlar
- `expression()` → aritmetik ve karşılaştırmalı ifadeleri işler


## 3. Leksik Analiz Ayrıntıları

**`lexer.py`** dosyasında Python’un `re` modülüyle düzenli ifadeler kullanılmıştır. Girişteki kod satırları şu token türlerine ayrılır:
- `KEYWORD`: int, float, if, while, return
- `IDENTIFIER`: Değişken ve fonksiyon isimleri
- `NUMBER`: Sayılar
- `OPERATOR`: +, -, *, /, =, ==, >, <, !=
- `DELIMITER`: ;, (, ), {, }
- `UNKNOWN`: Tanımlı olmayan karakterler

Token'lar `Token` sınıfı ile nesneleştirilmiştir.


## 4. Parser Yöntemi

Parser, **recursive descent parser** türünde, yani top-down olarak çalışmaktadır. `expression()`, `term()`, `factor()` gibi yapılar klasik gramer ağacı takibini sağlar. Hatalar `SyntaxError` ile kontrol edilir ve GUI üzerinden kullanıcıya gösterilir.


## 5. Renklendirme Şeması

Gerçek zamanlı sözdizimi vurgulama işlemi `QSyntaxHighlighter` sınıfı ile yapılmaktadır. Her token türü için özel bir renk ve biçim tanımlanmıştır:
- `KEYWORD`: Mavi ve kalın
- `IDENTIFIER`: Siyah
- `NUMBER`: Mor
- `OPERATOR`: Kırmızı
- `DELIMITER`: Yeşil
- `UNKNOWN`: Gri ve kalın

## 6. Arayüz (GUI) Gerçekleştirme

**Qt Designer** kullanılarak `.ui` formatında bir arayüz tasarlanmıştır. Bu arayüz `main.py` içinde `uic.loadUi()` fonksiyonu ile yüklenmektedir.

### Kullanılan Bileşenler:
- `QTextEdit`: Kod giriş alanı
- `QLabel`: Hata veya başarı mesajı alanı
- `QPushButton`: (isteğe bağlı) Manuel analiz tetikleyici
- `textChanged` sinyali ile her değişiklikte analiz yapılır


## 7. Gerçek Zamanlılık

Kullanıcı editörde her yazdığında:
- Kod otomatik olarak tokenize edilir
- Parser tarafından analiz edilir
- Vurgulama ve hata bilgisi anında güncellenir

Böylece gerçek zamanlı bir kullanıcı deneyimi sağlanır.
