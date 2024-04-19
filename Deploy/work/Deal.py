from pipedrive.client import Client
import csv
import time


# 1. Change domain name
# 2. Change API key
# OPTIONAL 3. Change rate limit if account has higher than base rate for faster


client = Client(domain='') # <-- change this

client.set_api_token('') # <-- change this

rate_limit = 18 # <-- change this

with open('names.csv', newline='') as f:
    reader = csv.reader(f)
    names = list(reader)

with open('types.csv', newline='') as f:
    reader = csv.reader(f)
    types = list(reader)


option_list = [[{"label":"Yes"},{"label":"No"}], #FTHB? 2
               [{"label":"Purchase"},{"label":"Switch/Transfer"},{"label":"Refinance"},{"label":"Personal loan"},{"label":"Second mortgage"},{"label":"Land Purchase"},{"label":"Construction"},{"label":"Purchase Plus Improvements"},{"label":"Spousal buyout"},{"label":"Renewal (TBD)"}], #Purpose 10
               [{"label":"Owner-occupied"},{"label":"Owner-occupied + rental"},{"label":"Rental"},{"label":"Second home/cottage"}], #Use 4
               [{"label":"First"},{"label":"Second"},{"label":"Third"}], #Rank 3
               [{"label":"Start"},{"label":"Stop"},{"label":"Finished"}], #Active App Drip? 3
               [{"label":"Yes"},{"label":"No"},{"label":"N/A"}], #Mort Plan Sent? 3
               [{"label":"Yes"},{"label":"No"}], #Compliance uploaded & tasked 2
               [{"label":"Yes"},{"label":"No"}], #Closing gift sent? 2
               [{"label":"Yes"},{"label":"No"},{"label":"Off"}], #Added to tracker? 3
               [{"label":"Yes"},{"label":"No"}], #Realtor intro sent? 2
               [{"label":"Yes"},{"label":"No"}], #Active purchase? 2
               [{"label":"Fixed"},{"label":"Adjustable"},{"label":"Variable"},{"label":"HELOC"},{"label":"Multi-component"},{"label":"Personal loan"},{"label":"TBD"}], #Product 7
               [{"label":"Yes"},{"label":"No"}], #Contacts made for renewal 2
               [{"label":"Yes"},{"label":"No"}], #renewal deal created 2
               [{"label":"Mid-term change"},{"label":"Sold or paid off"},{"label":"Transferred or Refinanced at maturity"}], #refinanced at maturity 3
               [{"label":"Yes"},{"label":"No"}], #is this a renewal deal 2
               [{"label":"Mid-term change"},{"label":"Sold or paid off"},{"label":"Transferred or Refinanced at maturity"}], #Mortgage Dissolved 3
               [{"label":"Pay themselves"},{"label":"Lender pays"},{"label":"Change to pay themselves - currently lender paid"},{"label":"Change to lender paid - currently pay themselves"}], #Property Tax Selection 4
               [{"label":"Monthly"},{"label":"Semi-monthly"},{"label":"Bi-weekly"},{"label":"Weekly"},{"label":"Accelerated bi-weekly"},{"label":"Accelerated weekly"}], #Payment Frequency Selection 6
               [{"label":"B1 - Life"},{"label":"B1 - Disability"},{"label":"B2 - Life"},{"label":"B2 - Disability"},{"label":"B1 - None"},{"label":"B2 - None"},{"label":"B1 - Not eligible"},{"label":"B2 - Not eligible"}], #MPP Selections 8
               [{"label":"Yes"},{"label":"No"}], #MPP Sent? 2
               [{"label":"Yes"},{"label":"No"}], #LOD Acknowledged? 2
               [{"label":"Yes"},{"label":"No"},{"label":"AVM"}], #Appraisal Required 3
               [{"label":"Client"},{"label":"Broker"},{"label":"Reimbursed to client after"},{"label":"Lender (QC)"},{"label":"N/A"}], #Appraisal paid by? 5
               [{"label":"New Doc Uploaded"},{"label":"All Docs Reviewed"}], #Finmo Docs uploaded 2
               [{"label":"Realtor"},{"label":"From a past client"},{"label":"Is an existing client"},{"label":"Personal contact (they are friend, family, etc...)"},{"label":"Friend or Family referred them"},{"label":"Financial Advisor"},{"label":"Lawyer"},{"label":"Insurance agent"},{"label":"Advertising (incl. GTB)"},{"label":"Open House"},{"label":"BNI"},{"label":"Bank Rep"},{"label":"Event (other than Home show, FTHB or Divorce seminars)"},{"label":"Builder"},{"label":"On-line (excl. any from TMA directly)"},{"label":"Home show"},{"label":"TMA  (on-line or referral)"},{"label":"Other mortgage agent"},{"label":"Facebook groups/shout outs"},{"label":"FTHB Seminar"}], #Referal Source 20
               [{"label":"Yes"},{"label":"No"}] #Zap Triggered 2
               ]


option_list_iterator = 0
rate_limit_iterator = 0

print("Creating custom deal fields")

for x in range(len(names)):
    if types[x][0] == "single option":
        data = {'name': names[x][0], 'options': option_list[option_list_iterator], 'field_type': 'enum'}
        client.deals.create_deal_field(data)
        option_list_iterator += 1
    else:
        data = {'name': names[x][0], 'field_type': types[x][0]}
        client.deals.create_deal_field(data)
    rate_limit_iterator += 1
    print(rate_limit_iterator)
    if rate_limit_iterator == rate_limit:
        print("Rate limit hit, sleeping for 2 seconds")
        rate_limit_iterator = 0
        time.sleep(2)

print("Done")