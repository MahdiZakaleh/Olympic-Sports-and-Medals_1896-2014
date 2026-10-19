
import glssdoor_scraper as gs
import pandas as pd


df = gs.get_jobs('data scientist', 15, False, None, 5)
df.to_csv('glassdoor_jobs.csv', index=False)
