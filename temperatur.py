#membuat definisi untuk fungsi konversi suhu
#menerima 2 paramater "temperatur, value"
def konversisuhu(temperature, value):
    if value == 'C':
        temperatursuhu = (temperature - 32) * 5/9
        return temperatursuhu, 'C'
    else:
        temperatursuhu = (temperature * 9/5) + 32
        return temperatursuhu, 'F'

#memberikan nilai temperatur C serta fungsi konversi suhu  
celsius_temperature = 30
temperatursuhu, target_value = konversisuhu(celsius_temperature, 'F')
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah{temperatursuhu}°{target_value}")

#memberikan nilai temperatur F serta fungsi konversi suhu
fahrenheit_temperature = 30
temperatursuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
print(f"{fahrenheit_temperature}°F dikonversi ke fahrenheit adalah{temperatursuhu}°{target_value}")
