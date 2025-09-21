# Instagram Profile Clone

Sebuah clone halaman profil Instagram yang dibuat menggunakan HTML, CSS, dan framework Tailwind CSS serta Bootstrap. Proyek ini meniru tampilan dan nuansa halaman profil Instagram dengan desain yang responsif dan modern.

## 📸 Preview

Proyek ini menampilkan halaman profil Instagram dengan:
- Foto profil bulat
- Informasi pengguna (nama, bio, statistik)
- Tombol edit profil dan pengaturan
- Area highlight stories
- Grid foto/postingan


## 🛠️ Teknologi yang Digunakan

- **HTML5**: Struktur dasar halaman
- **Tailwind CSS & Bootstrap 5.3.8**: Dua framework yang dipakai
- **Bootstrap Icons**: Icon set untuk elemen UI
- **Font Awesome**: Library Ikon
- **Google Fonts (Roboto)**: Typography
- **CSS**: Styling Custom Sendiri
- **Assets Lokal**: Foto, dll dari penyimpanan dekstop

## 📁 Struktur Proyek

```
tugas2/
├── Bootstrap/
│ ├── index.html
│ └── assets/
│ └── img/
│ ├── foto1.jpg
│ ├── foto2.jpg
│ ├── foto3.jpg
│ ├── ... (total 17 gambar)
│
├── Tailwind/
│ ├── index.html
│ └── assets/
│ └── img/
│ ├── foto1.jpg
│ ├── foto2.jpg
│ ├── foto3.jpg
│ ├── ... (total 17 gambar)
│
└── README.md
```

## 🚀 Cara Menjalankan

1. **Clone atau download** proyek ini
2. **Buka file `index.html`** di browser web Anda
3. Halaman akan langsung ditampilkan tanpa perlu server khusus

```bash
# Jika menggunakan Git
git clone [repository-url]
cd instagram-profile-clone

# Buka di browser
open index.html
# atau
start index.html
```

## 📱 Fitur Responsif

Proyek ini dioptimalkan untuk berbagai ukuran layar:

- **Desktop**: Layout horizontal dengan foto profil besar
- **Tablet**: Layout yang disesuaikan dengan elemen yang tetap proporsional  
- **Mobile**: Layout vertikal dengan elemen yang terpusat

### Breakpoints yang Digunakan:

### Tailwind
- `sm`: 640px ke atas
- `md`: 768px ke atas 

### Bootstrap
- `sm`: 576px
- `md`: 768px 
- `lg`: 992px 

## 🎨 Komponen Utama

### 1. Header Profile
- **Foto Profil**: Gambar bulat responsif 
- **Info Pengguna**: Nama, tombol aksi, dan statistik
- **Tombol**: Ikuti, Edit Profile, dan panah kebawah
- **Statistik**: Kiriman, Pengikut, Diikuuti

### 2. Bio Section
- Nama pengguna
- Deskripsi singkat
### 3. Highlights Section
- Area untuk Instagram Stories highlights

### 4. Posts Grid
- Grid 3 kolom untuk menampilkan foto
- Gambar yang responsive dan cover penuh
- Gap yang konsisten antar gambar

## 🎯 Kustomisasi

### Mengubah Profil
Untuk mengubah informasi profil, edit bagian berikut di `index.html`:

```html
<!-- Foto Profil -->
<img src="GANTI_URL_FOTO_ANDA" alt="My Profile Picture" />

<!-- Nama Pengguna -->
<h1 class="font-light text-lg mb-0">andiiffatur</h1>

<!-- Bio -->
<p>Ain't Gonna Lie DUDE!</p>
<p>Tokoh Publik</p>
```

## 📦 Dependencies (CDN)

Proyek ini menggunakan CDN untuk semua dependencies:

- **Tailwind CSS**: `@tailwindcss/browser@4`
- **Bootstrap**: `5.3.8`
- **Bootstrap Icons**: `1.13.1`
- **Google Fonts**: `Roboto font family`

## 🌟 Keunggulan

- ✅ **Fully Responsive** - Bekerja di semua device
- ✅ **Modern Design** - Mengikuti design system Instagram
- ✅ **Dark Theme** - Tema gelap yang nyaman di mata
- ✅ **Fast Loading** - Menggunakan CDN untuk performa optimal
- ✅ **Cross Browser** - Compatible dengan browser modern
- ✅ **Clean Code** - HTML yang terstruktur dan mudah dipahami

## 🔧 Pengembangan Lebih Lanjut

Untuk pengembangan selanjutnya, Anda dapat menambahkan:

- **JavaScript Interactivity**: Modal untuk gambar, like button, comments
- **Backend Integration**: Koneksi dengan database untuk data dinamis
- **Authentication**: Sistem login/register
- **Real Posts**: Upload dan manajemen postingan
- **Stories Feature**: Implementasi Instagram Stories
- **Following System**: Sistem follow/unfollow
