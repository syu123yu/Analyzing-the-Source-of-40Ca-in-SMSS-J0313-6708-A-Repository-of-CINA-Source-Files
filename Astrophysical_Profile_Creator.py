# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 21:00:48 2025

@author: syu12
"""

template_file = input("Input the template file name: ")
num_profiles = int(input("Number of profiles to generate: "))
density_i = float(input("Smallest Density to Start:"))
density_f = float(input("Largest Density to End:"))
delta_d = (density_f-density_i)/(num_profiles)
temp_i = float(input("Smallest Temperature to Start:"))
temp_f = float(input("Largest Temperature to End:"))
delta_t = (temp_f-temp_i)/(num_profiles)

with open(template_file, "r") as f:
    template = f.read()

for i in range(1,(num_profiles)+1):
    density = float(density_i + (i*delta_d))
    temperature = float(temp_i + (i*delta_t))

    profile = template
    profile = profile.replace("1.19000000E-01", f"{density:.8E}")
    profile = profile.replace("3.98000000E+01", f"{temperature:.8E}")

    output_name = f"{i+1}.txt"
    with open(output_name, "w") as f:
        f.write(profile)