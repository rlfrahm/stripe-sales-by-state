import stripe, csv, datetime, os.path

import settings

stripe.api_key = settings.STRIPE_PK

start = datetime.datetime(settings.YEAR, 1, 1)
end = datetime.datetime(settings.YEAR, 12, 31)
charges = stripe.Charge.list(limit=100, refunded=False, paid=True, status='succeeded', created= { 'gte': start, 'lte': end })

zips = {}

def run():
  i = 0
  zips_filename = '%s_zips.csv' % (settings.YEAR)
  if not os.path.isfile(zips_filename):
    for charge in charges.auto_paging_iter():
      # for charge in charges:
      # Do something with customer
      i += 1
      print(i)
      if charge.billing_details.address.postal_code not in zips:
        zips[charge.billing_details.address.postal_code] = charge.amount
      else:
        zips[charge.billing_details.address.postal_code] += charge.amount

    with open(zips_filename, 'w', newline='') as csvfile:
      zipswriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      for zip, amount in zips.items():
        zipswriter.writerow([zip, amount])

  states = {}

  with open(zips_filename, newline='') as csvfile:
    zipsfile = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in zipsfile:
      print(row)
      amt = int(row[1])
      state, abbr = get_state(row[0])
      if state not in states:
        states[state] = {
          'amount': amt / 100,
          'zip': row[0],
          'abbr': abbr
        }
      else:
        states[state]['amount'] += amt / 100
  
  print('============')
  print('= %s.csv' % (settings.YEAR))
  print('============')
  print('State,Abbr,Zip,Amount')
  with open('%s.csv' % (settings.YEAR), 'w', newline='') as csvfile:
    stateswriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    stateswriter.writerow(['State', 'Abbr', 'Zip', 'Amount'])
    for state, value in states.items():
      v = [state, value['abbr'], value['zip'], value['amount']]
      print(','.join(str(l) for l in v))
      stateswriter.writerow(v)

