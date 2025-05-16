# Ryu Controller
Ryu Controller adalah Pengendali jaringan berbasis perangkat lunak (SDN) terbuka yang dirancang untuk meningkatkan kelincahan jaringan dengan mempermudah pengelolaan dan penyesuaian penanganan lalu lintas.

Instalasi Ryu Cotroller
1. Update Apt
    ```
    sudo apt update
    ```
    Output:
   
    ![image](https://hackmd.io/_uploads/SkmEFQUpyl.png)
3. Intall pip3
    ```
    sudo apt install -y python3-pip
    ```
    Output:
   
    ![image](https://hackmd.io/_uploads/ByctK7L61l.png)
5. Instalasi git
    ```
    sudo apt install -y git
    ```
    Output:
   
    ![image](https://hackmd.io/_uploads/BJuCFXUpyl.png)
7. Clone ryu dari git
    ```
    git clone https://github.com/faucetsdn/ryu.git
    ```
    Output:

   ![image](https://hackmd.io/_uploads/HyWBc7861g.png)
9. Masuk ke direktori/folder ryu
    ```
    cd ryu
    ```
    Output:
   
    ![image](https://hackmd.io/_uploads/H1QjcQUakx.png)
11. Instalasi di direktori/folder ryu
    ```
    sudo python3 ./setup.py install
    ```
    Output:
    
    ![image](https://hackmd.io/_uploads/Skq84BITke.png)
13. Keluar Direktori
    ```
    cd ..
    ```
    Output:
    
    ![image](https://hackmd.io/_uploads/H1CyJN8a1l.png)
15. Install ryu
    ```
    sudo pip3 install --upgrade ryu
    ```
    Output:
    
    ![image](https://hackmd.io/_uploads/SyHMHrLp1x.png)

17. Mem-verifikasi
   ```
   ryu-manager
   ```
   Output:
   
   ![image](https://hackmd.io/_uploads/BJA8UHUaye.png)
