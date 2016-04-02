
week = range(1,18)
# Home Games Dictionary - Lists all 8 home games for each of 32 each
home_games = {
    'WAS':('DAL', 'NYG', 'PHI', 'GB', 'MIN', 'CAR', 'CLE', 'PIT'),
    'PHI':('DAL', 'NYG', 'WAS', 'GB', 'MIN', 'ATL', 'CLE', 'PIT'),
    'NYG':('DAL', 'PHI', 'WAS', 'CHI', 'DET', 'NO', 'BAL', 'CIN'),
    'DAL':('NYG', 'PHI', 'WAS', 'CHI', 'DET', 'TB', 'BAL', 'CIN'),
    'MIN':('CHI', 'DET', 'GB', 'DAL', 'NYG', 'ARZ', 'HOU', 'IND'),
    'GB':('CHI', 'DET', 'MIN', 'DAL', 'NYG', 'SEA', 'HOU', 'IND'),
    'DET':('CHI', 'GB', 'MIN', 'PHI', 'WAS', 'LAR', 'JAC', 'TEN'),
    'CHI':('DET', 'GB', 'MIN', 'PHI', 'WAS', 'SF', 'JAC', 'TEN'),
    'CAR':('DAL', 'NYG', 'WAS', 'GB', 'MIN', 'ATL', 'CLE', 'PIT'),
    'ATL':('CAR', 'NO', 'TB', 'ARZ', 'SF', 'GB', 'KC', 'SD'),
    'NO':('ATL', 'CAR', 'TB', 'LAR', 'SEA', 'DET', 'DEN', 'OAK'),
    'TB':('ATL', 'CAR', 'NO', 'LAR', 'SEA', 'CHI', 'DEN', 'OAK'),
    'ARZ':('LAR', 'SF', 'SEA', 'NO', 'TB', 'WAS', 'NE', 'NYJ'),
    'SEA':('ARZ', 'SF', 'LAR', 'ATL', 'CAR', 'PHI', 'BUF', 'MIA'),
    'LAR':('ARZ', 'SF', 'SEA', 'ATL', 'CAR', 'NYG', 'BUF', 'MIA'),
    'SF':('ARZ', 'LAR', 'SEA', 'NO', 'TB', 'DAL', 'NE', 'NYJ'),
    'NE':('BUF','MIA','NYJ','BAL','CIN','HOU','LAR','SEA'),
    'NYJ':('BUF','MIA','NE','BAL','CIN','IND','LAR','SEA'),
    'BUF':('MIA','NE','NYJ','CLE','PIT','JAC','ARZ','SF'),
    'MIA':('BUF','NE','NYJ','CLE','PIT','TEN','ARZ','SF'),
    'CIN':('BAL','CLE','PIT','BUF','MIA','DEN','PHI','WAS'),
    'PIT':('BAL','CIN','CLE','NE','NYJ','KC','DAL','NYG'),
    'BAL':('CIN','CLE','PIT','BUF','MIA','OAK','PHI','WAS'),
    'CLE':('BAL','CIN','PIT','NE','NYJ','SD','DAL','NYG'),
    'HOU':('IND','JAC','TEN','KC','SD','CIN','CHI','DET'),
    'IND':('HOU','JAC','TEN','KC','SD','PIT','CHI','DET'),
    'JAC':('HOU','IND','TEN','DEN','OAK','BAL','GB','MIN'),
    'TEN':('HOU','IND','JAC','DEN','OAK','CLE','GB','MIN'),
    'DEN':('KC','OAK','SD','HOU','IND','NE','ATL','CAR'),
    'KC':('DEN','OAK','SD','JAC','TEN','NYJ','NO','TB'),
    'OAK':('DEN','KC','SD','HOU','IND','BUF','ATL','CAR'),
    'SD':('DEN','KC','OAK','JAC','TEN','MIA','NO','TB')
}
# Away Games Dictionary - Lists all 8 away games for each of 32 teams
away_games = {
    'WAS': ('DAL', 'NYG', 'PHI', 'CHI', 'DET', 'ARZ', 'BAL', 'CIN'),
    'PHI': ('DAL', 'NYG', 'WAS', 'CHI', 'DET', 'SEA', 'BAL', 'CIN'),
    'NYG': ('DAL', 'PHI', 'WAS', 'GB', 'MIN', 'LAR', 'CLE', 'PIT'),
    'DAL': ('NYG', 'PHI', 'WAS', 'GB', 'MIN', 'SF', 'CLE', 'PIT'),
    'MIN': ('CHI', 'DET', 'GB', 'PHI', 'WAS', 'CAR', 'JAC', 'TEN'),
    'GB': ('CHI', 'DET', 'MIN', 'PHI', 'WAS', 'ATL', 'JAC', 'TEN'),
    'DET': ('CHI', 'GB', 'MIN', 'DAL', 'NYG', 'NO', 'HOU', 'IND'),
    'CHI': ('DET', 'GB', 'MIN', 'DAL', 'NYG', 'TB', 'HOU', 'IND'),
    'CAR': ('ATL', 'NO', 'TB', 'LAR', 'SEA', 'WAS', 'DEN', 'OAK'),
    'ATL': ('CAR', 'NO', 'TB', 'LAR', 'SEA', 'PHI', 'DEN', 'OAK'),
    'NO': ('ATL', 'CAR', 'TB', 'ARZ', 'SF', 'NYG', 'KC', 'SD'),
    'TB': ('ATL', 'CAR', 'NO', 'ARZ', 'SF', 'DAL', 'KC', 'SD'),
    'ARZ': ('LAR', 'SF', 'SEA', 'ATL', 'CAR', 'MIN', 'BUF', 'MIA'),
    'SEA': ('ARZ', 'SF', 'LAR', 'NO', 'TB', 'GB', 'NE', 'NYJ'),
    'LAR': ('ARZ', 'SF', 'SEA', 'NO', 'TB', 'DAL', 'NE', 'NYJ'),
    'SF': ('ARZ', 'LAR', 'SEA', 'ATL', 'CAR', 'CHI', 'BUF', 'MIA'),
    'NE': ('BUF', 'MIA', 'NYJ', 'CLE', 'PIT', 'DEN', 'ARZ', 'SF'),
    'NYJ': ('BUF', 'MIA', 'NE', 'CLE', 'PIT', 'KC', 'ARZ', 'SF'),
    'BUF': ('MIA', 'NE', 'NYJ', 'BAL', 'CIN', 'OAK', 'LAR', 'SEA'),
    'MIA': ('BUF', 'NE', 'NYJ', 'BAL', 'CIN', 'SD', 'LAR', 'SEA'),
    'CIN': ('BAL', 'CLE', 'PIT', 'NE', 'NYJ', 'HOU', 'DAL', 'NYG'),
    'PIT': ('BAL', 'CIN', 'CLE', 'BUF', 'MIA', 'IND', 'PHI', 'WAS'),
    'BAL': ('CIN', 'CLE', 'PIT', 'NE', 'NYJ', 'JAC', 'DAL', 'NYG'),
    'CLE': ('BAL', 'CIN', 'PIT', 'BUF', 'MIA', 'TEN', 'PHI', 'WAS'),
    'HOU': ('IND', 'JAC', 'TEN', 'DEN', 'OAK', 'NE', 'GB', 'MIN'),
    'IND': ('HOU', 'JAC', 'TEN', 'DEN', 'OAK', 'NYJ', 'GB', 'MIN'),
    'JAC': ('HOU', 'IND', 'TEN', 'KC', 'SD', 'BUF', 'CHI', 'DET'),
    'TEN': ('HOU', 'IND', 'JAC', 'KC', 'SD', 'MIA', 'CHI', 'DET'),
    'DEN': ('KC', 'OAK', 'SD', 'JAC', 'TEN', 'CIN', 'NO', 'TB'),
    'KC': ('DEN', 'OAK', 'SD', 'HOU', 'IND', 'PIT', 'ATL', 'CAR'),
    'OAK': ('DEN', 'KC', 'SD', 'JAC', 'TEN', 'BAL', 'NO', 'TB'),
    'SD': ('DEN', 'KC', 'OAK', 'HOU', 'IND', 'CLE', 'ATL', 'CAR')
}

