import wmi

# carrega informaçoes #
c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

#mostra resultados#
print(f"marca: {my_system.Manufacturer}")
print(f"Modelo: {my_system.Model}")
print(f"Nome: {my_system.Name}")
print(f"Qtde. CPUs: {my_system.NumberOfProcessors}")
print(f"Arquitetura: {my_system.SystemType}")
print(f"Familia:{my_system.SystemFamily}")
