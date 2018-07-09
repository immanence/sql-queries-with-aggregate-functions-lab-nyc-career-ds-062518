def total_seasons():
    return "SELECT count(year) FROM babe_ruth_stats;"

def total_seasons_with_ny():
    return "SELECT count(*) FROM babe_ruth_stats WHERE team = 'NY'"

def most_hr():
    return "SELECT max(hr) FROM babe_ruth_stats;"

def least_hr():
    return "SELECT min(hr) FROM babe_ruth_stats;"

def total_hr():
    return "SELECT sum(hr) FROM babe_ruth_stats;"

def average_hr_per_year():
    return "SELECT avg(hr) FROM babe_ruth_stats;"

def year_and_games_with_least_hr():
    return "SELECT year, games FROM babe_ruth_stats WHERE hr = 0;"

def select_yr_and_min_hr_with_at_least_100_games():
    return "SELECT year, min(hr) FROM babe_ruth_stats WHERE games >= 100;"

def avg_batting_avg_aliased_as_career_average():
    return "SELECT avg(avg) as career_average FROM babe_ruth_stats;"

def total_years_and_hits_per_team():
    return "SELECT team, count(year), sum(hits) FROM babe_ruth_stats GROUP BY team;"

def total_years_and_hr_per_team_ordered_by_hr():
    return "SELECT team, count(year), sum(hr) FROM babe_ruth_stats GROUP BY team ORDER BY team DESC;"

def years_with_on_base_over_300():
    return "SELECT year, hits + bb AS on_base FROM babe_ruth_stats GROUP BY year HAVING on_base > 300;"
