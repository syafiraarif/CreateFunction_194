#TUGAS 1
#membuat fungsi konversisuhu yang memiliki parameter temperature dan value
def konversisuhu(temperature, value):
    # Memeriksa apakah nilai 'value' adalah 'C' (Celsius)
    if value == 'C':
        # Mengonversi suhu dari Fahrenheit ke Celsius
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'  # Mengembalikan suhu yang dikonversi dan yang memiliki satuan 'C'
    else:
        # Mengonversi suhu dari Celsius ke Fahrenheit
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'F'  # Mengembalikan suhu yang dikonversi dan yang memiliki satuan 'F'

# Suhu Celsius yang akan dikonversi
celsius_temperature = 30
# Memanggil fungsi untuk mengonversi Celsius ke Fahrenheit
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')
# Mencetak hasil konversi dari Celsius ke Fahrenheit
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")

# Suhu Fahrenheit yang akan dikonversi
fahrenheit_temperature = 86
# Memanggil fungsi untuk mengonversi Fahrenheit ke Celsius
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
# Mencetak hasil konversi dari Fahrenheit ke Celsius
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}")


#TUGAS 2
# Mengimpor modul math untuk menggunakan konstanta pi
import math

# Fungsi lambda untuk menghitung luas lingkaran
# Rumus luas lingkaran adalah π * r * r
luas_lingkaran = lambda r: math.pi * r * r

# Contoh penggunaan:
jari_jari = 7  # memasukan jari-jari lingkaran
# area : memanggil fungsi lamda untuk Menghitung luas lingkaran dengan jari-jari yang telah dimasukan
area = luas_lingkaran(jari_jari)

# Mencetak hasil luas lingkaran 
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas_lingkaran(jari_jari):.2f}")
