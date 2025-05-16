# Docker
Docker adalah platform perangkat lunak yang memungkinkan pengembang untuk membangun, menguji, dan menyebarkan aplikasi secara cepat.
Instalasi Docker
1. Membuat direktori/file docker untuk menginstall docker lalu masuk ke folder docker
    ```
    vboxuser@VM-RyuMininet:~$ mkdir docker && cd docker
    ```
2. Membuat file untuk mengonfigurasi sistem agar dapat menginstal Docker di Ubuntu.
    - Membuat file `install_docker.sh`
        
        ``` 
        sudo nano install_docker.sh

        ```
    - Lalu isi dengan, codingan di bawah
        
        ``` markdown=
        # Add Docker's official GPG key:
        sudo apt-get update
        sudo apt-get install ca-certificates curl
        sudo install -m 0755 -d /etc/apt/keyrings
        sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/>
        sudo chmod a+r /etc/apt/keyrings/docker.asc

        # Add the repository to Apt sources:
        echo \
          "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] >
          $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
          sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update

        ```
    - selanjutnya, 
        ```
        chmod +x install_docker.sh
        ```
        fungsinya untuk memberikan izin eksekusi.
       
        
    - Setelah itu,
        ```
        ./install_docker.sh
        ```
        Fungsinya  untuk menjalankan skrip shell bernama install_docker.sh yang ada di direktori saat ini (./).

3. Instalasi docker
   
    ```
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```
    Output:

   ![image](https://hackmd.io/_uploads/rk9nyBUpkl.png)

5. Mem-verifikasi bahwa docker sudah terinstall atau belum
    ```
    sudo docker run hello-world
    ```
    Output:
   
    ![image](https://hackmd.io/_uploads/HJq-WHITyg.png)
