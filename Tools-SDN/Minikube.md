# Minikube
Minikube adalah alat yang menyiapkan lingkungan Kubernetes di PC atau laptop lokal.

Instalasi Minikube
1. Mengunduh file installer Minikube
    ```
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
    ```
    Output:
   
    ![image](https://hackmd.io/_uploads/HJ7Ynr8ayg.png)

3. Menginstal Minikube dari file .deb di sistem berbasis Debian/Ubuntu.
    ```
    sudo dpkg -i minikube_latest_amd64.deb
    ```
    output:
    ![image](https://hackmd.io/_uploads/rkGdprIa1x.png)
4. Menjalankan Minikube
    ```
   minikube start --driver=docker
    ```
    Output:
   
    Terdapat error
    ![image](https://hackmd.io/_uploads/SkckgL8ake.png)
    solusi:
    - menambahkan pengguna saat ini ($USER) ke dalam grup docker.
        ```
        sudo usermod -aG docker $USER
        ```
    - mengaktifkan keanggotaan grup docker tanpa perlu logout atau restart.
        ```
        newgrp docker
        ```
    - Jalankan minikube
        ```
       minikube start --driver=docker
        ```
    - Output:
        :::warning
        ![image](https://hackmd.io/_uploads/rJtS1vU6Jg.png)
    Saya garis bawahi berwarna orange, menendakan bahwa kubectl tidak ditemukan.
