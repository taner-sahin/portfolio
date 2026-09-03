# Taner Şahin | Django Backend Developer Portfolio

Bu proje, Django Backend Developer olarak geliştirdiğim projeleri, teknik yeteneklerimi, özgeçmişimi ve iletişim bilgilerimi tek bir profesyonel portföy sitesi altında sunmak amacıyla geliştirilmiştir.

Portföy sitesi Django ile geliştirilmiştir ve backend odaklı kariyer yolculuğumu sergilemektedir.

Ana hedefler:

- Django backend projelerini tek bir yerde sunmak
- Canlı uygulama, GitHub, demo video ve vaka analizi bağlantılarını göstermek
- Teknik yetenekleri ve kullanılan teknolojileri sergilemek
- CV'ye kolay erişim sağlamak
- İşverenlerin ve teknik ekiplerin projeleri hızlı şekilde inceleyebilmesini sağlamak
- Yeni projeler tamamlandıkça portföyü büyütmek

## Öne Çıkan Proje

### CareerTrack

CareerTrack; iş başvurularını, şirketleri, görüşmeleri, notları ve hatırlatıcıları yönetmek için geliştirdiğim Django tabanlı backend uygulamasıdır.

Başlıca özellikler:

- Authentication
- CRUD işlemleri
- Django ORM
- PostgreSQL
- Kullanıcı bazlı veri izolasyonu
- Global Search
- Gelişmiş raporlama
- CSV / PDF export
- 114 otomatik test
- Ubuntu VPS deployment
- Gunicorn
- Nginx
- HTTPS / SSL

CareerTrack için ayrıca portföy içerisinde ayrı bir teknik vaka analizi sayfası bulunmaktadır.

## Kullanılan Teknolojiler

- Python
- Django
- HTML
- CSS
- Bootstrap
- JavaScript
- PostgreSQL
- Git
- GitHub
- Linux / Ubuntu
- Gunicorn
- Nginx

## Portfolio Özellikleri

- Responsive tasarım
- Proje vitrini
- CareerTrack detay alanı
- CareerTrack vaka analizi
- GitHub bağlantıları
- Demo video bağlantısı
- CV görüntüleme ve indirme
- LinkedIn bağlantısı
- E-posta iletişimi
- Aktif navbar takibi
- Özel 404 ve 500 sayfaları

## Testler

Portfolio projesinde temel sayfaların erişilebilirliğini doğrulayan otomatik testler bulunmaktadır.

Şu anda test edilen temel akışlar:

- Ana sayfanın başarılı şekilde açılması
- CareerTrack vaka analizi sayfasının başarılı şekilde açılması

Testleri çalıştırmak için:

```bash
python manage.py test
```

Django sistem kontrolünü çalıştırmak için:

```bash
python manage.py check
```

## Lokal Kurulum

Projeyi klonlayın:

```bash
git clone https://github.com/taner-sahin/portfolio.git
cd portfolio
```

Virtual environment oluşturun:

```bash
python -m venv venv
```

Windows üzerinde virtual environment'ı aktif edin:

```bash
venv\Scripts\activate
```

Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

Environment değişkenlerini yapılandırın.

Ardından migration işlemlerini çalıştırın:

```bash
python manage.py migrate
```

Development sunucusunu başlatın:

```bash
python manage.py runserver
```

Development sunucusu varsayılan olarak şu adreste çalışır:

```text
http://127.0.0.1:8000/
```

## Production

Portfolio, production ortamında Linux tabanlı bir VPS üzerinde çalışacak şekilde hazırlanmıştır.

Production yapısında:

- Ubuntu
- PostgreSQL
- Gunicorn
- Nginx
- HTTPS / SSL
- Environment variables
- `DEBUG=False`

kullanılması hedeflenmektedir.

### Canlı Portfolio

Portfolio deployment tamamlandığında ana adres:

**https://tanersahindev.com**

olacaktır.

## CareerTrack Bağlantıları

### GitHub

https://github.com/taner-sahin/careertrack

### Demo Video

https://github.com/taner-sahin/careertrack/releases/download/v1.0.0/careertrack-demo.mp4

CareerTrack canlı uygulama adresi, portfolio deployment mimarisi tamamlandıktan sonra güncellenecektir.

## Gelişim Planı

Portfolio yeni backend projeleri tamamlandıkça güncellenmeye devam edecektir.

Planlanan proje sırası:

**CareerTrack → Portfolio V1 → ClientTrack / CRM → ShopAPI / DRF → İkinci REST API → TeamBoard → DockerCart → JobReady**

Yeni projeler tamamlandıkça portfolio içerisindeki proje alanları gerçek proje bilgileriyle güncellenecektir.

Her ciddi proje için mümkün olduğunda aşağıdaki sunum standardı uygulanacaktır:

**GitHub + Live Demo + Demo Video + Case Study**

## İletişim

**Taner Şahin**  
Django Backend Developer

GitHub:  
https://github.com/taner-sahin

LinkedIn:  
https://www.linkedin.com/in/taner-%C5%9Fahin-079980410/

E-posta:  
kemal.liya19@gmail.com

---

Bu portfolio, backend geliştirme sürecinde edindiğim teknik deneyimleri ve tamamladığım gerçek projeleri sergilemek amacıyla geliştirilmektedir.