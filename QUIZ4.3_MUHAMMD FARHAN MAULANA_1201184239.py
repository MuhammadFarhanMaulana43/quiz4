listgpa = [2.1,2.3,4,3]

def hadiah(gpa):
    bonus = 500000
    hadiah = gpa*bonus
    return hadiah

for gpa in listgpa:
    if gpa > 2.5 :
        print("hadiah anda : Rp", hadiah(gpa))
    else:
        print("maaf coba lagi")