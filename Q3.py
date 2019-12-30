import pandas as pd
import numpy as np
import pandas as pd

df = pd.read_csv('C:\pythontest\movie.csv',delimiter = ',', names = ['actorname','moviename'])

gm = df[['actorname','moviename']].groupby(['actorname']).size().reset_index(name='counts')
gs = print(gm.sort_values('counts', ascending=False))
print(gs)

#gc = gs.filter(lambda x: x['counts'].size() > 3)
#df[['actorname','moviename']].groupby(['actorname']).value_counts().loc#[lambda x: x>3]

#countss = df.groupby('actorname')['moviename'].value_counts()
#gf= gs.filter(lambda x: x['counts'].count() > 3)
#print(gc)


