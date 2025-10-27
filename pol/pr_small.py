#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys


def dhondt(nSeats, votes, verbose=False):
    """
    Author: https://gist.github.com/brunosan
    nSeats is the number of seats
    votes is a dictionary with the key:value {'party':votes}
    verbose is an option to print designation info
    """
    t_votes=votes.copy()
    seats={}
    for key in votes: seats[key]=0
    while sum(seats.values()) < nSeats:
        max_v= max(t_votes.values())
        next_seat=list(t_votes.keys())[list(t_votes.values()).index(max_v)]
        if next_seat in seats:
            seats[next_seat]+=1
        else:
            seats[next_seat]=1

        if verbose: 
            print("Round {}: {}".format(sum(seats.values()),next_seat))
            for key in t_votes:
                print("\t{} [{}]: {:.1f}".format(key,seats[key],t_votes[key]))
            print("\b")
        t_votes[next_seat]=votes[next_seat]/(seats[next_seat]+1)
    return seats


infile = sys.argv[1] #'electoral_calculus_data/1955.csv'
print('\nElection year:',infile)
data = pd.read_csv(infile,delimiter=';')

mlist = [["Fermanagh and South Tyrone","Tyrone West","Foyle","Londonderry East","Ulster Mid"], ["Bristol Central","Bristol North West","Bristol North East","Filton and Bradley Stoke","Thornbury and Yate"], ["Weston-super-Mare","Wells and Mendip Hills","Frome and East Somerset","Glastonbury and Somerton","Yeovil"], ["Ayrshire North and Arran","Ayrshire Central","Kilmarnock and Loudoun","Ayr, Carrick and Cumnock","Dumfries and Galloway"], ["Dunfermline and Dollar","Cowdenbeath and Kirkcaldy","Glenrothes and Mid Fife","Fife North East"], ["Cumbernauld and Kirkintilloch","Airdrie and Shotts","Coatbridge and Bellshill","Motherwell, Wishaw and Carluke"], ["Northumberland North","Hexham","Cramlington and Killingworth","Blyth and Ashington"], ["Darlington","Stockton West","Stockton North","Middlesbrough and Thornaby East","Middlesbrough South and East Cleveland","Redcar"], ["Wetherby and Easingwold","Harrogate and Knaresborough","York Outer","York Central","Selby"], ["Scunthorpe","Brigg and Immingham","Great Grimsby and Cleethorpes","Gainsborough","Lincoln"], ["Norfolk North West","Broadland and Fakenham","Norfolk North","Great Yarmouth","Norwich North"], ["Ely and East Cambridgeshire","St Neots and Mid Cambridgeshire","Cambridgeshire South","Cambridge"], ["Hereford and South Herefordshire","Herefordshire North","Shropshire South","Shrewsbury","Shropshire North","Wrekin, The","Telford"], ["Cardiff South and Penarth","Cardiff East","Cardiff West","Cardiff North","Vale of Glamorgan","Bridgend"], ["Chester North and Neston","Ellesmere Port and Bromborough","Wirral West","Birkenhead","Wallasey"], ["Morecambe and Lunesdale","Lancaster and Wyre","Blackpool North and Fleetwood","Blackpool South","Fylde","Preston","Ribble Valley"], ["Keighley and Ilkley","Shipley","Bradford South","Bradford West","Bradford East"], ["Ashton-under-Lyne","Stalybridge and Hyde","Gorton and Denton","Stockport","Hazel Grove","Cheadle"], ["Leigh and Atherton","Bolton West","Bolton South and Walkden","Bolton North East","Worsley and Eccles","Salford"], ["Sheffield Brightside and Hillsborough","Sheffield Central","Sheffield Heeley","Sheffield South East"], ["Stratford-on-Avon","Warwick and Leamington","Kenilworth and Southam","Rugby","Nuneaton","Warwickshire North and Bedworth"], ["Derbyshire South","Derby South","Derby North","Derbyshire Mid","Erewash"], ["Wolverhampton West","Wolverhampton North East","Wolverhampton South East","Walsall and Bloxwich","Aldridge-Brownhills"], ["Leicester West","Leicester South","Harborough, Oadby and Wigston","Leicester East","Melton and Syston","Rutland and Stamford"], ["Milton Keynes North","Milton Keynes Central","Buckingham and Bletchley","Aylesbury"], ["Newbury","Reading West and Mid Berkshire","Reading Central","Earley and Woodley","Wokingham","Bracknell"], ["Rochester and Strood","Chatham and Aylesford","Maidstone and Malling","Faversham and Mid Kent","Sittingbourne and Sheppey","Gillingham and Rainham"], ["Fareham and Waterlooville","Gosport","Portsmouth South","Portsmouth North","Havant"], ["Erith and Thamesmead","Bexleyheath and Crayford","Old Bexley and Sidcup","Bromley and Biggin Hill","Orpington","Eltham and Chislehurst"], ["Wimbledon","Mitcham and Morden","Sutton and Cheam","Carshalton and Wallington"], ["Ealing Southall","Ealing North","Hayes and Harlington","Uxbridge and South Ruislip","Ruislip, Northwood and Pinner"], ["Southgate and Wood Green","Enfield North","Edmonton and Winchmore Hill","Hornsey and Friern Barnet","Tottenham"], ["Antrim North","Antrim East","Antrim South","Lagan Valley"], ["Plymouth Moor View","Plymouth Sutton and Devonport","Devon South West","Devon South","Torbay"], ["Dorset West","Dorset North","Dorset Mid and North Poole","Dorset South"], ["Taunton and Wellington","Bridgwater","Tiverton and Minehead","Devon North"], ["Moray West, Nairn and Strathspey","Gordon and Buchan","Aberdeenshire North and Moray East","Aberdeenshire West and Kincardine","Aberdeen South","Aberdeen North"], ["Dunbartonshire West","Glasgow West","Glasgow North","Dunbartonshire Mid", ,"Glasgow North East"], ["Alloa and Grangemouth","Bathgate and Linlithgow","Falkirk","Livingston"], ["Washington and Gateshead South","Houghton and Sunderland South","Sunderland Central","South Shields","Jarrow and Gateshead East","Gateshead Central and Whickham"], ["Richmond and Northallerton","Skipton and Ripon","Thirsk and Malton","Scarborough and Whitby"], ["Suffolk Central and North Ipswich","Waveney Valley","Suffolk Coastal","Lowestoft"], ["Cambridgeshire North East","Peterborough","Cambridgeshire North West","Huntingdon"], ["Brecon, Radnor and Cwm Tawe","Caerfyrddin (Carmarthen)","Ceredigion Preseli","Pembrokeshire Mid and South","Llanelli"], ["Alyn and Deeside","Clwyd East","Wrexham","Clwyd North"], ["Widnes and Halewood","St Helens South and Whiston","Liverpool Garston","Knowsley","Warrington North","Warrington South"], ["Calder Valley","Halifax","Colne Valley","Huddersfield"], ["Doncaster North","Doncaster Central","Doncaster East and the Isle of Axholme","Rawmarsh and Conisbrough","Rother Valley","Rotherham"], ["Banbury","Bicester and Woodstock","Witney","Didcot and Wantage","Oxford West and Abingdon","Oxford East","Henley and Thame"], ["Smethwick","Halesowen","Stourbridge","Dudley","Tipton and Wednesbury","West Bromwich"], ["Hinckley and Bosworth","Leicestershire Mid","Loughborough","Leicestershire North West","Leicestershire South"], ["Hitchin","Stevenage","Welwyn Hatfield","Hertfordshire North East","Broxbourne","Hertford and Stortford"], ["Godalming and Ash","Guildford","Woking","Surrey Heath","Aldershot","Farnham and Bordon"], ["Chelmsford","Maldon","Rayleigh and Wickford","Castle Point","Southend West and Leigh","Southend East and Rochford"], ["Sussex Weald","Bexhill and Battle","Hastings and Rye","Eastbourne","Lewes","East Grinstead and Uckfield"], ["Thanet East","Herne Bay and Sandwich","Canterbury","Dover and Deal"], ["Romsey and Southampton North","Southampton Test","Southampton Itchen","Eastleigh","Hamble Valley"], ["Streatham and Croydon North","Croydon West","Croydon South","Croydon East","Beckenham and Penge"], ["Richmond Park","Kingston and Surbiton","Twickenham","Brentford and Isleworth","Feltham and Heston"], ["Brent East","Brent West","Harrow West","Harrow East","Hendon","Finchley and Golders Green","Chipping Barnet"], ["Chingford and Woodford Green","Walthamstow","Leyton and Wanstead","Stratford and Bow","West Ham and Beckton","East Ham"], ["Belfast North","Belfast West","Belfast South and Mid Down","Belfast East"], ["Cornwall South East","Cornwall North","St Austell and Newquay","Truro and Falmouth","St Ives","Camborne and Redruth"], ["Poole","Bournemouth West","Bournemouth East","Christchurch"], ["Salisbury","Wiltshire East","Melksham and Devizes","Wiltshire South West"], ["Orkney and Shetland","Caithness, Sutherland and Easter Ross","Inverness, Skye and West Ross-shire","Argyll, Bute and South Lochaber","Na h-Eileanan An Iar (Western Isles)"], ["Edinburgh South","Edinburgh South West","Edinburgh West","Edinburgh North and Leith","Edinburgh East and Musselburgh"], ["East Kilbride and Strathaven","Hamilton and Clyde Valley","Rutherglen","Glasgow East"], ["Carlisle","Penrith and Solway","Westmorland and Lonsdale","Barrow and Furness","Whitehaven and Workington"], ["Newcastle upon Tyne Central and West","Newcastle upon Tyne North","Newcastle upon Tyne East and Wallsend","Tynemouth"], ["Goole and Pocklington","Beverley and Holderness","Bridlington and the Wolds","Hull East","Hull North and Cottingham","Hull West and Haltemprice"], ["Sleaford and North Hykeham","Grantham and Bourne","South Holland and The Deepings","Boston and Skegness","Louth and Horncastle"], ["Norfolk South West","Norfolk Mid","Norfolk South","Norwich South"], ["Braintree","Witham","Colchester","Harwich and North Essex","Clacton","Essex North West"], ["Cotswolds North","Cheltenham","Tewkesbury","Forest of Dean","Stroud","Gloucester"], ["Merthyr Tydfil and Aberdare","Caerphilly","Pontypridd","Rhondda and Ogmore"], ["Bangor Aberconwy","Dwyfor Meirionnydd","Montgomeryshire and Glyndwr","Ynys Mon (Anglesey)"], ["Lancashire West","South Ribble","Chorley","Makerfield","St Helens North","Wigan"], ["Pontefract, Castleford and Knottingley","Normanton and Hemsworth","Wakefield and Rothwell","Ossett and Denby Dale","Spen Valley","Dewsbury and Batley"], ["Oldham East and Saddleworth","Oldham West, Chadderton and Royton","Rochdale","Heywood and Middleton North","Bury South","Bury North","Blackley and Middleton South"], ["Runcorn and Helsby","Chester South and Eddisbury","Crewe and Nantwich","Cheshire Mid","Congleton","Tatton","Macclesfield"], ["Burton and Uttoxeter","Stone, Great Wyrley and Penkridge","Lichfield","Cannock Chase","Tamworth","Kingswinford and South Staffordshire"], ["Solihull West and Shirley","Birmingham Selly Oak","Birmingham Northfield","Birmingham Edgbaston","Birmingham Hall Green and Moseley","Birmingham Yardley"], ["Rushcliffe","Broxtowe","Nottingham South","Nottingham North and Kimberley","Nottingham East","Gedling"], ["Northamptonshire South","Daventry","Northampton South","Northampton North","Corby and East Northamptonshire","Kettering","Wellingborough and Rushden"], ["Hertfordshire South West","Watford","Hemel Hempstead","Harpenden and Berkhamsted","St Albans","Hertsmere"], ["Slough","Windsor","Runnymede and Weybridge","Spelthorne","Esher and Walton"], ["Sevenoaks","Tonbridge","Dartford","Gravesham"], ["Chichester","Arundel and South Downs","Horsham","Crawley","Sussex Mid"], ["Barking","Dagenham and Rainham","Hornchurch and Upminster","Romford","Ilford South","Ilford North"], ["Bermondsey and Old Southwark","Peckham","Lewisham West and East Dulwich","Lewisham East","Lewisham North","Greenwich and Woolwich"], ["Ealing Central and Acton","Hammersmith and Chiswick","Kensington and Bayswater","Chelsea and Fulham","Queen's Park and Maida Vale"], ["Upper Bann","Newry and Armagh","Down South","Strangford","Down North"], ["Newton Abbot","Devon Central","Exeter","Exmouth and Exeter East","Honiton and Sidmouth","Torridge and Tavistock"], ["New Forest West","New Forest East","Isle of Wight West","Isle of Wight East"], ["Somerset North","Somerset North East and Hanham","Bath","Bristol South","Bristol East"], ["Angus and Perthshire Glens","Perth and Kinross-shire","Dundee Central","Arbroath and Broughty Ferry","Stirling and Strathallan"], ["Dumfriesshire, Clydesdale and Tweeddale","Berwickshire, Roxburgh and Selkirk","Midlothian","Lothian East"], ["Inverclyde and Renfrewshire West","Paisley and Renfrewshire North","Paisley and Renfrewshire South","Renfrewshire East","Glasgow South West","Glasgow South"], ["Bishop Auckland","Newton Aycliffe and Spennymoor","Durham, City of","Easington","Hartlepool","Durham North","Blaydon and Consett"], ["Bury St Edmunds and Stowmarket","Suffolk West","Ipswich","Suffolk South"], ["Cotswolds South","Chippenham","Swindon South","Swindon North"], ["Worcestershire West","Worcester","Droitwich and Evesham","Redditch","Bromsgrove","Wyre Forest"], ["Monmouthshire","Torfaen","Newport East","Newport West and Islwyn","Blaenau Gwent and Rhymney"], ["Gower","Swansea West","Neath and Swansea East","Aberafan Maesteg"], ["Blackburn","Rossendale and Darwen","Hyndburn","Burnley","Pendle and Clitheroe"], ["Sefton Central","Bootle","Liverpool Walton","Liverpool West Derby","Liverpool Wavertree","Liverpool Riverside","Southport"], ["Leeds North West","Leeds North East","Leeds Central and Headingley","Leeds West and Pudsey","Leeds South West and Morley","Leeds South","Leeds East"], ["Manchester Central","Manchester Rusholme","Stretford and Urmston","Manchester Withington","Wythenshawe and Sale East","Altrincham and Sale West"], ["Penistone and Stocksbridge","Barnsley North","Barnsley South","Sheffield Hallam"], ["Staffordshire Moorlands","Stoke-on-Trent North","Newcastle-under-Lyme","Stoke-on-Trent Central","Stafford","Stoke-on-Trent South"], ["Meriden and Solihull East","Coventry North West","Coventry South","Coventry East"], ["Bassetlaw","Newark","Sherwood Forest","Mansfield","Ashfield"], ["Bedfordshire North","Bedford","Bedfordshire Mid","Dunstable and Leighton Buzzard","Luton North","Luton South and South Bedfordshire"], ["Buckinghamshire Mid","Wycombe","Chesham and Amersham","Beaconsfield","Maidenhead"], ["Epsom and Ewell","Dorking and Horley","Reigate","Surrey East"], ["Thurrock","Basildon South and East Thurrock","Basildon and Billericay","Brentwood and Ongar","Epping Forest","Harlow"], ["Bognor Regis and Littlehampton","Worthing West","Worthing East and Shoreham","Hove and Portslade","Brighton Pavilion","Brighton Kemptown and Peacehaven"], ["Tunbridge Wells","Weald of Kent","Ashford","Folkestone and Hythe"], ["Hampshire North West","Basingstoke","Hampshire North East","Hampshire East","Winchester"], ["Putney","Tooting","Battersea","Clapham and Brixton Hill","Dulwich and West Norwood","Vauxhall and Camberwell Green"], ["Poplar and Limehouse","Bethnal Green and Stepney","Hackney South and Shoreditch","Hackney North and Stoke Newington"], ["High Peak","Derbyshire Dales","Derbyshire North East","Chesterfield","Bolsover","Amber Valley"], ["Birmingham Perry Barr","Birmingham Ladywood","Birmingham Hodge Hill and Solihull North","Birmingham Erdington","Sutton Coldfield"], ["Islington North","Hampstead and Highgate","Holborn and St Pancras","Cities of London and Westminster","Islington South and Finsbury"]]
consts = data['Name'].unique()

