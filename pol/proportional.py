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


def read_file(csvfile):
    '''
    1/ Read the CSV file and return a pandas DataFrame.
    2/ Replace NI counties with "Northern Ireland".
    3/ Replace area numerical codes with area names.
    '''
    dataitem = pd.read_csv(csvfile, sep=";")

    dataitem["County"] = \
dataitem["County"].replace(["Antrim", "Armagh", "Down",\
                            "Fermanagh", "Londonderry", "Tyrone"],
                            "Northern Ireland")

    areaname = {"Northern Ireland": 1, "Scotland": 2, "North East": 4, 
                "North West": 5, "Yorkshire and the Humber": 6, 
                "East Midlands": 7, "West Midlands": 8, "East of England": 9, 
                "London": 10, "South East": 11, "South West": 12}

    area_names_by_code = {code: name for name, code in areaname.items()}
    dataitem["Area"] = dataitem["Area"].replace(area_names_by_code)

    return dataitem


def get_county_totals(dataitem, verbose=False, region=False):
    '''
    1/ Determine the list of parties based on the presence of the "Green" column.
    2/ Calculate the total votes for each county or area.
    3/ Calculate the total number of seats for each county or area.
    4/ Print the seat totals if verbose is True.
    5/ Return the county totals and seat totals.
    '''

    if "Green" in dataitem:
        parties = ["CON", "LAB", "LIB", "UKIP", "Green", "NAT", "MIN", "OTH"]
    else:
        parties = ["CON", "LAB", "LIB", "NAT", "MIN", "OTH"]

    if region:
        county_totals = dataitem.groupby("Area")[parties].sum().to_dict(orient="index")
        seat_totals = dataitem.groupby("Area")["Name"].count().to_dict()
    else:
        county_totals = dataitem.groupby("County")[parties].sum().to_dict(orient="index")
        seat_totals = dataitem.groupby("County")["Name"].count().to_dict()

    if verbose:
        print(f'{sorted(seat_totals.items(), key=lambda x: x[1], reverse=True)}\n')

    return county_totals, seat_totals


def do_election(results, seats, verbose=False):
    '''
    1/ Perform the election using the D'Hondt method for each constituency.
    2/ Calculate the winner and vote percentages for each party.
    3/ Print detailed results if verbose is True.
    4/ Return the elected results and vote shares.
    '''

    elected = {}
    vote_shares = {}
    for constituency, result in results.items():
        election = dhondt(seats[constituency], result, verbose=False)
        winner = max(election, key=election.get)
        total_votes = sum(result.values())
        vote_percentages = {
            party: (votes / total_votes) * 100
            for party, votes in result.items()
        }
        long_results = [
            (party, f"{percentage:.2f}%")
            for party, percentage in sorted(
                vote_percentages.items(), key=lambda item: item[1], reverse=True
            )
        ]
        if verbose:
            print(f'{constituency} {election} {winner}\n{long_results}\n')
        elected[constituency] = election
        vote_shares[constituency] = vote_percentages


    return elected, vote_shares


csvfile = './electoral_calculus_data/2026-08ECpoll-County.csv'
ditem = read_file(csvfile)
results, seats = get_county_totals(ditem, verbose=True, region=False)
elected, vote_shares = do_election(results, seats, verbose=True)
