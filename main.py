#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
THE MYSTERY ADVENTURE BOT
Petualangan Interaktif Pencarian Harta Karun di Panjatan
Karakter Utama: Titi
"""

import time
import os
from typing import Dict, List, Tuple

class MysteryAdventureBot:
    def __init__(self):
        self.name = "Titi"
        self.health = 100
        self.energy = 100
        self.inventory = []
        self.visited_locations = set()
        self.completed_quests = set()
        self.money = 0
        self.current_location = "Desa Panjatan"
        self.game_over = False
        self.ending_type = None
        
    def clear_screen(self):
        """Membersihkan layar terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def slow_print(self, text: str, delay: float = 0.03):
        """Mencetak teks dengan efek mengetik"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def display_stats(self):
        """Menampilkan status pemain"""
        print(f"\n┌─────────────────────────────────────────┐")
        print(f"│ Nama     : {self.name:<30} │")
        print(f"│ Lokasi   : {self.current_location:<30} │")
        print(f"│ Kesehatan: {self.health:<30} │")
        print(f"│ Energi   : {self.energy:<30} │")
        print(f"│ Uang     : Rp {self.money:<27} │")
        print(f"│ Inventory: {len(self.inventory):<30} │")
        print(f"└─────────────────────────────────────────┘\n")
    
    def show_inventory(self):
        """Menampilkan inventory pemain"""
        print("\n📦 INVENTORY TITI:")
        if not self.inventory:
            print("   Inventory masih kosong")
        else:
            for i, item in enumerate(self.inventory, 1):
                print(f"   {i}. {item}")
        print()
    
    def add_inventory(self, item: str):
        """Menambahkan item ke inventory"""
        self.inventory.append(item)
        self.slow_print(f"✓ Titi mengambil: {item}")
    
    def has_item(self, item: str) -> bool:
        """Mengecek apakah pemain memiliki item"""
        return item in self.inventory
    
    def remove_item(self, item: str):
        """Menghapus item dari inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def use_energy(self, energy_loss: int):
        """Menggunakan energi"""
        self.energy = max(0, self.energy - energy_loss)
        if self.energy <= 0:
            self.slow_print("\n⚠️ Titi sudah kelelahan! Harus istirahat...")
            self.energy = 30
    
    def get_player_choice(self, choices: List[str]) -> int:
        """Mendapatkan pilihan dari pemain"""
        while True:
            for i, choice in enumerate(choices, 1):
                print(f"{i}. {choice}")
            try:
                choice = int(input("\nPilihan Titi: "))
                if 1 <= choice <= len(choices):
                    return choice
            except ValueError:
                pass
            print("❌ Pilihan tidak valid! Coba lagi.\n")
    
    # ==================== LOCATIONS ====================
    
    def location_desa_panjatan(self):
        """Lokasi pertama - Desa Panjatan"""
        self.clear_screen()
        self.slow_print("=" * 50)
        self.slow_print("🏘️  DESA PANJATAN - Awal Petualangan Titi 🏘️", delay=0.05)
        self.slow_print("=" * 50)
        
        story = """
Titi adalah seorang penjelajah muda yang pemberani. Dia baru tiba di Desa Panjatan,
sebuah desa kecil yang dikelilingi hutan lebat dan pegunungan misteri.

Konon kabarnya, harta karun legendaris tersembunyi di tempat ini. Harta karun itu
dikumpulkan oleh seorang bandit zaman dulu dan diyakini masih terpendam hingga sekarang.

Desa ini memiliki beberapa lokasi menarik:
- Rumah Tua di tepi hutan (katanya pemiliknya tahu tentang harta karun)
- Pasar Desa (tempat jual-beli)
- Makam Tua (tempat yang dianggap angker)
- Danau Panjatan (pemandangan indah tapi berbahaya)
        """
        self.slow_print(story)
        
        if self.visited_locations:
            self.display_stats()
            self.show_inventory()
        
        choices = [
            "Pergi ke Rumah Tua",
            "Kunjungi Pasar Desa",
            "Jelajahi Makam Tua",
            "Pergi ke Danau Panjatan",
            "Istirahat di penginapan"
        ]
        
        choice = self.get_player_choice(choices)
        
        if choice == 1:
            self.location_rumah_tua()
        elif choice == 2:
            self.location_pasar_desa()
        elif choice == 3:
            self.location_makam_tua()
        elif choice == 4:
            self.location_danau_panjatan()
        elif choice == 5:
            self.location_penginapan()
    
    def location_rumah_tua(self):
        """Lokasi: Rumah Tua"""
        self.clear_screen()
        self.current_location = "Rumah Tua"
        self.slow_print("=" * 50)
        self.slow_print("🏚️  RUMAH TUA - Misteri Memanggilmu 🏚️", delay=0.05)
        self.slow_print("=" * 50)
        
        story = """
Rumah tua ini terlihat sangat tua dan ditinggalkan. Pintunya setengah terbuka
dan terdengar angin berhembus lemah dari dalam.

Saat Titi mendekat, seorang nenek tua keluar dari rumah!
Wajahnya keriput namun matanya masih tajam.

NENEK: "Halo nak! Kamu mencari apa di tempat ini?"
        """
        self.slow_print(story)
        self.use_energy(15)
        
        if not "Bertemu Nenek Penjaga" in self.completed_quests:
            choices = [
                "Bertanya tentang harta karun",
                "Bertanya tentang desa ini",
                "Mencuri barang di dalam rumah",
                "Pergi dari sini"
            ]
            
            choice = self.get_player_choice(choices)
            
            if choice == 1:
                self.quest_harta_karun()
            elif choice == 2:
                self.talk_nenek_desa()
            elif choice == 3:
                self.steal_rumah_tua()
            elif choice == 4:
                self.location_desa_panjatan()
        else:
            print("\nNenek: 'Sudah ketemu jawabannya belum?'")
            choices = [
                "Tanya petunjuk lebih lanjut",
                "Pergi dari sini"
            ]
            choice = self.get_player_choice(choices)
            if choice == 1:
                self.quest_harta_karun()
            else:
                self.location_desa_panjatan()
    
    def quest_harta_karun(self):
        """Quest: Bertanya tentang harta karun"""
        self.clear_screen()
        story = """
TITI: "Nenek, apakah kamu tahu tentang harta karun yang terpendam di sini?"

NENEK: (tersenyum misterius)
"Harta karun? Ah, cerita lama dari masa kejayaan desa ini.
Benar, ada harta karun yang disembunyikan 40 tahun yang lalu.
Tapi lokasi pastinya hanya diketahui oleh 3 orang:
  1. Pembuat peta tersembunyi (sudah meninggal)
  2. Penjaga harta yang tersisa (mungkin masih hidup)
  3. Pemilik toko barang antik di pasar

Jika kamu ingin menemukannya, kumpulkan petunjuk dari:
- Makam Tua (tempat istirahat pembuat peta)
- Danau Panjatan (tempat perjanjian rahasia)
- Toko Barang Antik di pasar"

NENEK: "Tunggu... ambil ini. Kunci ini bisa membuka sesuatu yang penting."
        """
        self.slow_print(story)
        
        if not self.has_item("Kunci Berkarat"):
            self.add_inventory("Kunci Berkarat")
            self.add_inventory("Catatan Nenek: 'Cari 3 bagian peta'")
        
        self.completed_quests.add("Bertemu Nenek Penjaga")
        time.sleep(2)
        self.location_rumah_tua()
    
    def talk_nenek_desa(self):
        """Berbicara dengan Nenek tentang desa"""
        story = """
TITI: "Nenek, bisa ceritakan tentang sejarah desa ini?"

NENEK: "Desa Panjatan dulu sangat ramai. Ada pedagang, petualang, dan penjelajah.
Tapi suatu hari, seorang bandit terkenal menyembunyikan hartanya di sini.
Sejak saat itu, desa jadi sepi. Orang takut ada kejadian buruk."

TITI: "Apakah ada orang yang sempat menemukan harta karun itu?"

NENEK: "Tidak ada. Peta aslinya dipecah menjadi 3 bagian dan disembunyikan.
Setiap bagian dijaga oleh seseorang. Jika kamu bisa mengumpulkan semuanya,
mungkin kamu bisa menemukan hartanya."
        """
        self.slow_print(story)
        time.sleep(2)
        self.location_rumah_tua()
    
    def steal_rumah_tua(self):
        """Mencoba mencuri di rumah tua"""
        self.clear_screen()
        story = """
Titi mencoba masuk ke rumah tua sambil nenek tidak memperhatikan.

Di dalam rumah, Titi menemukan:
- Sejadi barang antik yang berharga
- Beberapa gambar tua di dinding

Saat Titi hendak mengambil barang, nenek tiba-tiba muncul!

NENEK: "HENTIKAN! Apa yang kamu lakukan?!"

Titi tertangkap basah mencuri. Nenek marah dan mengusirnya keluar!

❌ Kesempatan untuk mendapat petunjuk dari nenek hilang.
        """
        self.slow_print(story)
        self.completed_quests.add("Usir dari Rumah Tua")
        time.sleep(3)
        self.location_desa_panjatan()
    
    def location_pasar_desa(self):
        """Lokasi: Pasar Desa"""
        self.clear_screen()
        self.current_location = "Pasar Desa"
        self.slow_print("=" * 50)
        self.slow_print("🏪 PASAR DESA - Pusat Kehidupan Desa 🏪", delay=0.05)
        self.slow_print("=" * 50)
        
        story = """
Pasar desa ramai dengan pedagang dan pembeli. Aroma makanan tradisional
menyeruak di udara. Titi melihat beberapa toko:

1. Toko Barang Antik - Pemilik tua yang misterius
2. Warung Makan - Tempat mendengarkan cerita lokal
3. Toko Perlengkapan - Untuk membeli peralatan petualangan
4. Rumah Dukun - Tempat mistis
        """
        self.slow_print(story)
        self.use_energy(10)
        
        choices = [
            "Masuk ke Toko Barang Antik",
            "Mampir ke Warung Makan",
            "Belanja di Toko Perlengkapan",
            "Kunjungi Rumah Dukun",
            "Kembali ke Desa Panjatan"
        ]
        
        choice = self.get_player_choice(choices)
        
        if choice == 1:
            self.location_toko_antik()
        elif choice == 2:
            self.location_warung_makan()
        elif choice == 3:
            self.location_toko_perlengkapan()
        elif choice == 4:
            self.location_rumah_dukun()
        elif choice == 5:
            self.location_desa_panjatan()
    
    def location_toko_antik(self):
        """Lokasi: Toko Barang Antik"""
        self.clear_screen()
        story = """
Toko ini penuh dengan barang-barang antik berdebu. Di balik meja,
seorang pemilik toko tua sedang membaca buku.

PEMILIK TOKO: "Selamat datang. Ada yang bisa saya bantu?"

TITI: "Apakah kamu tahu tentang harta karun yang tersembunyi?"

PEMILIK TOKO: (tersenyum)
"Ah, peta! Iya, saya memiliki satu bagian peta asli.
Bagian ini menunjukkan lokasi Danau Panjatan.

Tapi... ini hanya akan kuberikan kepada yang bisa menjawab teka-teki.

TEKA-TEKI: 'Aku memiliki kota, tapi tidak ada rumah. Aku memiliki gunung,
tapi tidak ada pohon. Aku memiliki air, tapi tidak ada ikan. Apa aku?'
        """
        self.slow_print(story)
        self.use_energy(10)
        
        if not self.has_item("Bagian Peta 1"):
            print("\n(Pikirkan jawaban Titi...)")
            answers = [
                "Peta",
                "Dunia",
                "Langit",
                "Kapal"
            ]
            choice = self.get_player_choice(answers)
            
            if choice == 1:  # Peta adalah jawaban yang benar
                self.clear_screen()
                print("PEMILIK TOKO: 'BENAR! Kamu cerdas!'\n")
                self.add_inventory("Bagian Peta 1 (Danau Panjatan)")
                self.money += 50
                self.completed_quests.add("Jawab Teka-teki Toko Antik")
            else:
                self.clear_screen()
                print("PEMILIK TOKO: 'Salah. Coba lagi nanti.'\n")
                self.money -= 10
        
        choices = ["Kembali ke Pasar"]
        self.get_player_choice(choices)
        self.location_pasar_desa()
    
    def location_warung_makan(self):
        """Lokasi: Warung Makan"""
        self.clear_screen()
        story = """
Warung makan ini menghangatkan dengan aroma gulai dan nasi kuning.
Pemilik warung adalah ibu tua yang ramah.

IBU WARUNG: "Halo nak! Mau pesan apa? Nasi goreng spesial kami terkenal!"

TITI: "Biaya berapa? Aku sedang mencari harta karun..."

IBU WARUNG: "Ah, banyak yang cari tapi tidak pernah ada yang berhasil!
Tapi, saya tahu seseorang yang pernah mendapat bagian peta.
Dia adalah penjaga Makam Tua. Nama dia Pak Tirto."

IBU WARUNG: "Silakan makan dulu. Kuatkan diri mu. (Memberikan makanan gratis)

Energi Titi pulih! Titi merasa lebih segar.
        """
        self.slow_print(story)
        self.energy = min(100, self.energy + 30)
        self.add_inventory("Sepiring Nasi Kuning")
        self.use_energy(5)
        
        choices = ["Kembali ke Pasar"]
        self.get_player_choice(choices)
        self.location_pasar_desa()
    
    def location_toko_perlengkapan(self):
        """Lokasi: Toko Perlengkapan"""
        self.clear_screen()
        story = """
Toko perlengkapan ini menjual berbagai barang untuk petualangan:
- Kompas (Rp 50)
- Obat Penawar (Rp 60)
- Tali Tebal (Rp 40)
- Perlengkapan Menggali (Rp 80)
- Lampu Tangan (Rp 30)

PENJUAL: "Silakan lihat-lihat. Semua wajib untuk petualangan di hutan!"
        """
        self.slow_print(story)
        print(f"\nUangmu saat ini: Rp {self.money}\n")
        
        items = [
            ("Kompas", 50),
            ("Obat Penawar", 60),
            ("Tali Tebal", 40),
            ("Perlengkapan Menggali", 80),
            ("Lampu Tangan", 30),
            ("Tidak membeli apa-apa")
        ]
        
        for i, (item, price) in enumerate(items, 1):
            if i < len(items):
                print(f"{i}. {item} - Rp {price}")
            else:
                print(f"{i}. {item}")
        
        choice = int(input("\nPilihan: ")) - 1
        
        if 0 <= choice < len(items) - 1:
            item_name, price = items[choice]
            if self.money >= price:
                self.money -= price
                self.add_inventory(item_name)
            else:
                print("Uangmu tidak cukup!")
                time.sleep(2)
        
        self.location_pasar_desa()
    
    def location_rumah_dukun(self):
        """Lokasi: Rumah Dukun"""
        self.clear_screen()
        story = """
Rumah ini penuh dengan tanaman aneh dan aroma dupa.
Seorang dukun tua menyambut Titi dengan tatapan dalam.

DUKUN: "Aku melihat aura petualangan di dirimu. Kamu mencari sesuatu?"

TITI: "Aku mencari harta karun..."

DUKUN: "Harta karun akan membawa ketiga-belas cobaan untukmu.
Tapi, aku punya ramalan penting untuk dirimu.

📜 RAMALAN DUKUN:
'Ketiga bagian peta tersembunyi di tempat:
 1. Hati sang penjaga (Makam Tua)
 2. Pegangan tangan zaman dulu (Danau Panjatan)  
 3. Ingatan pemilik barang lama (Pasar)

Jika tiga terhimpun, pintu emas akan terbuka
Tapi hati-hati, musuh penjaga mungkin mengikutimu.'"

DUKUN memberi Titi sebotol ramuan untuk keberuntungan.
        """
        self.slow_print(story)
        self.add_inventory("Ramuan Keberuntungan Dukun")
        self.use_energy(5)
        
        choices = ["Kembali ke Pasar"]
        self.get_player_choice(choices)
        self.location_pasar_desa()
    
    def location_makam_tua(self):
        """Lokasi: Makam Tua"""
        self.clear_screen()
        self.current_location = "Makam Tua"
        self.slow_print("=" * 50)
        self.slow_print("⚰️  MAKAM TUA - Tempat Istirahat Pembuat Peta ⚰️", delay=0.05)
        self.slow_print("=" * 50)
        
        story = """
Makam tua ini terletak di tengah hutan yang sepi. Banyak makam tua
dengan tulisan yang sudah tidak terbaca.

Titi melihat seorang penjaga makam yang sedang membersihkan area.
Nama penjaga ini adalah Pak Tirto, seperti yang disebut ibu warung.

PAK TIRTO: "Siapa yang datang ke tempat ini? Aku jarang melihat pengunjung."

TITI: "Pak, saya mencari harta karun. Apakah kamu punya informasi?"

PAK TIRTO: (berhenti sejenak)
"Harta karun... ya, aku tahu ceritanya. Pembuat peta dimakamkan di sini.
Dia adalah sahabat saya dulu sebelum meninggal.

Dia meninggalkan sesuatu yang berharga untuk orang yang bisa memahami pesan tersembunyi.

Tapi sebelum itu, bisa tolong aku bersihkan makam? Aku sudah tua dan lelah."
        """
        self.slow_print(story)
        self.use_energy(20)
        
        if not "Bersihkan Makam" in self.completed_quests:
            choices = [
                "Membantu Pak Tirto membersihkan makam",
                "Menolak dan pergi",
            ]
            
            choice = self.get_player_choice(choices)
            
            if choice == 1:
                self.help_pak_tirto()
            else:
                self.location_desa_panjatan()
        else:
            print("\nPAK TIRTO: 'Terima kasih anak muda. Masih cari peta?'")
            choices = [
                "Tanya tentang peta",
                "Pergi dari sini"
            ]
            choice = self.get_player_choice(choices)
            if choice == 1:
                self.help_pak_tirto()
            else:
                self.location_desa_panjatan()
    
    def help_pak_tirto(self):
        """Membantu Pak Tirto"""
        self.clear_screen()
        story = """
Titi membantu Pak Tirto membersihkan makam dengan baik.
Pak Tirto terlihat sangat senang dan berterima kasih.

PAK TIRTO: "Terima kasih banyak anak muda. Kamu berbeda dari lelaki muda lainnya.
Kamu peduli pada orang tua.

Untuk itu, aku akan memberikan bagian peta yang dipercayakan kepadaku.
Ini adalah bagian ke dua, yang menunjukkan hutan rahasia!"

Pak Tirto memberikan:
✓ Bagian Peta 2 (Hutan Rahasia)
✓ Kunci Tua yang mungkin membuka sesuatu
✓ Perlengkapan Menggali berkualitas baik
        """
        self.slow_print(story)
        
        if not self.has_item("Bagian Peta 2"):
            self.add_inventory("Bagian Peta 2 (Hutan Rahasia)")
            self.add_inventory("Kunci Tua Pak Tirto")
            self.add_inventory("Perlengkapan Menggali Profesional")
            self.completed_quests.add("Bersihkan Makam")
            self.money += 100
        
        time.sleep(2)
        self.location_makam_tua()
    
    def location_danau_panjatan(self):
        """Lokasi: Danau Panjatan"""
        self.clear_screen()
        self.current_location = "Danau Panjatan"
        self.slow_print("=" * 50)
        self.slow_print("💧 DANAU PANJATAN - Keindahan dan Misteri 💧", delay=0.05)
        self.slow_print("=" * 50)
        
        story = """
Danau Panjatan terletak di tengan lembah yang sunyi. Air danau jernih
dan mencerminkan langit biru. Tapi ada yang aneh di sini...

Titi melihat tulisan-tulisan aneh di batu besar di tepi danau.
Seperti pesan rahasia dari zaman dulu.

Terdapat juga sebuah patung setengah terendam yang mungkin kunci sesuatu.

Tiba-tiba, seorang pemuda misterius muncul dari balik pohon!

PEMUDA MISTERIUS: "Hei! Apa yang kamu cari di tempat ini?"
        """
        self.slow_print(story)
        self.use_energy(15)
        
        if not "Bertemu Pemuda Misterius" in self.completed_quests:
            choices = [
                "Bertanya siapa dia",
                "Langsung mencari peta",
                "Mengajak jadi teman",
                "Pergi dari sini"
            ]
            
            choice = self.get_player_choice(choices)
            
            if choice == 1:
                self.talk_pemuda_misterius()
            elif choice == 2:
                self.search_peta_danau()
            elif choice == 3:
                self.befriend_pemuda()
            elif choice == 4:
                self.location_desa_panjatan()
        else:
            choices = [
                "Cari peta di danau",
                "Berbincang lagi",
                "Pergi dari sini"
            ]
            choice = self.get_player_choice(choices)
            if choice == 1:
                self.search_peta_danau()
            elif choice == 2:
                self.talk_pemuda_misterius()
            else:
                self.location_desa_panjatan()
    
    def talk_pemuda_misterius(self):
        """Berbicara dengan pemuda misterius"""
        story = """
TITI: "Siapa namamu? Apa yang kamu lakukan di sini?"

PEMUDA: "Nama saya Reno. Aku adalah keturunan penjaga harta karun itu.
Ayahku dulu menjaga harta, sebelum meninggal.

Sebenarnya... aku juga mencari peta itu. Tapi tidak untuk mengambil harta.
Aku ingin memastikan harta itu tidak disalahgunakan.

PETA TERAKHIR mungkin sudah hilang diambil orang lain.
Tapi, jika kamu butuh bantuan, aku siap membantu."

TITI: "Apakah kamu tahu di mana peta itu?"

RENO: "Patung di danau ini adalah kunci. Jika kamu bisa membukanya,
peta ketiga ada di dalamnya."
        """
        self.slow_print(story)
        self.completed_quests.add("Bertemu Pemuda Misterius")
        time.sleep(2)
        self.location_danau_panjatan()
    
    def befriend_pemuda(self):
        """Mengajak pemuda jadi teman"""
        story = """
TITI: "Hei, sepertinya kita punya tujuan yang sama. Mau jadi teman?"

RENO: (tersenyum)
"Aku suka orangmu. Okay, kita jadi tim sekarang!

Untuk membuka patung ini, kita butuh kunci khusus.
Aku punya sebagian, tapi separuhnya hilang.

Mungkin kunci itu satu set. Jika kamu punya kunci dari tempat lain,
bisa kita cocokan."
        """
        self.slow_print(story)
        self.add_inventory("Separuh Kunci Reno")
        self.completed_quests.add("Berteman dengan Reno")
        time.sleep(2)
        self.location_danau_panjatan()
    
    def search_peta_danau(self):
        """Mencari peta di danau"""
        self.clear_screen()
        
        if self.has_item("Perlengkapan Menggali Profesional"):
            story = """
Titi menggunakan perlengkapan menggali profesional dari Pak Tirto.

Dengan hati-hati, Titi menggali area di sekitar patung.
Setelah beberapa menit, sesuatu terasa keras!

KRRRRR... patung terbuka!

Di dalamnya tersimpan:
✓ Bagian Peta 3 (Gua Rahasia)
✓ Peta Lengkap yang menunjukkan lokasi harta karun
✓ Buku Harian Pembuat Peta

Akhirnya! Ketiga bagian peta sudah terkumpul!
            """
            self.slow_print(story)
            
            if not self.has_item("Bagian Peta 3"):
                self.add_inventory("Bagian Peta 3 (Gua Rahasia)")
                self.add_inventory("PETA LENGKAP - Harta Karun!")
                self.add_inventory("Buku Harian Pembuat Peta")
                self.money += 150
            
            print("\n🎉 PENCAPAIAN: Semua 3 bagian peta berhasil dikumpulkan!")
            time.sleep(3)
        else:
            story = """
Titi mencoba menggali dengan tangan, tapi sangat sulit.
Tanpa alat yang tepat, Titi tidak bisa membuka patung.

Titi perlu perlengkapan menggali yang lebih baik.
            """
            self.slow_print(story)
            time.sleep(2)
        
        self.location_danau_panjatan()
    
    def location_penginapan(self):
        """Lokasi: Penginapan"""
        self.clear_screen()
        story = """
Titi beristirahat di penginapan sederhana di desa.
        
Energi Titi pulih sepenuhnya setelah tidur.
Kesehatan juga meningkat kembali.
        """
        self.slow_print(story)
        self.energy = 100
        self.health = 100
        
        if self.has_item("PETA LENGKAP - Harta Karun!"):
            print("\nTiti bermimpi. Dalam mimpi, dia melihat lokasi harta karun...")
            time.sleep(2)
            print("Saatnya menemukan harta karun yang sesungguhnya!")
            time.sleep(2)
            self.show_final_location()
        else:
            print("\nSetelah istirahat, Titi siap melanjutkan petualangan.")
            time.sleep(2)
            self.location_desa_panjatan()
    
    def show_final_location(self):
        """Menampilkan lokasi akhir - Gua Rahasia"""
        self.clear_screen()
        self.current_location = "Gua Rahasia"
        self.slow_print("=" * 50)
        self.slow_print("⛏️  GUA RAHASIA - TUJUAN AKHIR ⛏️", delay=0.05)
        self.slow_print("=" * 50)
        
        story = """
Dengan peta lengkap, Titi dapat menemukan lokasi gua rahasia.
Gua ini tersembunyi di balik tebing yang curam.

Setelah perjalanan panjang, Titi akhirnya sampai di mulut gua.

Udara dingin menerpa. Di dalam gua, terlihat cahaya emas yang bersinar.

TITI: "Ini dia... harta karun legendaris yang dicari-cari selama puluhan tahun!"

Titi memasuki gua dengan perlahan...
        """
        self.slow_print(story)
        time.sleep(2)
        
        self.navigate_gua_rahasia()
    
    def navigate_gua_rahasia(self):
        """Navigasi di dalam gua rahasia"""
        self.clear_screen()
        
        story = """
Di dalam gua, Titi menemukan berbagai tantangan:

1. LORONG PERTAMA: Lantai yang tidak stabil
   Titi harus berjalan dengan hati-hati.

2. LORONG KEDUA: Ruangan gelap yang misterius
   Titi butuh cahaya untuk melihat.

3. LORONG KETIGA: Ruangan dengan banyak harta emas
   Tapi... ada yang aneh di sini...
        """
        self.slow_print(story)
        
        # Lorong pertama
        self.handle_lorong_pertama()
    
    def handle_lorong_pertama(self):
        """Menghandle lorong pertama"""
        self.clear_screen()
        story = """
LORONG PERTAMA: Lantai Tidak Stabil

Titi berjalan dengan hati-hati. Lantai batu mulai bergetar!

Pilihan Titi:
        """
        self.slow_print(story)
        
        choices = [
            "Berlari cepat ke ujung lorong",
            "Berjalan perlahan dan hati-hati",
            "Menggunakan tali untuk menyeberang"
        ]
        
        choice = self.get_player_choice(choices)
        
        if choice == 1:
            story = """
Titi berlari cepat, tapi lantai mulai runtuh!

BRRRRAAAAKKKKKK!!!

Titi terjatuh dan terluka.

❌ Titi mengalami cedera. Kesehatan turun!
            """
            self.slow_print(story)
            self.health -= 30
        elif choice == 2:
            story = """
Titi berjalan dengan perlahan dan terukur.
Lantai tetap stabil karena Titi tidak memberikan beban berat sekaligus.

BERHASIL! Titi berhasil menyeberang dengan aman.
            """
            self.slow_print(story)
        elif choice == 3:
            story = """
Titi menggunakan tali yang dibawanya untuk menyeberang.
Sangat aman dan cepat!

BERHASIL! Titi tiba di ujung lorong dengan selamat.
            """
            self.slow_print(story)
            self.health += 10
        
        time.sleep(2)
        self.handle_lorong_kedua()
    
    def handle_lorong_kedua(self):
        """Menghandle lorong kedua - ruangan gelap"""
        self.clear_screen()
        story = """
LORONG KEDUA: Ruangan Gelap

Titi memasuki ruangan yang sangat gelap.
Tidak bisa melihat apapun.

Tiba-tiba, terdengar suara berbisik aneh...

"KIM KAMI TIDAK AKAN MEMBERIKAN HARTA INI KEPADA SIAPAPUN..."

Pilihan Titi:
        """
        self.slow_print(story)
        
        choices = [
            "Menggunakan Lampu Tangan jika punya",
            "Menggunakan Ramuan Keberuntungan",
            "Menunggu sampai mata terbiasa gelap"
        ]
        
        # Filter pilihan berdasarkan inventory
        if not self.has_item("Lampu Tangan"):
            choices = ["Menggunakan Ramuan Keberuntungan", "Menunggu sampai mata terbiasa gelap"]
        
        choice = self.get_player_choice(choices)
        
        if "Lampu" in choices[0] if len(choices) > 0 else False and choice == 1:
            story = """
Titi menyalakan lampu tangan!

Cahaya menerangi ruangan. Titi bisa melihat jalan terang.
Bisikan gaib pun menghilang.

BERHASIL! Titi melewati ruangan gelap dengan cepat.
            """
            self.slow_print(story)
        elif "Ramuan" in str(choices) and choice == 1:
            story = """
Titi minum ramuan keberuntungan dari dukun.

Tiba-tiba, cahaya ajaib membimbing langkahnya!
Ramuan dukun bekerja sempurna!

BERHASIL! Titi melewati ruangan gelap dengan percaya diri.
            """
            self.slow_print(story)
            self.remove_item("Ramuan Keberuntungan Dukun")
        else:
            story = """
Titi berdiri diam, menunggu matanya terbiasa dengan kegelapan.

Setelah beberapa menit, mata Titi mulai membiasakan diri.
Samar-samar Titi bisa melihat jalan di depan.

Perlahan-lahan, Titi melangkah maju...

(Lebih lambat, tapi berhasil!)
            """
            self.slow_print(story)
            self.use_energy(20)
        
        time.sleep(2)
        self.handle_lorong_ketiga()
    
    def handle_lorong_ketiga(self):
        """Menghandle lorong ketiga - harta karun"""
        self.clear_screen()
        self.slow_print("=" * 50)
        self.slow_print("🏆 LORONG KETIGA: KAMAR HARTA KARUN 🏆", delay=0.05)
        self.slow_print("=" * 50)
        
        story = """
Titi keluar dari kegelapan dan masuk ke ruangan yang bercahaya emas!

WOOOOOWWWW!!!

Di depan mata Titi, ada tumpukan emas, permata, dan harta berharga lainnya!
Cahaya emas menerangi seluruh ruangan.

Tapi... ada PATUNG BESAR dengan wajah misterius di tengah harta karun.

Patung itu seperti penjaga harta karun.

Tiba-tiba, patung itu mulai bergerak!!!

PATUNG PENJAGA: "SIAPA YANG BERANI MENGAMBIL HARTA MILIKKU?!"

Titi merasa takut, tapi... suara itu terdengar familiar.
        """
        self.slow_print(story)
        self.use_energy(10)
        time.sleep(3)
        
        self.handle_final_challenge()
    
    def handle_final_challenge(self):
        """Tantangan akhir"""
        choices = [
            "Lari dari gua",
            "Berhadapan dengan penjaga",
            "Berbicara baik-baik dengan penjaga"
        ]
        
        choice = self.get_player_choice(choices)
        
        if choice == 1:
            self.clear_screen()
            story = """
Titi berlari keluar dari gua secepat mungkin!

BOOOM! Patung penjaga ambruk di belakangnya.
Gua mulai runtuh!

Titi berhasil keluar..., tapi TANGAN KOSONG!

ENDING BURUK: Titi tidak mendapatkan harta karun.
Harta karun tetap terkunci di bawah tanah.

Titi kembali ke desa sebagai penjelajah yang gagal.
            """
            self.slow_print(story)
            self.ending_type = "ENDING BURUK - Kabur"
            self.game_over = True
        
        elif choice == 2:
            self.clear_screen()
            story = """
TITI: "Aku tidak takut! Aku juga punya hak atas harta ini!"

Titi melawan patung dengan perlengkapan.

CRASH!!! BANG!!! POOOFFF!!!

Patung runtuh menjadi debu...

Tapi... biaya kerusakan akan sangat besar! Energi Titi habis!
            """
            self.slow_print(story)
            self.use_energy(40)
            
            if self.energy <= 0:
                self.clear_screen()
                self.slow_print("Titi tersungkur... semuanya menjadi gelap...")
                self.ending_type = "ENDING BURUK - Kelelahan"
                self.game_over = True
            else:
                self.handle_harta_karun()
        
        else:
            self.clear_screen()
            story = """
TITI: (Dengan tenang) "Halo... siapa sebenarnya kamu?"

Patung itu berhenti bergerak. Cahaya emas berubah warna.

SUARA GAIB: "Aku adalah roh penjaga harta ini selama 40 tahun.
Menunggu seseorang yang cukup bijak untuk menemukannya.

Tapi, harta ini memiliki tanggung jawab besar.
Apakah kamu siap menanggungnya?"

TITI: "Apa tanggung jawab itu?"

SUARA GAIB: "Harta ini harus digunakan untuk kebaikan desa.
Tidak boleh untuk kepentingan pribadi.
Jika setuju, harta ini milikmu."
            """
            self.slow_print(story)
            time.sleep(2)
            
            # Pilihan moral akhir
            final_choices = [
                "Setuju gunakan untuk kebaikan desa",
                "Ingin harta untuk diri sendiri"
            ]
            
            final_choice = self.get_player_choice(final_choices)
            
            if final_choice == 1:
                self.handle_ending_baik()
            else:
                self.handle_ending_tengah()
    
    def handle_harta_karun(self):
        """Menangani pengambilan harta karun setelah melawan"""
        story = """
Meskipun lelah, Titi berhasil mengumpulkan sebagian harta karun.

Titi membawa:
- Sepuluh tas emas
- Beberapa permata berharga
- Perhiasan antik

Total: Rp 10,000,000 (hanya sebagian kecil dari total)

ENDING NETRAL: Titi menjadi kaya, tapi tidak kaya raya.
Harta karun sebagian besar masih tersembunyi.
        """
        self.slow_print(story)
        self.money += 10000000
        self.ending_type = "ENDING NETRAL - Setengah Harta"
        self.game_over = True
    
    def handle_ending_baik(self):
        """ENDING BAIK - Menggunakan untuk kebaikan"""
        self.clear_screen()
        self.slow_print("=" * 50)
        self.slow_print("✨ ENDING TERBAIK - PAHLAWAN DESA ✨", delay=0.05)
        self.slow_print("=" * 50)
        
        story = """
Roh penjaga tersenyum (walau tidak terlihat).

SUARA GAIB: "Kamu adalah orang yang tepat. Semua harta ini milikmu!"

Cahaya emas memenuhi seluruh gua.

Titi dapat mengumpulkan sepenuhnya:
✓ 500 tas berisi emas murni
✓ 1000 permata langka  
✓ Perhiasan bersejarah
✓ Naskah kuno bernilai tinggi

Total: Rp 500,000,000 !!!

---

MASA DEPAN DESA:

Titi menggunakan harta untuk membangun:
- Sekolah baru di desa
- Rumah sakit untuk warga
- Jalan yang lebih baik
- Sistem irigasi untuk pertanian
- Perpustakaan komunitas

Desa Panjatan menjadi desa yang berkembang pesat!

Pak Tirto, Nenek di Rumah Tua, dan semua penduduk desa sangat berterima kasih.
Reno menjadi teman baik Titi dan mereka memulai sekolah petualangan.

TITI MENJADI PAHLAWAN DESA!

Cerita tentang Titi dan Harta Karun Panjatan tersebar ke seluruh daerah.
Banyak orang yang datang untuk belajar tentang keberanian dan kebijaksanaan Titi.

🎉 SELAMAT! TITI BERHASIL DENGAN SEMPURNA! 🎉
        """
        self.slow_print(story)
        self.money = 500000000
        self.ending_type = "ENDING TERBAIK ⭐"
        self.game_over = True
    
    def handle_ending_tengah(self):
        """ENDING NETRAL - Mengejar uang"""
        self.clear_screen()
        self.slow_print("=" * 50)
        self.slow_print("💰 ENDING BIASA - PENJELAJAH KAYA 💰", delay=0.05)
        self.slow_print("=" * 50)
        
        story = """
Roh penjaga menghilang dalam kekecewaan.

Tapi harta karun tetap terbuka untuk Titi!

Titi dapat mengumpulkan:
✓ 100 tas berisi emas murni
✓ 200 permata berharga
✓ Beberapa perhiasan

Total: Rp 100,000,000

---

Titi menjadi kaya raya, tapi...

Desa Panjatan tidak berkembang banyak.
Titi pindah ke kota besar untuk hidup mewah.

Sesekali Titi mengingat desa dan orang-orang baik di sana,
tapi sudah jarang berkunjung.

📊 HASIL AKHIR:
- Titi kaya
- Tapi kesepian
- Hubungan dengan desa menjadi dingin
- Ketenangan sejati tidak ditemukan

END (Biasa saja...)
        """
        self.slow_print(story)
        self.money = 100000000
        self.ending_type = "ENDING NETRAL 😐"
        self.game_over = True
    
    def show_end_screen(self):
        """Tampilkan layar akhir"""
        self.clear_screen()
        self.slow_print("=" * 50)
        self.slow_print("🎮 PETUALANGAN TITI BERAKHIR 🎮", delay=0.05)
        self.slow_print("=" * 50)
        
        self.display_stats()
        
        print("\n📊 STATISTIK AKHIR PERMAINAN:")
        print(f"Total Uang: Rp {self.money:,}")
        print(f"Item Dikumpulkan: {len(self.inventory)}")
        print(f"Quests Selesai: {len(self.completed_quests)}")
        print(f"Ending: {self.ending_type}")
        
        if self.ending_type == "ENDING TERBAIK ⭐":
            print("\n🏆 TITI ADALAH PAHLAWAN SEJATI! 🏆")
        elif "TERBAIK" in self.ending_type:
            print("\n⭐ PERJALANAN LEGENDARIS! ⭐")
        elif "NETRAL" in self.ending_type:
            print("\n😐 PERJALANAN YANG BIASA SAJA 😐")
        else:
            print("\n😞 PERJALANAN YANG MENYESAL 😞")
        
        print("\n" + "=" * 50)
        print("Terima kasih telah bermain The Mystery Adventure Bot!")
        print("=" * 50 + "\n")
    
    def run(self):
        """Menjalankan game"""
        self.clear_screen()
        self.slow_print("=" * 50)
        self.slow_print("🎮 SELAMAT DATANG DI 🎮", delay=0.05)
        self.slow_print("THE MYSTERY ADVENTURE BOT", delay=0.05)
        self.slow_print("=" * 50)
        
        intro = """
PETUALANGAN INTERAKTIF PENCARIAN HARTA KARUN

📍 LOKASI: Desa Panjatan yang Penuh Misteri
👸 KARAKTER: Titi - Penjelajah Muda yang Berani

Selamat datang di dunia petualangan yang penuh tantangan!
Apakah Titi akan menemukan harta karun legendaris?
Apa yang akan Titi lakukan dengan harta itu?

Keputusan Titi akan menentukan masa depan desa Panjatan.

Mari kita mulai petualangan...
        """
        self.slow_print(intro, delay=0.02)
        
        input("\n[Tekan ENTER untuk memulai petualangan Titi...]")
        
        # Game loop
        while not self.game_over:
            self.location_desa_panjatan()
        
        # Menampilkan layar akhir
        time.sleep(2)
        self.show_end_screen()

# ============== MAIN ==============

if __name__ == "__main__":
    game = MysteryAdventureBot()
    game.run()
 