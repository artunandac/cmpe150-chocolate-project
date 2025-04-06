# 🍫 cmpe150-chocolate-parcel

Bu proje, CMPE150 (Bilgisayara Giriş) dersi kapsamında geliştirilmiştir.  
Amaç, sınırlı sayıda küçük, orta ve büyük boy çikolatayı kullanarak istenen bir hedef ağırlığı **mümkünse büyük çikolataları öncelikli kullanarak** tam olarak oluşturmaktır.

---

## 📌 Proje Tanımı

**Problem:**  
Verilen hedef bir ağırlığa ulaşmak için elinizdeki küçük, orta ve büyük çikolatalardan belirli sayılarda vardır. Amaç bu çikolataları kullanarak:

- Hedef ağırlığa **tam olarak** ulaşmak,
- Mümkün olan en fazla **büyük**, sonra **orta**, sonra **küçük** çikolatayı kullanmak,
- Eğer böyle bir kombinasyon mümkün değilse `-1 -1 -1` çıktısı vermektir.

---

## 📥 Girdi Formatı

Boşlukla ayrılmış 7 tam sayı:

```
<hedef_ağırlık> <adet_küçük> <ağırlık_küçük> <adet_orta> <ağırlık_orta> <adet_büyük> <ağırlık_büyük>
```

---

## 📤 Çıktı Formatı

Uygun kombinasyon bulunduysa:

```
<kullanılan_küçük> <kullanılan_orta> <kullanılan_büyük>
```

Uygun kombinasyon yoksa:

```
-1 -1 -1
```

---

## 🔍 Örnekler

### ✅ Örnek 1
```
Girdi:   27 4 2 3 5 3 9
Çıktı:   3 1 2
```
Açıklama: 2×9 + 1×5 + 3×2 = 27 gram

---

### ❌ Örnek 2
```
Girdi:   30 2 2 2 3 2 10
Çıktı:   -1 -1 -1
```
Açıklama: Elinizdeki çikolatalarla 30 grama ulaşmak mümkün değil.

---

## 🚀 Çalıştırma

Bu programı çalıştırmak için terminalde şunu yazmanız yeterli:

```bash
python3 chocolate.py
```

7 adet tam sayıyı boşlukla girmeniz istenir.

---

## 📁 Dosya Yapısı

```
cmpe150-chocolate-parcel/
├── chocolate.py      # Python kaynak dosyası
├── README.md         # Bu doküman
```

---

## 💡 Proje Vurguları

- ✔️ Temiz ve okunabilir Python kodu
- 🧠 Greedy yaklaşım ile algoritmik çözüm
- 🧪 Edge-case’ler ve sınırlı kaynak kontrolü
- 📚 Yorumlu, anlaşılır yapı
- 🧰 Komut satırı dostu kullanım

---

## 👨‍💻 Hakkımda

Ben, mühendislik bakış açısına sahip bir tıp öğrencisiyim. Yazılım geliştirme, algoritmik düşünme ve donanım-yazılım entegrasyonu konularına ilgi duyuyorum.  
Bu proje, **sistematik problem çözme**, **temiz kod yazımı** ve **dokümantasyon becerilerimi** ortaya koymaktadır.

📫 İletişim: GitHub üzerinden mesaj atabilirsiniz. (İsteğe bağlı olarak e-posta eklenebilir.)

---

## 🏷️ Etiketler

`Python` `Greedy Algorithm` `CMPE150` `Algorithmic Thinking` `Course Project` `Optimization`

---

# 🍫 cmpe150-chocolate-parcel (English)

This project was developed for the CMPE150 (Introduction to Computing) course.

Its purpose is to determine whether a given target weight can be reached by using available small, medium, and large chocolates — prioritizing larger chocolates where possible.

---

## 📌 Project Description

**Problem:**  
You are given limited numbers of small, medium, and large chocolates, each with specific weights. Your goal is to:

- Reach a **target weight exactly**,
- Use the maximum number of **large**, then **medium**, then **small** chocolates,
- If no valid combination exists, return `-1 -1 -1`.

---

## 📥 Input Format

Seven space-separated integers:

```
<target_weight> <n_small> <w_small> <n_medium> <w_medium> <n_large> <w_large>
```

---

## 📤 Output Format

If a valid combination is found:

```
<used_small> <used_medium> <used_large>
```

Otherwise:

```
-1 -1 -1
```

---

## 🔍 Examples

### ✅ Example 1
```
Input:   27 4 2 3 5 3 9
Output:  3 1 2
```
Explanation: 2×9 + 1×5 + 3×2 = 27 grams ✅

---

### ❌ Example 2
```
Input:   30 2 2 2 3 2 10
Output:  -1 -1 -1
```
Explanation: No valid combination possible ❌

---

## 🚀 How to Run

Run in terminal using:

```bash
python3 chocolate.py
```

Then input 7 space-separated integers as prompted.

---

## 📁 File Structure

```
cmpe150-chocolate-parcel/
├── chocolate.py      # Main Python script
├── README.md         # This file
```

---

## 🌟 Project Highlights

- ✅ Clean, well-structured Python code
- 🧠 Greedy algorithmic logic
- 🧪 Edge case and constraint-aware
- 📚 Fully documented and beginner-friendly
- ⚙️ Terminal-based usage

---

## 🙋 About Me

I am a medical student with an engineering mindset, passionate about software development, systems integration, and problem solving.  
This project reflects my ability to **think algorithmically**, write **clean code**, and document projects effectively.

📫 Contact: Feel free to reach out via GitHub. (Optional: add email)

---

## 🏷️ Tags

`Python` `Greedy` `Optimization` `Student Project` `CMPE150` `Algorithmic Problem Solving`
