import pandas as pd, numpy as np
import re
from pathlib import Path

ddir = Path(__file__).parent / 'data'
print(ddir)

df_param = pd.read_csv(ddir / 'Parms.txt', sep='\t').rename(columns=lambda x: re.sub(' ', '_', x.lower())).rename(columns={'parm_code': 'parameter_cd', 'name':'parameter_name'})
df_unit = pd.read_csv(ddir / 'Units.txt', sep='\t').rename(columns=lambda x: re.sub(' ', '_', x.lower())).loc[:, ['code', 'abbr']].rename(columns={'code': 'unit_cd', 'abbr': 'unit_abbr'})
df_site_all = pd.read_csv(ddir / 'Site.txt', sep='\t').rename(columns=lambda x: re.sub(' ', '_', x.lower())).rename(columns={'aqs_code': 'aqs_cd'})
##df_param = pd.read_csv('parameters.csv')
df_meth0 = pd.read_csv(ddir / 'methods_all.csv').rename(columns=lambda x: re.sub(' ', '_', x.lower())).rename(columns={'parameter_code':'parameter_cd', 'method_code': 'meth_cd'})
df_meth = df_meth0.loc[:, [
 'parameter_cd', 'meth_cd', 'recording_mode',
       'collection_description', 'analysis_description', 'federal_mdl',]]

def reader(fn):
    df = (pd.read_csv(fn, sep='|', skiprows = 10)
            .rename(columns=lambda x: re.sub(' ', '_', x.lower()))
            .iloc[:, :13]
            .assign(aqs_cd=lambda x: (1000*x.state_cd + x.county_cd)*10000 + x.site_id)
            )
    return df

def proc(df, kind=None):
    df_meta = df[['parameter_cd',  'unit_cd',  'meth_cd']].drop_duplicates().merge(df_param).merge(df_unit).merge(df_meth)
    df_meta.insert(0, 'kind', kind)

    df_site = df[['aqs_cd']].drop_duplicates().merge(df_site_all)
    df_site.insert(0, 'kind', kind)
    return df_meta, df_site

if __name__ == '__main__':
    import sys
    fn = sys.argv[1]
    df = reader(fn)
    df2 = proc(df, kind=None)

