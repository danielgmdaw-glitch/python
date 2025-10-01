# Programa que convierte bytes a GB, MB, KB y Bytes (SI y IEC)
bytes_input = int(input("Introduce número de bytes: "))

# Sistema decimal (SI)
GB_si = bytes_input // 10**9
MB_si = (bytes_input % 10**9) // 10**6
KB_si = (bytes_input % 10**6) // 10**3
B_si = bytes_input % 10**3

# Sistema binario (IEC)
GiB = bytes_input // 1024**3
MiB = (bytes_input % 1024**3) // 1024**2
KiB = (bytes_input % 1024**2) // 1024
B_iec = bytes_input % 1024

print(f"{bytes_input} bytes en sistema decimal (SI): {GB_si} GB, {MB_si} MB, {KB_si} KB, {B_si} bytes")
print(f"{bytes_input} bytes en sistema binario (IEC): {GiB} GiB, {MiB} MiB, {KiB} KiB, {B_iec} bytes")