def get_state(zipcode):
  zipcode = int(str(zipcode).split('-')[0])
  if zipcode >= 35000 and zipcode <= 36999:
    st = 'AL'
    state = 'Alabama'
  elif zipcode >= 99500 and zipcode <= 99999:
    st = 'AK'
    state = 'Alaska'
  elif zipcode >= 85000 and zipcode <= 86999:
    st = 'AZ'
    state = 'Arizona'
  elif zipcode >= 71600 and zipcode <= 72999:
    st = 'AR'
    state = 'Arkansas'
  elif zipcode >= 90000 and zipcode <= 96699:
    st = 'CA'
    state = 'California'
  elif zipcode >= 80000 and zipcode <= 81999:
    st = 'CO'
    state = 'Colorado'
  elif zipcode >= 6000 and zipcode <= 6999:
    st = 'CT'
    state = 'Connecticut'
  elif zipcode >= 19700 and zipcode <= 19999:
    st = 'DE'
    state = 'Delaware'
  elif zipcode >= 32000 and zipcode <= 34999:
    st = 'FL'
    state = 'Florida'
  elif zipcode >= 30000 and zipcode <= 31999:
    st = 'GA'
    state = 'Georgia'
  elif zipcode >= 96700 and zipcode <= 96999:
    st = 'HI'
    state = 'Hawaii'
  elif zipcode >= 83200 and zipcode <= 83999:
    st = 'ID'
    state = 'Idaho'
  elif zipcode >= 60000 and zipcode <= 62999:
    st = 'IL'
    state = 'Illinois'
  elif zipcode >= 46000 and zipcode <= 47999:
    st = 'IN'
    state = 'Indiana'
  elif zipcode >= 50000 and zipcode <= 52999:
    st = 'IA'
    state = 'Iowa'
  elif zipcode >= 66000 and zipcode <= 67999:
    st = 'KS'
    state = 'Kansas'
  elif zipcode >= 40000 and zipcode <= 42999:
    st = 'KY'
    state = 'Kentucky'
  elif zipcode >= 70000 and zipcode <= 71599:
    st = 'LA'
    state = 'Louisiana'
  elif zipcode >= 3900 and zipcode <= 4999:
    st = 'ME'
    state = 'Maine'
  elif zipcode >= 20600 and zipcode <= 21999:
    st = 'MD'
    state = 'Maryland'
  elif zipcode >= 1000 and zipcode <= 2799:
    st = 'MA'
    state = 'Massachusetts'
  elif zipcode >= 48000 and zipcode <= 49999:
    st = 'MI'
    state = 'Michigan'
  elif zipcode >= 55000 and zipcode <= 56999:
    st = 'MN'
    state = 'Minnesota'
  elif zipcode >= 38600 and zipcode <= 39999:
    st = 'MS'
    state = 'Mississippi'
  elif zipcode >= 63000 and zipcode <= 65999:
    st = 'MO'
    state = 'Missouri'
  elif zipcode >= 59000 and zipcode <= 59999:
    st = 'MT'
    state = 'Montana'
  elif zipcode >= 27000 and zipcode <= 28999:
    st = 'NC'
    state = 'North Carolina'
  elif zipcode >= 58000 and zipcode <= 58999:
    st = 'ND'
    state = 'North Dakota'
  elif zipcode >= 68000 and zipcode <= 69999:
    st = 'NE'
    state = 'Nebraska'
  elif zipcode >= 88900 and zipcode <= 89999:
    st = 'NV'
    state = 'Nevada'
  elif zipcode >= 3000 and zipcode <= 3899:
    st = 'NH'
    state = 'New Hampshire'
  elif zipcode >= 7000 and zipcode <= 8999:
    st = 'NJ'
    state = 'New Jersey'
  elif zipcode >= 87000 and zipcode <= 88499:
    st = 'NM'
    state = 'New Mexico'
  elif zipcode >= 10000 and zipcode <= 14999:
    st = 'NY'
    state = 'New York'
  elif zipcode >= 43000 and zipcode <= 45999:
    st = 'OH'
    state = 'Ohio'
  elif zipcode >= 73000 and zipcode <= 74999:
    st = 'OK'
    state = 'Oklahoma'
  elif zipcode >= 97000 and zipcode <= 97999:
    st = 'OR'
    state = 'Oregon'
  elif zipcode >= 15000 and zipcode <= 19699:
    st = 'PA'
    state = 'Pennsylvania'
  elif zipcode >= 300 and zipcode <= 999:
    st = 'PR'
    state = 'Puerto Rico'
  elif zipcode >= 2800 and zipcode <= 2999:
    st = 'RI'
    state = 'Rhode Island'
  elif zipcode >= 29000 and zipcode <= 29999:
    st = 'SC'
    state = 'South Carolina'
  elif zipcode >= 57000 and zipcode <= 57999:
    st = 'SD'
    state = 'South Dakota'
  elif zipcode >= 37000 and zipcode <= 38599:
    st = 'TN'
    state = 'Tennessee'
  elif  zipcode >= 75000 and zipcode <= 79999 or zipcode >= 88500 and zipcode <= 88599:
    st = 'TX'
    state = 'Texas'
  elif zipcode >= 84000 and zipcode <= 84999:
    st = 'UT'
    state = 'Utah'
  elif zipcode >= 5000 and zipcode <= 5999:
    st = 'VT'
    state = 'Vermont'
  elif zipcode >= 22000 and zipcode <= 24699:
    st = 'VA'
    state = 'Virgina'
  elif zipcode >= 20000 and zipcode <= 20599:
    st = 'DC'
    state = 'Washington DC'
  elif zipcode >= 98000 and zipcode <= 99499:
    st = 'WA'
    state = 'Washington'
  elif zipcode >= 24700 and zipcode <= 26999:
    st = 'WV'
    state = 'West Virginia'
  elif zipcode >= 53000 and zipcode <= 54999:
    st = 'WI'
    state = 'Wisconsin'
  elif zipcode >= 82000 and zipcode <= 83199:
    st = 'WY'
    state = 'Wyoming'
  else:
    st = 'none'
    state = 'none'
  return state, st
run()