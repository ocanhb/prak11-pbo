# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:34:11 2024

@author: ocanh
"""

def nama_nim(func):
    def wrapper(*args, **kwargs):
        nama_lengkap = func(*args, **kwargs)
        nim = kwargs.get("nim", "NIM tidak tersedia")
        return f"{nama_lengkap} Nim {nim}"
    return wrapper

def nama_panggilan(func):
    def wrapper(*args, **kwargs):
        nama_lengkap = func(*args, **kwargs)
        title = "Mr" if kwargs.get("gender", "Laki-laki") == "Laki-laki" else "Mrs"
        return f"{title} {nama_lengkap}"
    return wrapper


@nama_nim
@nama_panggilan
def nama_lengkap(nama_depan, nama_belakang, **kwargs):
    return f"{nama_depan} {nama_belakang}"

# Fungsi untuk mendapatkan masukan dari pengguna
def input_data():
    nama_depan = input("Masukkan nama depan: ")
    nama_belakang = input("Masukkan nama belakang: ")
    gender = input("Masukkan jenis kelamin (Laki-laki/Perempuan): ").capitalize()
    nim = input("Masukkan NIM: ")
    return nama_depan, nama_belakang, gender, nim

# Contoh pemanggilan
while True:
    try:
        nama_depan, nama_belakang, gender, nim = input_data()
        nama = nama_lengkap(nama_depan, nama_belakang, gender=gender, nim=nim)
        print("Nama Lengkap:", nama)
        break
    except Exception as e:
        print("Terjadi kesalahan:", e)

