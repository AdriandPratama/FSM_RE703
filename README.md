# Kelompok 10 :
## 1. Laura Putri Rahayu. N 4222201013
## 2. Adriand Pratama 4222201036

   
# FSM Robot Obstacle Avoidance (ROS + Gazebo)

## Deskripsi
Proyek ini merupakan simulasi robot mobile menggunakan **Finite State Machine (FSM)** pada lingkungan **ROS Noetic** dan **Gazebo**.  
Robot bergerak secara otonom dan mampu menghindari rintangan dengan memanfaatkan data dari sensor **LaserScan**.

Pendekatan FSM digunakan untuk membuat logika kontrol robot lebih terstruktur, jelas, dan mudah dikembangkan.

---

## Tujuan
- Menerapkan konsep Finite State Machine pada robot mobile
- Menggunakan data LaserScan untuk obstacle avoidance
- Mensimulasikan pergerakan robot secara otonom
- Menyusun alur kontrol robot yang mudah dipahami

---

## Lingkungan Pengembangan
- Sistem Operasi: Ubuntu 20.04
- ROS: ROS Noetic
- Simulator: Gazebo
- Robot: TurtleBot3
- Bahasa Pemrograman: Python (rospy)

---

## Konsep Finite State Machine (FSM)

FSM terdiri dari beberapa state utama:

- **FORWARD**  
  Robot bergerak lurus ke depan.

- **DECIDE**  
  Robot menentukan arah belok berdasarkan ruang kosong terbesar.

- **TURN_LEFT**  
  Robot berputar ke kiri.

- **TURN_RIGHT**  
  Robot berputar ke kanan.

Perpindahan antar state ditentukan oleh jarak rintangan yang dibaca sensor LaserScan.

---

## Alur Sistem (Blok Diagram)

Alur kerja sistem secara sederhana:

LaserScan → FSM → /cmd_vel → Robot  
Robot bergerak → LaserScan membaca ulang → FSM memproses ulang

Proses ini berjalan secara berulang selama node ROS aktif.

---

## Penjelasan Topik /cmd_vel

Topik `/cmd_vel` digunakan untuk mengirim perintah kecepatan ke robot.

Isi pesan `/cmd_vel`:
- `linear.x`  : kecepatan maju atau mundur
- `angular.z`: kecepatan rotasi (belok kiri atau kanan)

FSM menentukan nilai kecepatan ini berdasarkan state robot saat ini.

---

## Cara Menjalankan Program

### 1. Menjalankan ROS Master
```
roscore
```

### 2. Menjalankan Simulasi TurtleBot3
```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

### 3. Menjalankan Program FSM
Pastikan file Python sudah executable:
```
chmod +x fsm_robot.py
```

Jalankan program:
```
rosrun <nama_package> fsm_robot.py
```

---

## Hasil yang Diharapkan
- Robot bergerak maju secara otomatis
- Robot mendeteksi rintangan menggunakan LaserScan
- Robot memilih arah belok kiri atau kanan
- Robot tidak menabrak dinding
- Pergerakan robot stabil dan konsisten

---

## Catatan
Program ini dibuat dengan logika sederhana namun terstruktur agar mudah dipahami dan dapat dikembangkan lebih lanjut sesuai kebutuhan.
