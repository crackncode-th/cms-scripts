import csv
import os

fname = input("Enter file name: ")

data = open(fname)

reader = csv.reader(data)

for row in reader:
    if "Username" in row[2]:
        continue
    # usage: cmsAddUser [-h] [-e EMAIL] [-t TIMEZONE] [-l LANGUAGES]
    # [-p PLAINTEXT_PASSWORD | -H HASHED_PASSWORD] [--bcrypt]
    # first_name last_name username
    os.system(
        f'cmsAddUser "{row[4]}" "" {row[2]} -e {row[1]} -p {row[3]} --bcrypt')
    # usage: cmsAddParticipation [-h] [-c CONTEST_ID] [-i IP] [-d DELAY_TIME]
    # [-e EXTRA_TIME] [-t TEAM] [--hidden] [--unrestricted]
    # [-p PLAINTEXT_PASSWORD | -H HASHED_PASSWORD] [--bcrypt]
    # username
    os.system(f'cmsAddParticipation -c 1 {row[2]}')