# Conference Dictionary - Lists all 16 teams in each of two conferences
conference = {
    'AFC': ('NE', 'NYJ', 'BUF', 'MIA', 'CIN', 'PIT', 'BAL', 'CLE', 'HOU', 'IND', 'JAC',
            'TEN', 'DEN', 'KC', 'OAK', 'SD'),
    'NFC': ('WAS', 'PHI', 'NYG', 'DAL', 'MIN', 'GB', 'DET', 'CHI', 'CAR', 'ATL', 'NO',
            'TB', 'ARZ', 'SEA', 'LAR', 'SF')
}
# Division Dict - lists all 4 teams in each of 8 divisions
division = {
    'AFC': {
        'EAST': {'NE', 'NYJ', 'BUF', 'MIA'},
        'WEST': {'DEN', 'KC', 'OAK', 'SD'},
        'SOUTH': {'HOU', 'IND', 'JAC', 'TEN'},
        'NORTH': {'CIN', 'PIT', 'BAL', 'CLE'}
    },
    'NFC': {
        'EAST': {'WAS', 'PHI', 'NYG''DAL'},
        'WEST': {'ARZ', 'SEA', 'LAR', 'SF'},
        'SOUTH': {'CAR', 'ATL', 'NO', 'TB'},
        'NORTH': {'MIN', 'GB', 'DET', 'CHI'}
    }

}

# Time Slot Dictionary - Lists all network timeslots available each week
Slots = {1: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
             'MON_2_ESPN', 'THU_L_NBC'],
         2: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
             'THU_L_CBS'],
         3: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
             'THU_L_CBS'],
         4: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
             'THU_L_CBS'],
         5: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
             'THU_L_CBS'],
         6: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
             'THU_L_CBS'],
         7: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
             'THU_L_CBS'],
         8: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
             'THU_L_CBS'],
         9: ['SUN_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
             'THU_L_CBS'],
         10: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
              'THU_L_NFL'],
         11: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
              'THU_L_NFL'],
         12: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
              'THU_E_CBS', 'THU_L_FOX'],
         13: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
              'THU_L_NFL'],
         14: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
              'THU_L_NFL'],
         15: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
              'THU_L_NFL', 'SAT_E_NFL', 'SAT_L_NFL'],
         16: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
              'THU_L_NFL'],
         17: ['Sun_E_CBS', 'Sun_E_FOX', 'SUN_L_CBS', 'SUN_L_FOX', 'SUN_D_CBS', 'SUN_D_FOX', 'SUN_N_NBC', 'MON_1_ESPN',
              'THU_L_NFL']}
