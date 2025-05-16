# Kubectl
Kubectl adalah alat baris perintah (command line tool) yang digunakan untuk mengelola klaster Kubernetes. 

1. Mengunduh kubectl dengan versi terbaru
    
    ```
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    ```
    Output:
   
    ![image](https://hackmd.io/_uploads/SJyaWDU6ye.png)

3. Mendownload file checksum (SHA256) dari binary kubectl versi terbaru Kubernetes.
    ```
     curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
    ```
    Output:
   
    ![image](https://hackmd.io/_uploads/rJ3fQDLTkg.png)
4. Memvalidasi binary kubectl
    ```
    echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
    ```
    Output:
   
    ![image](https://hackmd.io/_uploads/B1Ld7wUT1g.png)
5. Install Kubectl
    ```
    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    ```
    Output:
   
    ![image](https://hackmd.io/_uploads/B17DvPUa1g.png)

   Solusi:
    - Ketik
        ```
        exit
        ```
        Untuk memastikan bahwa sudah keluar dari group.
    - Memberikan izin eksekusi (execute permission) pada file kubectl.
        ```
        chmod +x kubectl
        ```
    -  Memindahkan file kubectl dari direktori saat ini (./kubectl) ke direktori ~/.local/bin/    
        ```
        sudo mv ./kubectl ~/.local/bin/kubectl

        ```
    - Mengecek kubectl
        ```
        kubectl get po -A
        ```
        output:
      
        ![image](https://hackmd.io/_uploads/HyuFdvU6Jg.png)

