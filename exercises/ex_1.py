#В классической погоне Том бежит за Джерри, поскольку Джерри съел любимую еду Тома.
#Джерри бежит со скоростью X метров в секунду, пока Том гонится за ним со скоростью
#Y метров в секунду. Начальное расстояние между ними S.Определите, сможет ли Том поймать Джерри. 
#Если да, то за сколько секунд. 


jerrySpeed = int(input("Jerry's speed"))
tomSpeed = int(input("Tom's speed"))
distance = int(input("Distance between them"))

def time():
    time = distance / (tomSpeed - jerrySpeed)
    time = str(time)
    print("Will chase for " + time + " seconds")

if jerrySpeed >= tomSpeed:
    print("Won't chase")
else:
    time()
