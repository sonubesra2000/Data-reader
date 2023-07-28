import pandas as pd
import requests

def data_reader(start_date, end_date):
    url = f"https://o2power.api.sgrids.io/integration/customapi/64ba5ef041f56767b129032d?startdate={start_date}&enddate={end_date}"
    payload = {}
    headers = {
    'accept': 'application/json',
    'utcoffset': '330',
    'X-PROD-RADIATICS-CUSTOM-API': 'CvCTg4pelm7M8W00VSww0pgpTCelkBbsiVsbW8pDniRGRKKoLceHnufp6ugCPTvxCtoEayzTX2fy2kaC3Xdoi43zhPChBdRReGfPeAgxxF40CxYdOVssVBHSCLInSaOIeIpQz1LhDkqtjPB2eqORGto2xCSsZpQ2IcSxsWKOSgDeKiIKRh5w90839pWHoeJi0q27keH0ksgzpRBP854qKaHfDL3bdNmLZsxGLk2wCCuH96qwIC4Hd6QRn9NjsfqW',
    'Cookie': 'AWSALB=HlbLgjsLHAW6sy6gBhr3+ha86TB0dQn0T1E9tu9vMfZ5tlqeky5Z0RshfSM+k7cZqkw2JPJMinFQ8ril9WscSYQXXq+63NLJ81Ycj7yWe6UMVxw9U4dDZ3pB8pR4; AWSALBCORS=HlbLgjsLHAW6sy6gBhr3+ha86TB0dQn0T1E9tu9vMfZ5tlqeky5Z0RshfSM+k7cZqkw2JPJMinFQ8ril9WscSYQXXq+63NLJ81Ycj7yWe6UMVxw9U4dDZ3pB8pR4'
    }
    response = requests.get(url, headers=headers,data=payload)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data["data"]) 
        df['AC_POWER_SUM']=df.drop(columns=['planttimestamp', 'planttimestring']).sum(axis=1)
        df=df.rename(columns={'planttimestring':'Time'})
        df=df.drop('planttimestamp',axis=1)
        return df.reset_index(drop=True)
    else:
        print("Failed to retrieve data from the API")
        return None
