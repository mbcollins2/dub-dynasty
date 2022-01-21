import pickle
from espn_api.basketball import League
import pandas as pd
import numpy as np


def download_league_data():
    league_id = 88932378
    year = 2022
    swid = '355F8053-8A6C-45DE-9F80-538A6CA5DE8C'
    espn_s2 = 'AEBfB5kMxA%2Fe%2BoXPbA15UjYAgeb%2FNj4TjVnyDuvZmvG8nfiUQWkwnT4uy2hEFFA0owGdXprxcUotW4D6hucgXSlbMxHX%2B%2BUP6rQhL0auJI6l351sgglKKGzHKGpt0%2FRhXG190sPtf8IHvkXRo7dyq0IYJb1RPDAOqU0Vrm3WogtTvUeSWVkdZA7VUGEH3dmsYnh3D4mV21YMw1gE2pwQSpLFhuYVtBDtc%2FyTT6o%2FRO8wefkb0D1A4rjId%2FFyoK4BvLgxF5sB0%2FQLU7AJcmJgL4E15c38LQ2Prv3EFi1sFlLxAg%3D%3D'

    league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)

    with open('league.pkl', 'wb') as l:
        pickle.dump(league, l)


def download_free_agents():
    p = open('league.pkl', 'rb')
    league = pickle.load(p)

    fa = pd.DataFrame()

    for player in league.free_agents(size=1000):
        # print(player.name, player.stats, player.stats['2022'].get('total')['GP'])
        row = []

        row.append(player.name)
        row.append(player.proTeam)
        row.append(player.position)
        row.append(player.injuryStatus)
        row.append(player.injured)

        # total
        try:
            row.append(player.stats['2022'].get('total')['GP'])
            row.append(player.stats['2022'].get('total')['GS'])
            row.append(player.stats['2022'].get('total')['MIN'])
            row.append(player.stats['2022'].get('total')['MPG'])
            row.append(player.stats['2022'].get('applied_total'))
            row.append(player.stats['2022'].get('applied_avg'))
        except:
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)

        # last 30
        try:
            row.append(player.stats['2022_last_30'].get('total')['GP'])
            row.append(player.stats['2022_last_30'].get('total')['GS'])
            row.append(player.stats['2022_last_30'].get('total')['MIN'])
            row.append(player.stats['2022_last_30'].get('total')['MPG'])
            row.append(player.stats['2022_last_30'].get('applied_total'))
            row.append(player.stats['2022_last_30'].get('applied_avg'))
        except:
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)

        # last 15
        try:
            row.append(player.stats['2022_last_15'].get('total')['GP'])
            row.append(player.stats['2022_last_15'].get('total')['GS'])
            row.append(player.stats['2022_last_15'].get('total')['MIN'])
            row.append(player.stats['2022_last_15'].get('total')['MPG'])
            row.append(player.stats['2022_last_15'].get('applied_total'))
            row.append(player.stats['2022_last_15'].get('applied_avg'))
        except:
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)

        # last 7
        try:
            row.append(player.stats['2022_last_7'].get('total')['GP'])
            row.append(player.stats['2022_last_7'].get('total')['GS'])
            row.append(player.stats['2022_last_7'].get('total')['MIN'])
            row.append(player.stats['2022_last_7'].get('total')['MPG'])
            row.append(player.stats['2022_last_7'].get('applied_total'))
            row.append(player.stats['2022_last_7'].get('applied_avg'))
        except:
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)
            row.append(np.nan)


        fa = fa.append([row])

    fa = fa.reset_index(drop=True)

    fa.columns = [
        'name'
        ,'team'
        ,'position'
        ,'injury_status'
        ,'injured'

        # total
        ,'total_gp'
        ,'total_gs'
        ,'total_min'
        ,'total_mpg'
        ,'total_fpts'
        ,'total_favg'

        # last 30
        ,'l30_gp'
        ,'l30_gs'
        ,'l30_min'
        ,'l30_mpg'
        ,'l30_fpts'
        ,'l30_favg'

        # last 15
        ,'l15_gp'
        ,'l15_gs'
        ,'l15_min'
        ,'l15_mpg'
        ,'l15_fpts'
        ,'l15_favg'

        # last 7
        ,'l7_gp'
        ,'l7_gs'
        ,'l7_min'
        ,'l7_mpg'
        ,'l7_fpts'
        ,'l7_favg'
    ]

    # replace NaN with 0
    fa = fa.fillna(0.0)

    # convert float cols to int
    fa.loc[:, fa.dtypes=='float'] = fa.select_dtypes(float).astype('int')

    # filter out players with no injury status as they appear to be inactive
    fa = fa.loc[fa.injury_status.str.len() != 0]

    # add ratio columns
    fa['total_gp_ratio'] = round(fa['total_gp'] / fa.total_gp.max(), 2)
    fa['l30_gp_ratio'] = round(fa['l30_gp'] / fa.l30_gp.max(), 2)
    fa['l15_gp_ratio'] = round(fa['l15_gp'] / fa.l15_gp.max(), 2)
    fa['l7_gp_ratio'] = round(fa['l7_gp'] / fa.l7_gp.max(), 2)

    fa['total_gs_ratio'] = round(fa['total_gs'] / fa.total_gs.max(), 2)
    fa['l30_gs_ratio'] = round(fa['l30_gs'] / fa.l30_gs.max(), 2)
    fa['l15_gs_ratio'] = round(fa['l15_gs'] / fa.l15_gs.max(), 2)
    fa['l7_gs_ratio'] = round(fa['l7_gs'] / fa.l7_gs.max(), 2)

    fa['total_min_ratio'] = round(fa['total_min'] / fa.total_min.max(), 2)
    fa['l30_min_ratio'] = round(fa['l30_min'] / fa.l30_min.max(), 2)
    fa['l15_min_ratio'] = round(fa['l15_min'] / fa.l15_min.max(), 2)
    fa['l7_min_ratio'] = round(fa['l7_min'] / fa.l7_min.max(), 2)

    fa['total_mpg_ratio'] = round(fa['total_mpg'] / fa.total_mpg.max(), 2)
    fa['l30_mpg_ratio'] = round(fa['l30_mpg'] / fa.l30_mpg.max(), 2)
    fa['l15_mpg_ratio'] = round(fa['l15_mpg'] / fa.l15_mpg.max(), 2)
    fa['l7_mpg_ratio'] = round(fa['l7_mpg'] / fa.l7_mpg.max(), 2)

    fa['total_fpts_ratio'] = round(fa['total_fpts'] / fa.total_fpts.max(), 2)
    fa['l30_fpts_ratio'] = round(fa['l30_fpts'] / fa.l30_fpts.max(), 2)
    fa['l15_fpts_ratio'] = round(fa['l15_fpts'] / fa.l15_fpts.max(), 2)
    fa['l7_fpts_ratio'] = round(fa['l7_fpts'] / fa.l7_fpts.max(), 2)

    fa['total_favg_ratio'] = round(fa['total_favg'] / fa.total_favg.max(), 2)
    fa['l30_favg_ratio'] = round(fa['l30_favg'] / fa.l30_favg.max(), 2)
    fa['l15_favg_ratio'] = round(fa['l15_favg'] / fa.l15_favg.max(), 2)
    fa['l7_favg_ratio'] = round(fa['l7_favg'] / fa.l7_favg.max(), 2)

    fa.to_csv('free_agents.csv', index=False)