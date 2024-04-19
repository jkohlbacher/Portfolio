from pipedrive.client import Client
import time

# 1. Change domain name
# 2. Change API key

client = Client(domain='') # <-- change this

client.set_api_token('') # <-- change this

rate_limit = 18 # <-- change this

fdata1 = {'name': 'Referral Source', 
          'options':[{"label":"Realtor"},
                     {"label":"From past client"},
                     {"label":"Is an existing client"},
                     {"label":"Personal contact (friend, family, etc...)"},
                     {"label":"Friend or family referred them"},
                     {"label":"Financial Advisor"},
                     {"label":"Lawyer"},
                     {"label":"Insurance agent"},
                     {"label":"Advertising (incl. GTB)"},
                     {"label":"Open House"},
                     {"label":"BNI"},
                     {"label":"Bank rep"},
                     {"label":"Event (other than Home show, FTHB or Divorce seminars)"},
                     {"label":"Builder"},
                     {"label":"On-line (excl. any from TMA directly)"},
                     {"label":"Home show"},
                     {"label":"TMA (on-line or referral)"},
                     {"label":"Other mortgage agent"},
                     {"label":"Facebook groups/shout outs"},
                     {"label":"FTHB seminar"}], 'field_type': 'enum'}

fdata2 = {'name': 'Initial contact date', 'field_type': 'date'}

fdata3 = {'name': 'Referral name (link)', 'field_type': 'people'}

fdata4 = {'name': 'Co-Applicant (Person link)', 'field_type': 'people'}

fdata5 = {'name': 'Co-applicant', 'field_type': 'varchar'}

fdata6 = {'name': 'Co-applicant phone', 'field_type': 'varchar'}

fdata7 = {'name': "All Borrower's Names", 'field_type': 'varchar'}

fdata8 = {'name': 'Date of Birth', 'field_type': 'date'}

fdata9 = {'name': 'Birth month and day', 'field_type': 'date'}

fdata10 = {'name': 'Birthday drip', 'options':[{"label":"Start"},{"label":"Stop - Unsubscribed"}], 'field_type': 'enum'}

fdata11 = {'name': 'Referral name', 'field_type': 'varchar'}

fdata12 = {'name': 'Zap Triggered', 'options':[{"label":"Yes"},{"label":"No"}], 'field_type': 'enum'}

fdata13 = {'name': 'Google or FB review given? (per person)', 'options':[{"label":"Yes"},{"label":"Temporary No"}], 'field_type': 'enum'}

fdata14 = {'name': 'Co-applicant e-mail', 'field_type': 'varchar'}

fdata15 = {'name': "App Recv'd E-mail sent", 'options':[{"label":"Yes"},{"label":"No"}], 'field_type': 'enum'}



flist = [fdata1,fdata2,fdata3,fdata4,fdata5,fdata6,fdata7,fdata8,fdata9,fdata10,fdata11,fdata12,fdata13,fdata14,fdata15]

rate_limit_iterator = 0

print("Creating custom person fields")

for data in flist:
    client.persons.create_person_field(data)
    rate_limit_iterator += 1
    print(rate_limit_iterator) 
    if rate_limit_iterator == rate_limit:
        print("Rate limit hit, sleeping for 2 seconds")
        rate_limit_iterator = 0
        time.sleep(2)
        
print("Done")