#print(data)
name_to_index = {
    name: index
    for index, sublist in enumerate(mlist)
    for name in sublist
}

# Add a new column "Const" to the DataFrame
data["ConstIdx"] = data["Name"].map(name_to_index) # find the NaN's first.astype(int)

# Check NaNs
nan_rows = data["Name"][pd.isna(data["ConstIdx"])]
nrtl = nan_rows.tolist()
for r in nrtl:
    print(r)

##############################################################

counties = data['ConstIdx'].unique()
county_votes = []
electorates = {}
seats = {}
party_votes = {}
rnd_seats = []

for cou in counties:
    county_votes.append(data.loc[data['ConstIdx'] == cou, 'Electorate'].sum())

for i in range(len(counties)):
    electorates[counties[i]] = county_votes[i]
    try:
        party_votes[counties[i]] = {'CON': data.loc[data['ConstIdx'] == counties[i], 'CON'].sum(),
                                'LAB': data.loc[data['ConstIdx'] == counties[i], 'LAB'].sum(),
                                'LIB': data.loc[data['ConstIdx'] == counties[i], 'LIB'].sum(),
                                'UKIP': data.loc[data['ConstIdx'] == counties[i], 'UKIP'].sum(),
                                'Green': data.loc[data['ConstIdx'] == counties[i], 'Green'].sum(),
                                'NAT': data.loc[data['ConstIdx'] == counties[i], 'NAT'].sum(),
                                'MIN': data.loc[data['ConstIdx'] == counties[i], 'MIN'].sum(),
                                'OTH': data.loc[data['ConstIdx'] == counties[i], 'OTH'].sum()}
    except:
        party_votes[counties[i]] = {'CON': data.loc[data['ConstIdx'] == counties[i], 'CON'].sum(),
                                'LAB': data.loc[data['ConstIdx'] == counties[i], 'LAB'].sum(),
                                'LIB': data.loc[data['ConstIdx'] == counties[i], 'LIB'].sum(),
                                'NAT': data.loc[data['ConstIdx'] == counties[i], 'NAT'].sum(),
                                'MIN': data.loc[data['ConstIdx'] == counties[i], 'MIN'].sum(),
                                'OTH': data.loc[data['ConstIdx'] == counties[i], 'OTH'].sum()}

for lst in mlist:
    rnd_seats.append(int(len(lst)))

gb_res = []

print('\n')
gbiv = iter(rnd_seats)
for gk, gi in party_votes.items():
    print(gk)
    results = dhondt(next(gbiv), gi, verbose=False)
    print(mlist[int(gk)],': ',results, max(gi, key=gi.get)) #,max(gi.values()))
    print('\n')
    gb_res.append(results)
tots = {k: sum(d[k] for d in gb_res if k in d) for k in set(k for d in gb_res for k in d)}

print('UK', tots,'\n')
