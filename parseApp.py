from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QGridLayout, QScrollArea, QGroupBox
)
from PyQt6.QtCore import Qt

import sys
import fungsiCFG as cfg
 
class ListLexicon(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamus")
        self.resize(400, 600)
        
        self.scroll = QScrollArea()
        groupBox = QGroupBox()
        kamusLayout = QGridLayout()
        groupBox.setLayout(kamusLayout)
        
        # membuat scroll area untuk layout-nya
        self.scroll.setWidget(groupBox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        outerLayout = QVBoxLayout()
        outerLayout.addWidget(self.scroll)
        self.setLayout(outerLayout)
        
        # membuat komponen label tiap jenis lexicon
        pronLabel = QLabel("Kata Ganti:")
        nounLabel = QLabel("Kata Benda:")
        propLabel = QLabel("Kata Benda Khusus:")
        verbLabel = QLabel("Kata Kerja:")
        adjLabel = QLabel("Kata Sifat:")
        advLabel = QLabel("Kata Keterangan:")
        prepLabel = QLabel("Preposisi:")
        numLabel = QLabel("Numeralia:")
        
        # menaruh semua lexicon ke dalam variabel
        pron = "saya | aku | hamba | kami | kita | kamu | anda | engkau | kalian | dia | ia | beliau | mereka | ini | itu"
        noun = "pesta | kemarin | ujian | bola | dinding | peraturan | kuliah | penyakit | bantuan | kepanitiaan | sedih | vaksin | pramuka | pancasila | buku | lemari | audisi | puncak | rumah | mangga | lawan | ikan | ketenarannya | setahun | pertandingan | prestasinya | orang | sungai | hari | nanti | neneknya | minggu | akhir | cupang | usia | tahun | warna | pidato | bapak | seminar | bocah | pintu | usianya | guci | ketua | periode | barang | lapangan | temanku | pohon | tembok | jeda | daki | celana | kursi | tv | ular | rongga | mulut | sakura | kemenangan | petir | hukuman | malam | Ayah | kucingnya | keputusan | sifat | keberhasilan | hal | kisah | perjuangan | Ibu | suara | masakan | parfum | bunga | nanas | motor | lukisan | pisau | lantai | kulit | obat | teh | tulisan | baju | layar | ingin | antara | bulan"
        prop = "budi | steven | matthew | wahyu | roni | dito | jakarta | andi | indra | upin | saputra | susi | adi | banu | intan | dara | syifa | kadek | indah | abi | putri | wati | amanda | dian | arya | diah | citra | bali"
        verb = "lalu | menang | melihat | berhasil | pulang | berjalan | tinggal | berlangsung | dimulai | belajar | membuka | mengetuk | berdebat | berpamitan | pergi | menginjak | adalah | membeli | mengoleksi | dibangun | memberi | melekat | menempel | berada | duduk | dilewati | sayang | melawan | melakukan | berteriak | merasa"
        adj = "puas | bersih | lama | pudar | kotor | rajin | sakit | dewasa | merah | larut | lambat | singkat | perlahan | mendadak | baru | kuno | antik | primitif | lawas | lelet | dekat | jauh | akrab | lebat | rapat | besar | sempit | luas | bangga | bosan | takut | ngeri | kesal | sedih | segan | ragu | kagum | benci | berani | lembut | gembira | serius | iba | jahat | merdu | lezat | harum | semerbak | manis | asam | tampan | serak | bising | nyaring | indah | tajam | kasar | licin | halus | tebal | pahit | dingin | rapi | basah | lebar | hebat | suka"
        adv = "sudah | sangat | telah | belum | akan | sedang | ingin | mau | harus | mesti | agak | sangat | cukup | terlalu"
        prep = "sejak | dalam | dengan | di | jika | pada | dari | saat | untuk | atas | kepada | terhadap"
        num = "semua | suatu | setiap | banyak | satu | dua | tiga | empat | lima | enam | tujuh | delapan | sembilan"
        
        # membuat text area untuk tiap jenis lexicon dan menaruh variabel yang sesuai
        pronText = QTextEdit()
        pronText.setText(pron.replace(' ', '').replace('|', '\n')) # mengubah | menjadi newline
        nounText = QTextEdit()
        nounText.setText(noun.replace(' ', '').replace('|', '\n'))
        propText = QTextEdit()
        propText.setText(prop.replace(' ', '').replace('|', '\n'))
        verbText = QTextEdit()
        verbText.setText(verb.replace(' ', '').replace('|', '\n'))
        adjText = QTextEdit()
        adjText.setText(adj.replace(' ', '').replace('|', '\n'))
        advText = QTextEdit()
        advText.setText(adv.replace(' ', '').replace('|', '\n'))
        prepText = QTextEdit()
        prepText.setText(prep.replace(' ', '').replace('|', '\n'))
        numText = QTextEdit()
        numText.setText(num.replace(' ', '').replace('|', '\n'))
        
        # menambah komponen ke grid layout
        kamusLayout.addWidget(pronLabel, 0, 0)
        kamusLayout.addWidget(pronText, 1, 0, 1, 5)
        kamusLayout.addWidget(nounLabel, 2, 0)
        kamusLayout.addWidget(nounText, 3, 0, 1, 5)
        kamusLayout.addWidget(propLabel, 4, 0)
        kamusLayout.addWidget(propText, 5, 0, 1, 5)
        kamusLayout.addWidget(verbLabel, 6, 0)
        kamusLayout.addWidget(verbText, 7, 0, 1, 5)
        kamusLayout.addWidget(adjLabel, 8, 0)
        kamusLayout.addWidget(adjText, 9, 0, 1, 5)
        kamusLayout.addWidget(advLabel, 10, 0)
        kamusLayout.addWidget(advText, 11, 0, 1, 5)
        kamusLayout.addWidget(prepLabel, 12, 0)
        kamusLayout.addWidget(prepText, 13, 0, 1, 5)
        kamusLayout.addWidget(numLabel, 14, 0)
        kamusLayout.addWidget(numText, 15, 0, 1, 5)


class CFG(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Parsing Bahasa Baku Bahasa Indonesia")
        self.resize(300,200)
        self.window1 = ListLexicon()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # membuat komponen untuk GUI lalu dimasukkan ke layout
        self.inputLabel = QLabel("Masukkan kalimat disini:")
        self.checkButton = QPushButton("Check")
        self.checkButton.clicked.connect(self.klik)
        self.kalimatEntry = QLineEdit()
        self.statusLabel = QLabel("Status:")
        layout.addWidget(self.inputLabel)
        layout.addWidget(self.kalimatEntry)
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.checkButton)

        # membuat button untuk membuka window kamus
        kamusButton = QPushButton("Lihat Kamus")
        kamusButton.clicked.connect(self.toggle_window1)
        layout.addWidget(kamusButton)


    def klik(self):
        # ambil kalimat dalam entry
        kalimat = self.kalimatEntry.text()
        
        # cek jika hitungCYK me-return True maka kalimat diterima, berlaku sebaliknya jika False
        if len(kalimat) == 0:
            self.statusLabel.setText("Masukkan kalimat terlebih dahulu.")
        elif cfg.hitungCYK(kalimat.lower().split(' '), 'K'):
            self.statusLabel.setText("Status: Baku")
        else:
            self.statusLabel.setText("Status: Tidak Baku")
            
 
    def toggle_window1(self):
        # membuka window kamus
        if not self.window1.isVisible():
            self.window1.show()

# start program    
app = QApplication(sys.argv)
window = CFG()
window.show()
sys.exit(app.exec())