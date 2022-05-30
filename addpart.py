import os

for i in range(1,153+1):
    if i == 134:
        continue
    os.system(f"cmsAddParticipation -c 4 user{i}")
