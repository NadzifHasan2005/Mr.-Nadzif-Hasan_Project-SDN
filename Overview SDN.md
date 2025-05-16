# Software Define Network
_Software Define Network_ adalah sebuah paradigma jaringan baru yang melakukan decouple atau pemisahan antara _control plane_ dengan _data plane_. _Software Define Network_ memdahkan jaringan untuk dikelola, bereksperimen dan mengembangkan protokol baru, serta beradaptasi pada perubahan infrakstuktur. 

## Komponen Utama Arsitektur SDN
1. Application Layer
  Pada _application layer_ akan menemukan sistem seperti deteksi intrusi, load balancing, dan firewall. Ini berbda dengan jaringan tradisional yang memerlukan alat tambahan untuk menambahkan fitur tersebut. Pada arsitektur SDN, bisa mengatur _data plane_ hanya dengan meggunakan _controller_.
2. Control Layer
   Lapisan ini merupakan bagian tengah yang berguna sebagai otak dari jaringan yang tersedia. Pada lapisan ini SDN _Controller_ akan mentranslasikan kebutuhan antara aplikasi dan infrakstuktur. 
3. Infrastuktur Layer
   Lapisan ini merupakan jaringan yang bergina untuk menangani aliran data paket. Lapisan infrastuktur terdiri dari elemen jaringan yang mengatur _SDN Datapath_ sesuai dengan instruksi dari _Control-Data-Plane-Interface_ atau CDPI  

## Fungsi Arsitektur Software Defined Network (SDN)
1. Menyederhanakan pegaturan dan pemeliharaan jaringan.
2. Memprediksi masalah pada jaringan.
3. mempercepat pembangunan atau penambahan jaringan.
4. Menekan biaya pengeluaran.
