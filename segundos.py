segundos_input = input("Por favor, entre com o número de segundos que deseja converter: ")
total_seg = int(segundos_input)

dias = total_seg // 86400
seg_restantes = total_seg % 86400
horas = seg_restantes // 3600
seg_restantes = seg_restantes % 3600
minutos = seg_restantes // 60
segundos = seg_restantes % 60

print( dias , " dias, " , horas , " horas, ", minutos , " minutos e " , segundos , " segundos.")

