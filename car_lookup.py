"""
Edmunds.com API Python wrapper - Car Market Value Lookup
Edmunds API Documentation: http://developer.edmunds.com/

author: Jon Fairbanks <admin@jlfairbanks.com>
"""

from edmunds import Edmunds
import json, ast, os
api = Edmunds('api_key')

cls = lambda: os.system('cls')

# Gather car details (NEW)
cls()
year = raw_input("What year is the car?: ")
make = raw_input("What make?: ")
model = raw_input("Model?: ")
mileage = raw_input("And approx. how many miles?: ")
proper_desc = year + ' ' + make + ' ' + model + ' w/ ' + mileage + ' mi.'

# Make the API call for styleID
id_endpoint = '/api/vehicle/v2/' + make + '/' + model + '/' + year + '/styles'
json_response = api.make_call(id_endpoint)

# Gather style ID details from Edmunds
styleID = json_response['styles'][0]['id']
styleID = str(styleID)
zip = '68138'

# Make the API call for current rough market value
tmv_endpoint = '/v1/api/tmv/tmvservice/calculateusedtmv?condition=Rough&styleid=' + styleID + '&mileage=' + mileage + '&zip=' + zip
json_response = api.make_call(tmv_endpoint)

# Gather current rough market value from Edmunds
rough_market_value = json_response['tmv']['totalWithOptions']['usedPrivateParty']
rough_market_value = '{0:.2f}'.format(rough_market_value)
rough_market_value = str(rough_market_value)

# Make the API call for current average market value
tmv_endpoint = '/v1/api/tmv/tmvservice/calculateusedtmv?condition=Average&styleid=' + styleID + '&mileage=' + mileage + '&zip=' + zip
json_response = api.make_call(tmv_endpoint)

# Gather current average market value from Edmunds
average_market_value = json_response['tmv']['totalWithOptions']['usedPrivateParty']
average_market_value = '{0:.2f}'.format(average_market_value)
average_market_value = str(average_market_value)

# Make the API call for current clean market value
tmv_endpoint = '/v1/api/tmv/tmvservice/calculateusedtmv?condition=Clean&styleid=' + styleID + '&mileage=' + mileage + '&zip=' + zip
json_response = api.make_call(tmv_endpoint)

# Gather current clean market value from Edmunds
clean_market_value = json_response['tmv']['totalWithOptions']['usedPrivateParty']
clean_market_value = '{0:.2f}'.format(clean_market_value)
clean_market_value = str(clean_market_value)

# Print TMV for vehicle 
cls()
user_response = 'Approx. Retail for ' + proper_desc + ' = $' + rough_market_value + ' - $' + clean_market_value + '\n'
print user_response

# Save details to a text file
with open("output.txt", "a") as myfile:
    myfile.write(user_response)

# For debugging purposes only, comment out before live
#print json_response
#print styleID
#print "*** End of Script ***"