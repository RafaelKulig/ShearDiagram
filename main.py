import matplotlib.pyplot as plt
def shear_diag(beam_length,load_distance,load_intensity,support_position_1,support_position_2):
    x=[0,support_position_1,load_distance,support_position_2,beam_length]
    shear_force=[0,0,0,0,0]
    reaction_2=(load_intensity*(load_distance-support_position_1))/(support_position_2-support_position_1)
    reaction_1=load_intensity-reaction_2

    shear_force[1]=reaction_1
    shear_force[2]=reaction_1
    shear_force[3]=reaction_1-load_intensity

    plt.step(x,shear_force,where='post',label='Shear Force')
    plt.xlabel('Distance along the beam')
    plt.ylabel('Shear Force')
    plt.title('Shear Force Diagram')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()



shear_diag(beam_length=10, load_distance=6, load_intensity=15, support_position_1=2, support_position_2=8)