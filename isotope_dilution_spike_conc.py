standard = 10 #in ppb or ng

iso_a_blank = 476.8
iso_a_spike = 610.1
iso_a_standard = 94297.2
iso_a_stand_spike = 94408.4

iso_b_blank = 69.5
iso_b_spike = 57951.6
iso_b_standard = 13394.7
iso_b_stand_spike = 84522.0


As = iso_a_spike/(iso_a_spike+iso_b_spike) #Spike Ratio
Astand = iso_a_standard/(iso_a_standard+iso_b_standard)
A_ss = iso_a_stand_spike/(iso_b_stand_spike)

Bs = iso_b_spike/(iso_a_spike+iso_b_spike)
Bstand = iso_b_standard/(iso_a_standard+iso_b_standard)
threshold = 1e-2  # You can adjust this threshold based on your precision needs

x = standard

i = x
while i > 0:
    z = 10 - (((As - A_ss*Bs)/(A_ss*Bstand-Astand))*i)
    if z < 0:
        i -= 0.00001
        print(i)
    
    if abs(z) < threshold:
        print(f"Breaking the loop because z has reached 0.\n Your spike is {i} ng. \n Ratio of Isotope A to B is {As}")
        break

        
