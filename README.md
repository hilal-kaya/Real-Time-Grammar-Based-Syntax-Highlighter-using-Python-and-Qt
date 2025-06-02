# Real-Time-Grammar-Based-Syntax-Highlighter-using-Python-and-Qt

## Proje Özeti

Bu proje, belirli bir gramer temeline dayalı gerçek zamanlı sözdizimi vurgulayıcı bir uygulama geliştirir. 
Uygulama:

Düzenli ifadelerle leksik analiz yapar
Recursive descent yöntemiyle sözdizimi analizini gerçekleştirir
PyQt5 ve Qt Designer kullanarak grafik arayüz sunar
Kod yazarken anında vurgulama ve hata bildirimi yapar

## Kullanılan Teknolojiler

Python 3
PyQt5 (grafik arayüz için)
Qt Designer (.ui dosyası)
Python re modülü (regex ile token üretimi)
Dil ve Gramer Yapısı

Uygulama, C diline benzer basitleştirilmiş bir dil grameri üzerine kuruludur. 
Desteklenen ifadeler:

Değişken tanımlama: int x;
Atama: x = 5 + 3;
Koşul ifadeleri: if (x > 3) { ... }
Döngüler: while (x < 10) { ... }

## Örnek Gramer (EBNF benzeri)
STATEMENT ::= VAR_DECLARATION | ASSIGNMENT | IF_STATEMENT | WHILE_STATEMENT
VAR_DECLARATION ::= TYPE IDENTIFIER ";"
ASSIGNMENT ::= IDENTIFIER "=" EXPRESSION ";"
EXPRESSION ::= TERM (("+" | "-") TERM)* (KARSILASTIRMA_OP TERM)?


✨ Uygulamanın Temel Özellikleri

Token türlerine göre renkli vurgulama:
Anahtar kelimeler (mavi)
Tanımlayıcılar (siyah)
Sayılar (mor)
Operatörler (kırmızı)
Ayraçlar (yeşil)
Geçersiz karakterler (gri)
Gerçek zamanlı analiz ve geri bildirim
Hatalı sözdiziminde kullanıcıya mesaj gösterme


## Teknik Gerçekleştirme

lexer.py: Regex ile metni tokenlara ayırır
parser.py: Token akışını gramer kurallarına göre işler
highlighter.py: QSyntaxHighlighter ile vurgulama yapar
main.py: GUI'yi çalıştırır ve sinyalleri bağlar

# Karşılaşılan Zorluklar

>, <, == gibi karşılaştırma operatörlerinin lexer ve parser’a eklenmesi
Gerçek zamanlı kontrol yaparken performans kaybı yaşamamak
Dış syntax kütüphanelerine başvurmadan çözüm üretmek

# Sonuç:

Uygulama, kendi yazılmış analiz motoru ve kullanıcı dostu arayüzüyle gramer tabanlı vurgulayıcı işlevini başarıyla yerine getirir. Öğrencinin dil kavrayışını artıracak şekilde geri bildirim sunar.

🎥 Demo Videosu

https://youtu.be/rqj7ixQ1AYI?si=0ECi8-e3Ta3P_VaZ

📝 Makale Linki




▶️ Çalıştırma Talimatı

Gereksinimleri kur: pip install PyQt5
Terminalden çalıştır: python main.py
Kod yazmaya başlayın, anında vurgulama aktif olur.
Hazırlayan: Hilal Kaya
Ders: Programlama Dilleri Projesi
